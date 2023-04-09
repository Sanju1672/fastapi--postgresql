from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class BookSchema(BaseModel):
    id: Optional[int]=None
    title: Optional[string]=None
    author: Optional[string]=None
    publishedyear: Optional[int]=None

    class Config:
        orm.mode = True

 class RequestBook(BaseModel):
    parameter: = BookSchema = Field(...)

 class Response (GenericModel,Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
    