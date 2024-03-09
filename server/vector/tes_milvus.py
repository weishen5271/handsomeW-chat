from langchain.embeddings.cohere import CohereEmbeddings
from langchain_community.vectorstores import Milvus
from langchain_community.embeddings.openai import OpenAIEmbeddings
from transformers import AutoModelForCausalLM, BitsAndBytesConfig, AutoTokenizer

from server.document_loader.text_loader import  MyTextLoader
from langchain.embeddings import HuggingFaceBgeEmbeddings
import torch
host = "127.0.0.1"
port = 19530

MODEL_NAME = ''

embed_model = {
    "ernie-tiny": "nghuyong/ernie-3.0-nano-zh",
    "ernie-base": "nghuyong/ernie-3.0-base-zh",
    "text2vec-base": "shibing624/text2vec-base-chinese",
    "text2vec": "GanymedeNil/text2vec-large-chinese",
    "text2vec-paraphrase": "shibing624/text2vec-base-chinese-paraphrase",
    "text2vec-sentence": "shibing624/text2vec-base-chinese-sentence",
    "text2vec-multilingual": "shibing624/text2vec-base-multilingual",
    "text2vec-bge-large-chinese": "shibing624/text2vec-bge-large-chinese",
    "m3e-small": "moka-ai/m3e-small",
    "m3e-base": "moka-ai/m3e-base",
    "m3e-large": "moka-ai/m3e-large",

    "bge-small-zh": "BAAI/bge-small-zh",
    "bge-base-zh": "BAAI/bge-base-zh",
    "bge-large-zh": "BAAI/bge-large-zh",
    "bge-large-zh-noinstruct": "BAAI/bge-large-zh-noinstruct",
    "bge-base-zh-v1.5": "BAAI/bge-base-zh-v1.5",
    "bge-large-zh-v1.5": "BAAI/bge-large-zh-v1.5",

    "bge-m3": "BAAI/bge-m3",

    "piccolo-base-zh": "sensenova/piccolo-base-zh",
    "piccolo-large-zh": "sensenova/piccolo-large-zh",
    "nlp_gte_sentence-embedding_chinese-large": "damo/nlp_gte_sentence-embedding_chinese-large",
    "text-embedding-ada-002": "your OPENAI_API_KEY",
}



def fun(docs):
    # 设置一个嵌入模型，将文档块转换为向量嵌入。
    EMBEDDING_MODEL = "bge-large-zh-v1.5"
    embeddings = HuggingFaceBgeEmbeddings(model_name=embed_model['bge-base-zh-v1.5'])
    print(embeddings)
    Milvus.from_documents(
        docs,
        embedding=embeddings,
        connection_args={"host": host, "port": port}
    )
    # print(embeddings)
    # 设置用于保存矢量嵌入的矢量存储。这里我们使用Milvus作为向量存储。

def load_embediing_mode(model_name="ernie-tiny"):
    embeddings = HuggingFaceBgeEmbeddings(model_name="ernie-tiny")


# def create_model_and_tokenizer():
#     bnb_config = BitsAndBytesConfig(
#         load_in_4bit=True,
#         bnb_4bit_quant_type="nf4",
#         bnb_4bit_compute_dtype=torch.float16,
#     )
#
#     model = AutoModelForCausalLM.from_pretrained(
#         MODEL_NAME,
#         use_safetensors=True,
#         quantization_config=bnb_config,
#         trust_remote_code=True,
#         device_map="auto",
#     )
#
#     tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
#     tokenizer.pad_token = tokenizer.eos_token
#     tokenizer.padding_side = "right"
#
#     return model, tokenizer




if __name__ == '__main__':
    # 加载document
    doc = MyTextLoader("text.txt")
    print(doc.get_docs())
    # 转换成向量
    fun(doc.get_docs())
