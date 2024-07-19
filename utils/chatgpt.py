from openai import OpenAI
from config.config import Config
from utils.database import DataBase as database_utils
from utils.document import Document as document_utils
from utils.langchain import Langchain 
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

class ChatGPT:
  
    @staticmethod
    def send_message_to_chatgpt(user_message, file):
        try:
            # Variables
            openai_api_key = Config.key  # o usar OPENAI_API_KEY si estás utilizando variables de entorno
            client = OpenAI(api_key=openai_api_key)
            lang = Langchain()
            
            # Obtener la información relevante del archivo de texto usando LangChain
            information = lang.get_response_from_langchain(file, user_message)
            
            # Preparar los documentos de entrada para ChatGPT
            docs = [{"text": doc['content']} for doc in information]  # Ajustar 'content' según la estructura actual
            
            # Crear la cadena de preguntas y respuestas
            llm = ChatOpenAI(model_name='gpt-3.5-turbo', openai_api_key=openai_api_key)
            chain = load_qa_chain(llm, chain_type="stuff")
            
            # Personalizar el prompt con el rol de asistente de belleza y cuidado personal
            prompt = (
                "You are an assistant for a beauty, cosmetics, and personal care store. "
                "You provide information about various beauty products, help customers with their inquiries, "
                "and offer recommendations based on their needs. Your responses should be friendly, helpful, "
                "and knowledgeable, and you are developed by Clobi Technologies.\n\n"
                f"User's question: {user_message}\n\n"
                "Relevant documents:\n"
            )
            prompt += "\n".join([f"{doc['text']}" for doc in docs])
            
            # Obtener la respuesta usando LangChain
            response = chain.run(input_documents=docs, question=prompt)
            
            return response
        except Exception as e:
            print(f"\n Ups!, An error has occurred: {e} \n")
            return 'Ups!, An error has occurred'