from typing import Optional
from pydantic import BaseModel

class BlogModel(BaseModel):
    title : str
    sub_title : str
    content : str
    author : str
    tags : list
    rating : Optional[float] = None


class UpdateBlogModel(BaseModel):
    title : str = None
    sub_title : str = None
    content : str = None
    author : str = None
    tags : list = None
    rating : Optional[float] = None