import os
from dotenv import load_dotenv
from typing import Dict, List, Tuple, Optional
import json
from abc import ABC, abstractmethod
import re

from openai import OpenAI

load_dotenv()


def extract_bracketed_text(input_string):
    matches = re.findall(r'<(.*?)>', input_string)
    
    if matches:
        return matches
    else:
        print("No text found inside angle brackets.")
        return None


def get_user_message(text: str) -> List[Dict]:
    return [{
        "role": "user",
        "content": text
    }]


class BaseModel(ABC):
    @abstractmethod
    def complete(self, **kwargs):
        pass

class OpenRouterModel(BaseModel):
    def __init__(self, 
                 model: str = "qwen/qwen2.5-vl-3b-instruct:free",
                 api_key_name: str = "OPENROUTER_API_KEY"
                 ):

        self.model = model
        open_router_api_key = os.environ.get(api_key_name)
        self.client = OpenAI(base_url="https://openrouter.ai/api/v1",
                             api_key=open_router_api_key)
        self.temperature = 0
        

    def complete(self, user_messages: List):
        response = self.client.chat.completions.create(
            model= self.model,
            temperature=self.temperature,
            messages=user_messages,
        )

        if not response.id:
            print(f"Response blocked: {response}")
            return None, response

        response_message = response.choices[0].message
        return response_message.content, response
