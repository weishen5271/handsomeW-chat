from langchain.chains import RetrievalQA

from langchain_community.llms import ChatGLM

from server.document_loader import text_loader,pdf_loader
from server.embedding.myembedding import MyEmbedding
from server.vector.MyVector import MyVector
import requests
host = "127.0.0.1"
port = 19530

'''
    提取文件并做本地知识库问答
'''

def chat(prompt,history):
    resp = requests.post(
        url = "http://127.0.0.1:8000",
        json = {'prompt':prompt,"history":history},
        headers = {"Content-Type":"application/json;charset=utf-8"}
    )
    return resp.json()['response'],resp.json()['history']


endpoint_url = "http://127.0.0.1:8000";
llm = ChatGLM(
    endpoint_url=endpoint_url,
    max_token = 80000,
    top_p = 0.9
)
myvector = MyVector(host,port)
EMBEDDING_MODEL = "bge-large-zh-v1.5"
myEmBedding = MyEmbedding(EMBEDDING_MODEL)
doc = text_loader.get_docs("../server/vector/text.txt")
#db = myvector.store_milvus(doc.get_docs(),myEmBedding.get_embedding(),"test1")
db = myvector.get_milvus(myEmBedding.get_embedding(),"test1")
retriever = db.as_retriever()
'''
    文档放在哪？
'''
# qa = RetrievalQA.from_chain_type(
#     llm = llm,
#     chain_type='stuff',
#     retriever = retriever
# )
# response = qa.run("孙悟空")
# print(response)

# 从向量库中提取
query = "猪八戒是谁"
docs = db.similarity_search(query)
content = [docs[0].page_content]
prompt = f"已知信息:\n{content}\n根据已知信息回答问题:\n{query}"
print(prompt)
response,history = chat(prompt,[])
print(response)
