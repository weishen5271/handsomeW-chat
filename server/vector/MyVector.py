from langchain_community.vectorstores import Milvus

class MyVector():

    def __init__(self,host,port):
        self.host = host
        self.port = port

    def store_milvus(self,doc,embedding,collection_name):
        db = Milvus.from_documents(
            doc,
            embedding=embedding,
            connection_args={"host": self.host, "port": self.port},
            collection_name=collection_name
        )
