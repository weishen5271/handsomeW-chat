from transformers import AutoModelForCausalLM, BitsAndBytesConfig, AutoTokenizer,AutoModel


'''
    运行chatglm 问答测试代码
'''
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

# tokenizers = AutoTokenizer.from_pretrained("THUDM/chatglm-6b",trust_remote_code=True)
# model = AutoModel.from_pretrained("THUDM/chatglm-6b",trust_remote_code=True)

tokenizers = AutoTokenizer.from_pretrained("D:\huggingface\hub\models\chatglm3-6b",trust_remote_code=True)
# 采用4比特量化 什么是4比特量化
model = AutoModel.from_pretrained("D:\huggingface\hub\models\chatglm3-6b",trust_remote_code=True).quantize(4).half().cuda()

model = model.eval()

response,history = model.chat(tokenizers,"你好",history = [])
print(response)

response,history = model.chat(tokenizers,"晚上睡不着怎么办",history = history)
print(response)