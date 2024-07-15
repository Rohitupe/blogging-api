from fastapi import APIRouter, status
from models.blog import BlogModel
from config.config import blogs_collection
import datetime

blog_root = APIRouter()

# post request
@blog_root.post("/blogs", status_code=status.HTTP_201_CREATED)
async def create_post(post : BlogModel):
    payload = post.model_dump()
    current_date = datetime.date.today()
    payload['date_created'] = str(current_date)
    
    res = blogs_collection.insert_one(payload)
    doc_id = str(res.inserted_id)
    return {
        "status":"ok",
        "message":"blog posted successfully",
        "_id" : doc_id
    }
    