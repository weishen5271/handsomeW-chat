from transformers import AutoModelForCausalLM, BitsAndBytesConfig, AutoTokenizer
from server.document_loader.text_loader import  MyTextLoader
from server.embedding.myembedding import MyEmbedding
from server.vector.MyVector import MyVector
from langchain.chains import RetrievalQA


import torch
host = "127.0.0.1"
port = 19530

MODEL_NAME = ''

def fun(docs):
    # 设置一个嵌入模型，将文档块转换为向量嵌入。
    EMBEDDING_MODEL = "bge-large-zh-v1.5"
    # 加载embedding模型
    myEmBedding = MyEmbedding(EMBEDDING_MODEL)
    print(myEmBedding.get_embedding())
    # 存储到向量数据库中
    myvector = MyVector(host,port)
    print(myvector.store_milvus(docs,myEmBedding.get_embedding(),"test1"))
    # print(embeddings)
    # 设置用于保存矢量嵌入的矢量存储。这里我们使用Milvus作为向量存储。

def chat():
    pass






if __name__ == '__main__':
    # 加载document
    doc = MyTextLoader("text.txt")
    print(doc.get_docs())
    # 转换成向量
    fun(doc.get_docs())
