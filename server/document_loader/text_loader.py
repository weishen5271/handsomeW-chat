from langchain.document_loaders.unstructured import UnstructuredFileLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
def get_docs(path):
    loader = TextLoader(path, encoding='utf-8')
    documents = loader.load()
    # 文档分割
    text_splitter = CharacterTextSplitter(chunk_size=256, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    return docs



