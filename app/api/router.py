from fastapi import APIRouter
from .product.views import router as product_router
from .suppliers.views import router as supplier_router
from .categorie.views import router as categorie_router
from .payment_methods.views import router as payment_methods_router
from .product_discount.views import router as product_discount_router


router = APIRouter()


router.include_router(product_router, prefix='/product', tags=['product']) # --> prefix adiciona o /product na rota @app.router('')
router.include_router(supplier_router, prefix='/supplier', tags=['supplier'])
router.include_router(categorie_router, prefix='/categorie', tags=['categorie'])
router.include_router(payment_methods_router, prefix='/payment_methods', tags=['payment_methods'])
router.include_router(product_discount_router, prefix='/product_discount', tags=['product_discount'])
