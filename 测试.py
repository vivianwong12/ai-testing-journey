from openai import OpenAI

client = OpenAI(
    api_key="sk-cp-XP6VmHYmZc-Hay7ZgxVf23HMqUtOSZa2iIKEunUc-GYh-JtStx6e5KxcIqh10qxJ6KH-ozE67Q2dIR1Eg0YimFpeHVGvrHzG_3H7l5-jctcyf1ikfdtVPsA",
    base_url="https://api.minimax.cn/v1"
)

response = client.chat.completions.create(
    model="MiniMax-M3",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hi, how are you?"},
    ],
    # 设置 reasoning_split=True 将思考内容分离到 reasoning_details 字段
    extra_body={"reasoning_split": True},
)

print(f"Thinking:\n{response.choices[0].message.reasoning_details[0]['text']}\n")
print(f"Text:\n{response.choices[0].message.content}\n")