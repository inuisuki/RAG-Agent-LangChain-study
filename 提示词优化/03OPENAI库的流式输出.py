from openai import OpenAI
#获取用户对象
client =OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
#调用模型
responce=client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role":"system","content":"你是一个Python编程专家，并且话非常多"},
        {"role":"assistant","content":"好的，我是编程专家，并且话非常多，你要问什么？"},
        {"role":"user","content":"输出1-10的数字，使用Python代码"}
    ],
    stream=True
)
#处理结果
for chunk in responce:
    print(
        chunk.choices[0].delta.content,
        end=" ",
        flush=True
    )
