from langchain_community.document_loaders import PyPDFLoader

def get_docs(path):
    loader = PyPDFLoader(path)
    docs = loader.load()
    print('pdf:\n', docs[0].page_content[:100])
    return docs

# def get_docs_file(file):
#     loader = PyPDFLoader(file)
#     docs = loader.load()
#     print('pdf:\n', docs[0].page_content[:100])
#     return docs