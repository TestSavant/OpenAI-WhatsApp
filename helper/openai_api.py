import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize the conversation history
conversation_history = [
    {'role': 'system', 'content': 'You are a helpful assistant bot named Zenko. You speak French first and English second. Always reply as Zenko'},
]

def chat_complition(prompt: str) -> dict:
    '''
    Call Openai API for text completion
    Parameters:
        - prompt: user query (str)
    Returns:
        - dict
    '''
    try:
        # Add the user's message to the conversation history
        conversation_history.append({'role': 'user', 'content': prompt})

        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=conversation_history  # Use the conversation history
        )

        # Add the model's response to the conversation history
        conversation_history.append({'role': 'assistant', 'content': response['choices'][0]['message']['content']})

        return {
            'status': 1,
            'response': response['choices'][0]['message']['content']
        }
    except:
        return {
            'status': 0,
            'response': 'openAI part didnt work'
        }
