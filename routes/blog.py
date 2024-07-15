from fastapi import APIRouter, status
from models.blog import BlogModel
from config.config import blog_collections
from serializers.blog import DecodeBlogs, DecodeBlog
from bson import ObjectId
import datetime

blog_app = APIRouter()

# post request create blog
@blog_app.post("/blogs", status_code=status.HTTP_201_CREATED)
async def create_post(post : BlogModel):
    payload = post.model_dump()
    current_date = datetime.date.today()
    payload['date_created'] = str(current_date)
    
    res = blog_collections.insert_one(payload)
    doc_id = str(res.inserted_id)
    return {
        "status":"ok",
        "message":"blog successfully created",
        "_id" : doc_id
    }


# get request get all blogs
@blog_app.get("/blogs", status_code=status.HTTP_200_OK)
async def get_posts():
    res = blog_collections.find()
    decoded_data = DecodeBlogs(res)
    return {
        "status":"ok",
        "data":decoded_data
    }


# get request get single blogs
@blog_app.get("/blogs/{id}", status_code=status.HTTP_200_OK)
async def get_post(id:str):
    res = blog_collections.find_one({"_id" : ObjectId(id)})
    decoded_data = DecodeBlog(res)
    return {
        "status":"ok",
        "data":decoded_data
    }