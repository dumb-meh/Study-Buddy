import os
import json
import openai
from dotenv import load_dotenv
from .mnemonic_schema import mnemonic_response

load_dotenv ()

class Mnemonic:
    def __init__(self):
        self.client=openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def get_mnemonic(self, input_data:str)->mnemonic_response:
        prompt=self.create_prompt()
        data=input_data
        response=self.get_openai_response (prompt,data)
        return response
    
    def create_prompt (self)->str:
        return f""" Your job is to Summarize the text you are given"""
    
    def get_openai_response (self, prompt:str, data:str)->str:
        completion =self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"system", "content": prompt},{"role":"user", "content": data}],
            temperature=0.7            
        )
        return completion.choices[0].message.content
    
