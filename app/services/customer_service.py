from fastapi.param_functions import Depends
from app.api.admin_user.schemas import ShowAdmin_UserSchemas
from app.repositories.customers_repository import CustomersRepository
from app.repositories.user_repository import UserRepository
from app.services.admin_user_services import Admin_userService
from app.api.customers.schemas import CustomerSchema
from app.models.models import Customers


class CustomerService :
    def __init__(self,customerRepository:CustomersRepository = Depends(),
                userRepository:UserRepository = Depends(),
                admin_userService: Admin_userService = Depends()):

        self.customerRepository = customerRepository
        self.userRepository = userRepository
        self.admin_userService = admin_userService

    def create_customer(self,customer:CustomerSchema):
        self.admin_userService.create_admin_user(customer.user_id)
        user_create = self.userRepository.find_by_email(customer.user_id.email)
        customer.user_id = user_create.id
        self.customerRepository.create(Customers(**customer.dict()))
