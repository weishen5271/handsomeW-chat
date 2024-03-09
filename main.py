from fastapi import FastAPI
import uvicorn
from server.router.knowledge import *
from concurrent.futures import ThreadPoolExecutor
import asyncio


app = FastAPI()

# 创建线程池
threadpool = ThreadPoolExecutor(max_workers=200)

app.include_router(knowledge_router)

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8000
    uvicorn.run(app,host = host,port=port)
