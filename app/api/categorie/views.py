from typing import List
from fastapi import APIRouter, status, Depends
from .schemas import CategorieSchema, ShowCategorieSchema
from fastapi.param_functions import Depends
from app.db.db import get_db
from app.models.models import Categorie
from app.repositories.categorie_repository import CategorieRepository
from app.services.auth_service import get_user, only_admin
from sqlalchemy.orm import Session
#sem implementar autenticaçao
#router = APIRouter ()   #(dependencies=[Depends(only_admin)])
router = APIRouter(dependencies=[Depends(only_admin)])

# @router.post('/', status_code=status.HTTP_201_CREATED,)
# def create(categorie: CategorieSchema, repository : CategorieRepository = Depends()):
#     repository.create(Categorie(**categorie.dict()))

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowCategorieSchema)
def create(category: CategorieSchema, db: Session = Depends(get_db)):
    model = Categorie(**category.dict())
    db.add(model)
    db.commit()
    db.refresh(model)
    
    return model

# @router.get('/', response_model=List[ShowCategorieSchema])
# def index(repository: CategorieRepository = Depends()):
#     return repository.get_all()
@router.get('/', response_model=List[ShowCategorieSchema])
def index(db: Session = Depends(get_db)):
    return db.query(Categorie).all()


# @router.put('/{id}')
# def update(id: int, categorie: CategorieSchema, repository: CategorieRepository = Depends()):
#     repository.update(id, categorie.dict())
@router.put('/{id}', response_model=ShowCategorieSchema)
def update(id: int, category: CategorieSchema, db: Session = Depends(get_db)):
    query = db.query(Categorie).filter_by(id=id)
    query.update(category.dict())
    db.commit()
    return db.query(Categorie).filter_by(id=id).first()

# @router.get('/{id}', response_model=ShowCategorieSchema)
# def show(id: int, repository: CategorieRepository = Depends()):
#     return repository.get_by_id(id)
@router.get('/{id}', response_model=ShowCategorieSchema)
def show(id: int, db: Session = Depends(get_db)):
    return db.query(Categorie).filter_by(id=id).first()