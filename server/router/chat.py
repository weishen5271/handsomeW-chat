from fastapi import APIRouter

# create router
knowledge_router = APIRouter(
    prefix='/chat',
    tags = ['chat']
)