from langchain.document_loaders.unstructured import UnstructuredFileLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
class MyTextLoader(UnstructuredFileLoader):
    def __init__(self,path):
        self.path = path
    def get_docs(self):
        loader = TextLoader(self.path, encoding='utf-8')
        documents = loader.load()
        # 文档分割
        text_splitter = CharacterTextSplitter(chunk_size=256, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)
        return docs


