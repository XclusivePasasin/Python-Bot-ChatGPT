from utils.whatsapp import WhastApp as whatsapp_utils
from utils.chatgpt import ChatGPT as chatgpt_utils
from utils.document import Document as document_utils

class Bot:
    @staticmethod
    def manage_chatbot(text, number, id_message, name):
        text = text.lower()
        pdf = document_utils.get_pdf_for_catalog()
        response = chatgpt_utils.send_message_to_chatgpt(text, pdf)
        data = whatsapp_utils.payload_for_user(number, response)
        whatsapp_utils.send_message_to_whatsapp_user(data)
