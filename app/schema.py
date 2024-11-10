import datetime
from typing import Literal, List, Optional
from pydantic import BaseModel


class BaseAdvertisement(BaseModel):
    title: str
    description: str
    price: float
    author: str


class CreateAdvertisementRequest(BaseAdvertisement):
    pass


class CreateAdvertisementResponse(BaseModel):
    id: int


class UpdateAdvertisementRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    author: Optional[str] = None


class GetAdvertisementResponse(BaseAdvertisement):
    id: int
    created_at: datetime.datetime


class SearchAdvertisementResponse(BaseModel):
    result: List[GetAdvertisementResponse]
