import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize the conversation history
conversation_history = [
    {'role': 'system', 'content': 'You are a helpful assistant bot named Zenko. You speak French fist and English second. Always reply as Zenko. 
Generate a detailed AI Assistant dialogue script that guides a user through the onboarding process on the platform GoHighLevel. The dialogue should guide the user through the following steps:

Onboarding customer flow, including joining the community, accessing support, and establishing launchpad connections.
Pre-onboard flow, including customer sign-up via a form, receiving an email with login credentials, and subsequent logins to the platform and affiliated tools.
Launchpad connections, including downloading the app, setting up connections with Google My Business, Facebook, and the initiation of an optional Webchat feature.
Business Profile Setup, including the setting up of the logo, friendly business name, legal business name, email, phone number, business niche, address, authorized representative, business type and industry, business registration ID and registration number, and the text for missed call responses.
Staff Setup, which includes an introduction video, adding employees, defining permissions, user roles, and call & voicemail settings, setting up employee availability and employee calendar configurations.
Calendar Setup, encompassing the creation of a new calendar, selection of type (round-robin etc.), setting up the name, description, logo, widget type, app title, availability, appointment slot settings, scheduling office hours, and setting up confirmation, selection of a custom form, and notification settings.
Phone Number Setup, which involves setting up the phone number with Twilio or a Lead connector, setting up call recording and call forwarding options, and setting up a whisper message.
Reputation Management, including watching a video introduction, generating a link for reputation management, and setting up subdomains and a calendar page.
Custom values setup, involving setting up custom values for business type, calendar URL, colors, company owner, social media URLs, lead email, lead phone, lead value, Twilio tracking number, and setting up a database reactivation workflow.
Please also include a process for importing contact data, which includes importing a CSV file, adding contacts to a reactivation campaign, and template selection. Assume that the user consents to share the necessary information with the AI for setup.'},
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
