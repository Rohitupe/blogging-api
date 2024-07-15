from fastapi import APIRouter

entry_root = APIRouter()

# end point
@entry_root.get("/")
async def apiRunning():
    res = {
        "status":"ok",
        "message":"API is running"
    }
    return res