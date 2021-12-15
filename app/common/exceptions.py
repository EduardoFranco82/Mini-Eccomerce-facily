class PaymentMethodsNotAvailableException(Exception):
    def __init__(self):
        self.message = 'This payment method is not available'
        super().__init__(self.message)


class PaymentMethodDiscountAlreadyExistsException(Exception):
    def __init__(self):
        self.message = 'Already exists a discount with this payment method'
        super().__init__(self.message)

class CouponCodeAlreadyExistsException(Exception):
    def __init__(self):
        self.message = 'Already exists a coupon code'
        super().__init__(self.message)


class PrimaryAddressAlreadyExistsException(Exception):
    def __init__(self):
        self.message = 'Already exists a primary address'
        super().__init__(self.message)


class Admin_userAlreadyExistsEmailException(Exception):
    def __init__(self):
        self.message = 'This email is already being used'
        super().__init__(self.message)