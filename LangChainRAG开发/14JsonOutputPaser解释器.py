from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser

str_parser=StrOutputParser()
json_parser=JsonOutputParser()

model=ChatTongyi(model="qwen-max")

first_prompt=PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}孩，请起名，并以Json格式返回"
    "要求key是name，value时起的名字，请严格遵循"
)

second_prompt=PromptTemplate.from_template(
    "姓名:{name}，帮我看下含义"
)

chain=first_prompt | model | json_parser | second_prompt | model | str_parser
res=chain.invoke({"lastname":"王","gender":"女"})
print(res)