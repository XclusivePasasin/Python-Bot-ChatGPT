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
    

#Te mando comentado esto, para ver si te funciona mejor esto o el que tenias vos
# def enviar_a_chatgpt(mensaje, modelo="gpt-3.5-turbo", api_key="TU_API_KEY"):
#     openai.api_key = api_key
#     respuesta = openai.ChatCompletion.create(
#         model=modelo,
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": mensaje}
#         ],
#         max_tokens=150  # Ajusta según tus necesidades
#     )
#     return respuesta.choices[0].message['content']

# # Ejemplo de uso
# respuesta_chatgpt = enviar_a_chatgpt(mensaje_final, api_key=api_key)
# print(respuesta_chatgpt)   