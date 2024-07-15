from utils.whatsapp import WhastApp as whatsapp_utils
from utils.chatgpt import ChatGPT as chatgpt_utils

class Bot:
    @staticmethod
    def manage_chatbot(text, number, id_message, name):
        text = text.lower()
        # Aquí llamamos a ChatGPT para obtener la respuesta
        response = chatgpt_utils.send_message_to_chatgpt(text)
        data = whatsapp_utils.payload_for_user(number, response)
        # Enviar la respuesta al usuario
        whatsapp_utils.send_message_to_whatsapp_user(data)
