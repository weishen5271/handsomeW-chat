import requests

def chat_http(prompt,history):
    resp = requests.post(
        url = "http://127.0.0.1:8000",
        json = {'prompt':prompt,"history":history},
        headers = {"Content-Type":"application/json;charset=utf-8"}
    )
    return resp.json()['response'],resp.json()['history']

def chat_with_online_chatglm(prompt,history,model_name:str="glm-3-turbo"):
    from zhipuai import ZhipuAI
    client = ZhipuAI(api_key="")  # 填写您自己的APIKey
    messages = []
    if (history is not None and type(history) is list):
        messages.update(history)
    messages.append(prompt)
    messages.append( {
                "content": "好的，我来讲一个轻松的笑话给您听。\n\n一天，小明迟到了，老师问他：“你为什么迟到？”\n小明回答说：“老师，我今天看到一块牌子上写着‘学校慢行’，所以我就慢慢地走来了。”",
                "role": "assistant"
            })
    response = client.chat.completions.create(
        model=model_name,  # 填写需要调用的模型名称
        messages=messages,
    )
    return  response
