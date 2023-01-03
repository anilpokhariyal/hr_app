from pydantic import BaseModel
from typing import Union, UUID


class Contact(BaseModel):
    id: UUID
    name: Union[str]
    number: Union[str]
    relation: Union[str]
