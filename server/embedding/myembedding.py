from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from configs.server_config import EMBED_MODEL
class MyEmbedding():
    def __init__(self,name):
        self.name = name

    def get_embedding(self):
        embedding = HuggingFaceBgeEmbeddings(model_name=EMBED_MODEL[self.name])
        return embedding