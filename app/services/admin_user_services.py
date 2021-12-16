from app.api.customers.schemas import UserSchema
from app.common.exceptions import Admin_userAlreadyExistsEmailException
from app.repositories.user_repository import UserRepository
from app.api.admin_user.schemas import Admin_UserSchemas
from fastapi import Depends, HTTPException, status
from app.common.exceptions import Admin_userAlreadyExistsEmailException
from app.models.models import User
import bcrypt


class User_dto:
    def __init__(self, display_name, email, password) :
        self.display_name = display_name
        self.email = email
        self.password = password

    def dict(self):
        return {'display_name' : self.display_name, 'email': self.email, 'password' : self.password}


class Admin_userService:
    def __init__(self,userRepository:UserRepository = Depends()):
        self.userRepository = userRepository

    def is_valid_email(self,id,email):
        if id != None :
            same_email = self.userRepository.get_by_id(id)
            if same_email.email == email:
                return True
        if not self.userRepository.find_by_email(email):
            return True
        raise Admin_userAlreadyExistsEmailException()
        
    def generate_password(self,password):
        return bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())

    def create_admin_user(self,user:User_dto):
        if self.is_valid_email(None,user.email):
            user.password = self.generate_password(user.password)
            userdata = user.dict()
            userdata.update({'role': 'admin'})
            return self.userRepository.create(User(**userdata))

    
    def create_customer_user(self, user: User_dto):
        if self.is_valid_email(None, user.email ):
            user.password = self.generate_password(user.password)
            userdata = user.dict()
            userdata.update({'role': 'costumer'})
            return self.userRepository.create(User(**userdata))

    def update_admin_user(self,id,admin_user:Admin_UserSchemas):
        if self.is_valid_email(id,admin_user.email):
            admin_user.password = self.generate_password(admin_user.password)
            return self.userRepository.update(id,admin_user.dict())