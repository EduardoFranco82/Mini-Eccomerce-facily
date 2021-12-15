from fastapi import Depends
from app.common.exceptions import PaymentMethodDiscountAlreadyExistsException, PaymentMethodsNotAvailableException
from app.models.models import ProductDiscount
from app.repositories.payment_method_repository import PaymentMethodRepository
from app.repositories.product_discount_repository import ProductDiscountRepository
from app.api.product_discount.schemas import ProductDiscountSchema


class ProductDiscountService:
    def __init__(self, payment_method_repository: PaymentMethodRepository = Depends(),
                 product_discount_repository: ProductDiscountRepository = Depends()):
        self.payment_method_repository = payment_method_repository
        self.product_discount_repository = product_discount_repository

    def create_discount(self, discount: ProductDiscountSchema):
        payment_method = self.payment_method_repository.get_by_id(
            discount.payment_method_id)

        if not payment_method or not payment_method.enabled:
            raise PaymentMethodsNotAvailableException()

        find_payment_method_existence = self.product_discount_repository.filter(
            {'product_id': discount.product_id, 'payment_method_id': discount.payment_method_id})

        if find_payment_method_existence:
            raise PaymentMethodDiscountAlreadyExistsException()

        self.product_discount_repository.create(
            ProductDiscount(**discount.dict()))

