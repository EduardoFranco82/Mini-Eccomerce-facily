from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends
from starlette import status
from .schemas import UserSchema
import bcrypt
from app.services.admin_user_services import Admin_userService
from app.common.exceptions import Admin_userAlreadyExistsEmailException 

router = APIRouter()


@router.post('/')
def create(user: UserSchema, service: Admin_userService = Depends()):
   
    try:
         service.create_admin_user(user)
    except Admin_userAlreadyExistsEmailException as email_exists:
        raise HTTPException (status_code=status.HTTP_400_BAD_REQUEST, detail= email_exists.message )
