from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv('API_KEY')

query = "what is machine learning"

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = API_KEY
)

completion = client.chat.completions.create(
  model="nvidia/nemotron-4-340b-instruct",
  messages=[{"role":"user","content":query}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
  stream=True
)

response=""
for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")
    response+=chunk.choices[0].delta.content



client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = API_KEY
)

completion = client.chat.completions.create(
  model="nvidia/nemotron-4-340b-reward",
  messages=[{"role":"user","content":query},{"role":"assistant","content":response}],
)
print(completion)