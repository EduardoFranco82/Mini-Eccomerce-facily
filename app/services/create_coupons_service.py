from app.repositories.coupons_repository import CouponsRepository
from fastapi import Depends
from app.models.models import Coupons
from app.repositories.coupons_repository import CouponsRepository
from app.api.coupons.schemas import CouponsSchema
from app.common.exceptions import CouponCodeAlreadyExistsException


class CreateCouponsService:
    def __init__ (self, coupons_repository: CouponsRepository = Depends()):
        self.coupons_repository = coupons_repository


    def unique_coupon (self, coupon: CouponsSchema):
        find_unique_coupon   = self.coupons_repository.filter({'code':coupon.code})

        if find_unique_coupon:
            raise CouponCodeAlreadyExistsException

        return self.coupons_repository.create(Coupons(**coupon.dict()))