from openai import OpenAI

client=OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

examples_data = {
    "是":[
        ("公司ABC发布了季度财报,显示盈利增长","财报披露,公司ABC利润上升"),
    ],
    "不是":[
        ("黄金价格下跌,投资者抛售","外汇市场交易额创下新高"),
    ]
}

questions=[
    ("利率上升,影响房地产市场。","高利率对房地产有一定冲击。"),
    ("股票市场今日大涨,投资者乐观。","持续上涨的市场让投资者感到满意。"),
    ("油价大幅下跌,能源公司面临挑战。","未来智能城市的建设趋势愈发明显。")
]

messages=[
    {"role":"system","content":"你是一个文本匹配专家。你的任务是判断给定的两个句子是否有关联。"}
]
for key,value in examples_data.items():
    for t in value:
        messages.append({"role":"user","content":f"句子一:{t[0]},句子二:{t[1]}"})
        messages.append({"role":"system","content":key})

for q in questions:
    response=client.chat.completions.create(
        model="qwen3-max",
        messages=messages + [{"role": "user", "content": f"句子一:{q[0]},句子二:{q[1]}"}]
    )
    print(response.choices[0].message.content)