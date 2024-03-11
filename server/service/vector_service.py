from fastapi import UploadFile
import mimetypes
from server.document_loader import pdf_loader,text_loader
from server.vector import  MyVector
from server.embedding.myembedding import  MyEmbedding
'''
    保存文件内容到向量库中
'''
test_collection_name = "test"
def save_vector(file_path,mime_type):
     print(file_path)
     if 'text/plain' in mime_type:
        docs = text_loader.get_docs(file_path)
     elif 'csv' in mime_type:
        pass
     elif 'pdf' in mime_type:
        docs = pdf_loader.get_docs(file_path)
     elif 'ms-excel' in mime_type or 'sheet' in mime_type:
        print(mime_type, flush=True)

     if (docs):
        myvector = MyVector()
        embedding = MyEmbedding('bge-large-zh-v1.5')
        db = myvector.store_milvus(docs,embedding.get_embedding(),"test1")
     else:
        return "传入的文件内容为空，或者格式不支持"
