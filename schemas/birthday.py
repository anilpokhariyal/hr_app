from pydantic import BaseModel
from typing import Union, UUID
from datetime import datetime


class Birthday(BaseModel):
    id: UUID
    date: Union[datetime, None]
    type: Union[str]
