from pydantic import BaseModel, EmailStr
from typing import Union, UUID


class Email(BaseModel):
    id: UUID
    title: Union[str]
    email: EmailStr
    varification_code: Union[str]
    status: Union[bool]

