from fastapi import APIRouter
from server.service import chat_service,prompt_service,vector_service
# create router
chat_router = APIRouter(
    prefix='/chat',
    tags = ['问答']
)

@chat_router.get('/chat')
async def chat(query: str):
    docs = vector_service.search(query)
    content = [docs[0].page_content]
    prompt = prompt_service.get_prompt(content, query)
    response,history = chat_service.chat_http(prompt, history=[])
    return response