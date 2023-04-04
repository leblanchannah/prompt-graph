from dotenv import load_dotenv
import os
import json
import openai

load_dotenv('../.env') 


openai.api_key = os.getenv('API_KEY')

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", # this is "ChatGPT" $0.002 per 1k tokens
  messages=[{"role": "user", "content": "Create a network graph with 5 nodes and 2 edges, formatted in json."}]
)

print(completion)

network_graph =  completion['choices'][0]['message']['content']
with open("network_graph.json", "w") as outfile:
    outfile.write(network_graph)
