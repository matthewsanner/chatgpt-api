import openai
from dotenv import dotenv_values
config = dotenv_values(".env")

openai.api_key = config["API_KEY"]

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="5 most populated cities in the world, in order: ",
    max_tokens=100
)

print(response.choices[0].text)
