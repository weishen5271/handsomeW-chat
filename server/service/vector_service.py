from fastapi import UploadFile
import mimetypes
from server.document_loader import *
from server.vector import  MyVector
from server.embedding.myembedding import  MyEmbedding
from langchain.document_loaders.unstructured import UnstructuredFileLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

'''
    保存文件内容到向量库中
'''
test_collection_name = "test"
def save_vector(file_path,mime_type):
     print(file_path)
     loader = None
     if 'text/plain' in mime_type:
        loader = TextLoader(file_path=file_path)
     elif 'csv' in mime_type:
        pass
     elif 'pdf' in mime_type:
        loader = RapidOCRPDFLoader(file_path=file_path)
     elif 'ms-excel' in mime_type or 'sheet' in mime_type:
        print(mime_type, flush=True)

     if (loader):
         documents = loader.load()
         text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
         docs = text_splitter.split_documents(documents)
     if (docs):
         print(docs)
         myvector = MyVector()
         embedding = MyEmbedding('bge-large-zh-v1.5')
         db = myvector.store_milvus(docs,embedding.get_embedding(),"test1")
     else:
        return "传入的文件内容为空，或者格式不支持"
def search(query: str):
    myvector = MyVector()
    embedding = MyEmbedding('bge-large-zh-v1.5')
    db = myvector.get_milvus(embedding.get_embedding(), "test1")
    docs = db.similarity_search(query)
    return docs



