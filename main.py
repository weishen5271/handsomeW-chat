from fastapi import FastAPI
import uvicorn
from server.router.knowledge import *
from concurrent.futures import ThreadPoolExecutor
import asyncio
from configs import (
    API_SERVER,
)

app = FastAPI()

# 创建线程池
threadpool = ThreadPoolExecutor(max_workers=200)

app.include_router(knowledge_router)

if __name__ == '__main__':

    uvicorn.run(app,host = API_SERVER.get("host"),port=API_SERVER.get("port"))
