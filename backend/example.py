from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

completion = client.chat.completions.create(
  extra_body={},
  model="deepseek/deepseek-r1-0528-qwen3-8b:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)