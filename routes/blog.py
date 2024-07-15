from fastapi import APIRouter, status, Response
from models.blog import BlogModel, UpdateBlogModel
from config.config import blog_collections, blog_collections_users_details
from serializers.blog import DecodeBlogs, DecodeBlog
from bson import ObjectId
import datetime

blog_app = APIRouter()


# home
@blog_app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"message":"Navigate to docs to explore api - http://URL/docs "}


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
        "_id":doc_id
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


# get request get single blog
@blog_app.get("/blogs/{id}", status_code=status.HTTP_200_OK)
async def get_post(id:str):
    res = blog_collections.find_one({"_id" : ObjectId(id)})
    decoded_data = DecodeBlog(res)
    return {
        "status":"ok",
        "data":decoded_data
    }


# patch request to update single blog
@blog_app.patch("/blogs/{id}",status_code=status.HTTP_200_OK)
async def update_post(id:str, payload :UpdateBlogModel):
    req = payload.model_dump(exclude_unset=True)
    blog_collections.find_one_and_update({"_id":ObjectId(id)}, {"$set" : req})

    return {
        "status":"ok",
        "message":"blog updated successfully"
    }


# delete request to delete a blog
@blog_app.delete("/blogs/{id}",status_code=status.HTTP_200_OK)
async def delete_post(id:str):
    blog_collections.find_one_and_delete({"_id":ObjectId(id)})
    return {
        "status":"ok",
        "message":"blog deleted successfully"
    }
