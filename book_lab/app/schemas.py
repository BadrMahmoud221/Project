from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    author : str = Field(..., min_length=3, max_length=100)

class BookCreate(BookBase):
    pass 

class BookUpdate(BookBase):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    author : Optional[str] = Field(None, min_length=3, max_length=100)
    is_read : Optional[bool] = None

class BookResponse(BookBase):
    id : int 
    is_read : bool 

    class Config :
        from_attributes = True


