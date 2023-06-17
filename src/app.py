from flask import Flask, request, jsonify

from helper.openai_api import chat_complition
from helper.twilio_api import send_message

app = Flask(__name__)

#Basic entrypoint. usefull to test the connection to the API
@app.route('/')
def home():
    return jsonify(
        {
            'status': 'OK',
            'wehook_url_example': 'BASEURL/twilio/',
            'message': 'Zenko AI webhooks are ready for work',
            
        }
    )

#main Twilio endpoint. Use: https://BASE_URL/twilio  Used by WhatsApp to create a communication line with GPT 
@app.route('/twilio', methods=['POST'])
def receiveMessage():
    try:
        # Extract incoming parameters from Twilio
        message = request.form['Body']
        sender_id = request.form['From']

        # Get response from Openai
        result = chat_complition(message)
        if result['status'] == 1:
            send_message(sender_id, result['response'])
    except:
        pass
    return 'OK', 200


# Additional API methods can be loaded here. As an example.. 

    
# @app.route('/image', methods=['POST'])
# def receiveMessage():
#     try:
#         # Extract incomng parameters from GPT Image generator
#         message = request.form['Body']
#         sender_id = request.form['From']

#         # Get response from Openai
#         result = image(query)
#         if result['status'] == 1:
#             send_message(sender_id, result['response'])
#     except:
#         pass
#     return 'OK', 200
