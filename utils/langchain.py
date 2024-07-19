import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings 
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI

class Langchain:
    
    _model = None
    _knowledge_base = None
    
    @staticmethod
    def load_model():
        if Langchain._model is None:
            Langchain._model = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
        return Langchain._model
    
    @staticmethod
    def create_embeddings_with_langchain(file):
        with open(file, 'r', encoding='utf-8') as file:
            text = file.read()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=100,
            length_function=len
        )        
        
        chunks = text_splitter.split_text(text)
        model = Langchain.load_model()
        Langchain._knowledge_base = FAISS.from_texts(chunks, model)

        return Langchain._knowledge_base
    
    def get_response_from_langchain(self, text_file, user_message):
        if Langchain._knowledge_base is None:
            Langchain._knowledge_base = self.create_embeddings_with_langchain(text_file)
        information = Langchain._knowledge_base.similarity_search(user_message, 7)
        return information