from pydantic import BaseModel
from typing import Union, UUID


class Address(BaseModel):
    id: UUID
    address_type: Union[str]
    address_line_1: Union[str]
    address_line_2: Union[str]
    address_line_3: Union[str]
    postcode: Union[str]
    city: Union[str]
    state: Union[str]
    country: Union[str]
