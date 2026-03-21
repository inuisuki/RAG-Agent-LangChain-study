from openai import OpenAI
#获取用户对象
client =OpenAI(
    api_key="sk-8d65a650bc2242588c56f85c2bb97bcb",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
#调用模型
responce=client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role":"system","content":"你是一个Python编程专家，并且不说废话简单回答"},
        {"role":"assistant","content":"好的，我是编程专家，并且话不多，你要问什么？"},
        {"role":"user","content":"输出1-10的数字，使用Python代码"}
    ]
)
#处理结果
print(responce.choices[0].message.content)

