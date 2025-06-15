import re
from typing import List, Dict

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