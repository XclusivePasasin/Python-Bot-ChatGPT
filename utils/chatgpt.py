from openai import OpenAI
from config.config import Config
from utils.database import DataBase as database_util
from utils.document import PDF


class ChatGPT:
  
  @staticmethod
  def send_message_to_chatgpt(message):
    try:
      # pdf_generator = PDF()
      # catalog_path = pdf_generator.create_pdf()
      # # Manejar texto antes de enviarlo
      # safe_message = message.encode('utf-8', 'ignore').decode('latin-1')  # Ejemplo de manejo de codificación
      client = OpenAI(api_key=Config.key)
      completion = client.chat.completions.create(
        model= Config.model,
        messages=[
          {"role": "system", "content": f"You are an assistant for a technology products store. You provide information about various tech products, help customers with their inquiries, and offer recommendations based on their needs. Your responses should be friendly, helpful and knowledgeable, and you are developed by Clobi Technologies."},
          {"role": "user", "content": message}
        ]
      )
      return completion.choices[0].message.content
    except Exception as e:
      print(f"Ups!, An error has occurred: {e}")
      return print('Ups!, An error has occurred ')
    