import os
from openai import OpenAI
 
client = OpenAI(api_key="YOUR_API_KEY")
 
response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages="This is a test",
        temperature=0,
        top_p=1,
        frequency_penalty=0,    
        presence_penalty=0
    )
 
print(response.choices[0].message.content)