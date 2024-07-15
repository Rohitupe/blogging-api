from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from typing import Optional
import random

from routes.entry import entry_root
from routes.blog import blog_root

app = FastAPI()

app.include_router(entry_root) 
app.include_router(blog_root)