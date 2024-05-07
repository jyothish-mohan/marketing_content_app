from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_content(topic, format):
    completion = client.chat.completions.create(
                response_format={ "type": "json_object" },
                model="gpt-3.5-turbo-1106",
                messages=[
                    {"role": "system", "content": """The user will give a topic and a format and you have to generate a marketing content for the topic in the given format. 
                     You can use emoji, fun words if needed. The content should be top notch. Return a json like this=>
                    `{'text': response}`
                    """},
                    {
                        "role":"user",
                        "content":f"topic: {topic}, format: {format}"
                    }
                ]
            )
    
    return completion.choices[0].message.content