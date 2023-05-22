import openai
from dotenv import dotenv_values
config = dotenv_values(".env")

openai.api_key = config["API_KEY"]

# Completion format
# response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt="5 most populated cities in the world, in order: ",
#     max_tokens=100
# )

# Chat format
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "generate a trivia question and answer"}
    ],
    temperature=1,  # Default is 1
    max_tokens=200  # Default is infinite in chat format
)

print(response.choices[0].message.content)
