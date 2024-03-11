import requests

def chat_http(prompt,history):
    resp = requests.post(
        url = "http://127.0.0.1:8000",
        json = {'prompt':prompt,"history":history},
        headers = {"Content-Type":"application/json;charset=utf-8"}
    )
    return resp.json()['response'],resp.json()['history']