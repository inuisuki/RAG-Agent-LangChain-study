from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnableLambda

Parser=StrOutputParser()
my_func=RunnableLambda(lambda ai_msg:{"name":ai_msg.content})
first_prompt=PromptTemplate.from_template(
    "我生了孩子，我姓{lastname}，孩子是{gender}孩，现在帮我起名，仅给我名字"
)
second_prompt=PromptTemplate.from_template(
    "姓名:{name}，帮我解析名字含义"
)
model=ChatTongyi(model="qwen3-max")
chain=first_prompt | model | my_func | second_prompt | model | Parser
for chunk in chain.stream({"lastname":"王","gender":"男"}):
    print(chunk,end="",flush=True)


