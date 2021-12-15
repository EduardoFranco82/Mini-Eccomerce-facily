from .base_repository import BaseRepository
from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.db import get_db
from app.models.models import Addresses

class AddressesRepository (BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Addresses)


    def is_primary(self, customer_id, primary):
        return (
            self.session.query(self.model)
            .filter_by(customer_id=customer_id, primary=primary)
            .first()
        )