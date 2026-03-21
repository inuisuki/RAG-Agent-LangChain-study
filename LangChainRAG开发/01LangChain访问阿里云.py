from langchain_community.llms.tongyi import Tongyi

model=Tongyi(model="qwen-max")

res=model.invoke(input="你是谁在做什么")

print(res)