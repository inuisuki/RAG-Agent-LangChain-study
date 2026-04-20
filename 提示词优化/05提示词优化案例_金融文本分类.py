from openai import OpenAI

# 获取client对象，调用OpenAI
client=OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 示例数据
example_data={
    '新闻报告':'今天股市震荡，收到宏观经济数据和全球贸易紧张局势的影响',
    '财务报告':'本公司财务报告显示，本公司实现稳步增长的盈利',
    '公司报告':'本公司高兴的宣布，成功完成最新一轮交易',
    '分析师报告':'最新的行业分析报告指出，科技公司的创新成为未来经济增长的主要动力'
}

# 提问数据
questions=[
    "今日央行公司宣布降低利率，以刺激经济增长",
    "ABC公司发布公告称，已经完成对XYZ公司的收购",
    "公司资产负债显示，公司偿还债务能力强劲",
    "最新的分析报告指出，可再生能源行业预计在未来提供坚实的财务基础",
    "小明喜欢小新鸭"
]

messages=[
    {"role":"system","content":"你是一个金融专家，将文本分类为[新闻报告,财务报告,公司报告,分析师报告]，不清楚的分类为不清楚类别"}
]

for key,value in example_data.items():
    messages.append({"role":"user","content":value})
    messages.append({"role":"assistant","content":key})

for q in questions:
    temp_messages = messages.copy()  # 创建副本
    temp_messages.append({"role":"user","content":f"按照示例规范回答文本{q}"})
    response=client.chat.completions.create(
        model="qwen3-max",
        messages=temp_messages
    )
    print(response.choices[0].message.content)