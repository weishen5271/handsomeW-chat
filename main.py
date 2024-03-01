from fastapi import FastAPI

from server.router.knowledge import *

app = FastAPI()

app.include_router(knowledge_router)

