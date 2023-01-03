from pydantic import BaseModel, EmailStr
from typing import Union, UUID, List
from contact import Contact
from address import Address
from birthday import Birthday
from user_email import Email
from datetime import date


class User(BaseModel):
    id: UUID
    internal_id: Union[str]
    first_name: str
    last_name: str
    contact: List[Contact]
    address: List[Address]
    dob: List[Birthday]
    dobj: Union[date]
    email: List[Email]
    status: Union[bool]
