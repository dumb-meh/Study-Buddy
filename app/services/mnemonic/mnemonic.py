import os
import openai
from dotenv import load_dotenv
from .summary_schema import summary_request,summary_response

load_dotenv ()

class Summary:
    def __init__(self):
        self.client=openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def summary(self, input_data:str)->summary_response:
        prompt=self.create_prompt()
        data=input_data
        response=self.get_openai_response (prompt,data)
        return self.parse_response (response)
    
    def crreate_prompt (self)->str:
        return f""" You are helpful AI assistant """
    
    def get_openai_response (self, prompt:str, data:str)->str:
        completion =self.client.chat.completions.create(
            model="gpt-3.5-turbo"
            messages=[{"role":"system", "content": data},{"role":"user", "content": data}]
            temperature=0.7            
        )
        return completion.choices[0].message.content

