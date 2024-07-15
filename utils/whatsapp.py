from config.config import Config
import requests


class WhastApp:
    
    def send_message_to_whatsapp_user(data):
        try:
            whatsapp_token = Config.whatsapp_token
            whatsapp_url = Config.whatsapp_url
            headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + whatsapp_token}
            print("Sending data:", data)  # Print data being sent
            response = requests.post(whatsapp_url, headers=headers, json=data)
            print("Response status:", response.status_code)  # Print response status
            print("Response text:", response.text)  # Print response text
            if response.status_code == 200:
                return 'Message sent successfully!', 200
            else:
                return 'Error sending message!', response.status_code
        except Exception as e:
            return str(e), 403
        
    def get_message_user(message):
        
        if 'type' not in message:
            return 'Message not recognized by the system.'
        
        type_message = message['type']
        if type_message == 'text':
            return message['text']['body']
        elif type_message == 'interactive' and 'button_reply' in message['interactive']:
            return message['interactive']['button_reply']['id']
        elif type_message == 'reaction':
            return message['reaction']['message_id']
        elif type_message == 'interactive' and 'list_reply' in message['interactive']:
            return message['interactive']['list_reply']['id']
        else:
            return 'Message type not supported.'
        
    def payload_for_user(number, response):
        data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": response
            }
        }
        return data