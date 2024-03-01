from fastapi import APIRouter

# create router
knowledge_router = APIRouter(
    prefix='/knowledge',
    tags = ['knowledge']
)



@knowledge_router.get('/') 
async def welcome() -> dict:
    return { "message": "Welcome to my Page"}


@knowledge_router.get('/import/file') 
async def import_file() -> dict:
    return { "message": "Welcome to my Page"}