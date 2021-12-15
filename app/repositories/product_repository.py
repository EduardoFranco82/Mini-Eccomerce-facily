from fastapi_pagination.ext.sqlalchemy import paginate #importar da extensao correta
from .base_repository import BaseRepository
from fastapi import Depends
from sqlalchemy.orm import Session, joinedload
from app.db.db import get_db
from app.models.models import Categorie, Product, ProductDiscount
from app.api.catalog.schemas import CatalogFilter

class ProductRepository(BaseRepository):# --> pega o crud de base_repository
    def __init__(self, session: Session = Depends (get_db)) :
        super().__init__(session, Product)

    # TUDO QUE FIZER AGORA , E PARA FAZER UM FILTRO DENTRO DA TABELA PRODUTO
    # O QUE ESTOU TENTANDO FILTAR EU PRE ESTABELECI NO SCHEMA
    def get_for_catalog (self, filter: CatalogFilter): # tem que filtrar para ter acesso aos parametros 
      # return self.query().filter(Categorie.name == 'eletrodomesticos').join(Categorie).all()# exemplo de puxar com join
        query = self.query()
        queryset = [Product.visible == True]# por causa da regra de visibilidade da api
        if filter.category_name:
            queryset.append(Categorie.name == filter.category_name)
           # query = query.join(Categorie)
        if filter.category_id: # se for diferente de none
            queryset.append(Product.categorie_id == filter.category_id)
        if filter.supplier_id:
            queryset.append(Product.supplier_id == filter.supplier_id)
        if filter.min_price :
            queryset.append(Product.price >= filter.min_price)
        if filter.max_price:
            queryset.append(Product.price <= filter.max_price)
        if filter.description:
            queryset.append(Product.description.like(f'%{filter.description}%'))#%% producrar a palavra independente da posiçao da string completa , so no inicio vai terminar, so final vai começar

        
        #self.query().filter(Product.categorie_id == filter.category_id)
        #self.query().filter(Product.price > 100) -> so da pra fazer com filter, filterby nao


       #1 return que ensinou return self.query().filter(*queryset).all()#com 1 asterisco so pega os valores e divide por virgula, com 2 asteriscos faz dicionario, chave valor
        #self.query().filter(Product.description == '', Product.price > 100) o que fez emcima e a mesma coisa
        #self.query().filter().filter() poderia fazer assim, porem , fez filter(*queryset)
        query = query.filter(*queryset).options(joinedload(Product.categorie), 
        joinedload(Product.supplier), 
        joinedload(Product.discounts).subqueryload(ProductDiscount.payment_method))
        #return com pagination
        return paginate(query)