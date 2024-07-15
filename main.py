from fastapi import FastAPI

from routes.blog import blog_app

app = FastAPI()

app.include_router(blog_app)