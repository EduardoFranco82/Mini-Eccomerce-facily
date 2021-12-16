from fastapi.param_functions import Depends
from app.api.admin_user.schemas import ShowAdmin_UserSchemas
from app.repositories.customers_repository import CustomersRepository
from app.repositories.user_repository import UserRepository
from app.services.admin_user_services import Admin_userService, User_dto
from app.api.customers.schemas import CustomerSchema, UpdateCustomersSchema
from app.models.models import Customers


class CustomerService :
    def __init__(self,customerRepository:CustomersRepository = Depends(),
                userRepository:UserRepository = Depends(),
                admin_userService: Admin_userService = Depends()):

        self.customerRepository = customerRepository
        self.userRepository = userRepository
        self.admin_userService = admin_userService

    def create_customer(self,customer:CustomerSchema):
        user_create = self.admin_userService.create_customer_user (User_dto(**customer.user.dict()))
        customer_data = customer.dict()
        customer_data.pop('user')
        customer_data.update({'user_id': user_create.id})
      #  user_create = self.userRepository.find_by_email(customer.user_id.email)
      #  customer.user_id = user_create.id
        return self.customerRepository.create(Customers(**customer_data))


    def update_customer(self, customer: UpdateCustomersSchema, id):
          customer_data = customer.dict()
          user_data = customer_data.pop('user')
          customer_model = self.customerRepository.update(id, customer_data)
          self.userRepository.update(user_data['id'], user_data)
          return customer_model