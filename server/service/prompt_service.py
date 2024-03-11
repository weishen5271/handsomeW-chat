
'''
   获取提示词
'''
def get_prompt(content,query):
    prompt = f"已知信息:\n{content}\n根据已知信息回答问题:\n{query}"
    return prompt