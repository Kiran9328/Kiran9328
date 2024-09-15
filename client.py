from openai import OpenAI

client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google"},
        {
            "role": "user",
            "content": "What is coding."
        }
    ]
)

print(completion.choices[0].message.content)