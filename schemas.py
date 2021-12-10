from pydantic import BaseModel
from datetime import date
from enum import Enum
from typing import List


class Enums(str, Enum):
    fiction = 'fiction'
    science = 'science'
    drama = 'drama'


class Movie(BaseModel):
    name: str
    genre: Enums
    cast: List[str]
    pub_date: date
    duration_minutes: int
