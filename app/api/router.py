from fastapi import APIRouter
from .product.views import router as product_router
from .suppliers.views import router as supplier_router
from .categorie.views import router as categorie_router
from .payment_methods.views import router as payment_methods_router
from .product_discount.views import router as product_discount_router
from .coupons.views import router as coupons_router
from .addresses.views import router as address_router
from .customers.views import router as customer_router
from .auth.views import router as auth_router
from .user.views import router as user_router
from .admin_user.views import router as admin_user_router
from .order.views import router as order_router
from .catalog.views import router as catalog_router


router = APIRouter()


router.include_router(product_router, prefix='/product', tags=['product']) # --> prefix adiciona o /product na rota @app.router('')
router.include_router(supplier_router, prefix='/supplier', tags=['supplier'])
router.include_router(categorie_router, prefix='/categorie', tags=['categorie'])
router.include_router(payment_methods_router, prefix='/payment_methods', tags=['payment_methods'])
router.include_router(product_discount_router, prefix='/product_discount', tags=['product_discount'])
router.include_router(coupons_router, prefix='/coupons', tags=['coupons'])
router.include_router(address_router, prefix='/address', tags=['address'])
router.include_router(customer_router, prefix='/customer', tags=['customer'])
router.include_router(auth_router, prefix='/auth', tags=['auth'])
router.include_router(user_router, prefix='/users', tags=['users'])
router.include_router(admin_user_router, prefix='/admin_users', tags=['admin_users'])
router.include_router(order_router, prefix='/order', tags=['order'])
router.include_router(catalog_router, prefix='/catalog', tags=['catalog'])