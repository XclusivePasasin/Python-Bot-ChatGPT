import PyPDF2 #librería para sacar la info del pdf
from langchain.text_splitter import RecursiveCharacterTextSplitter
import openai
from fpdf import FPDF
from utils.database import DataBase as database_util
import os
from langchain import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import nlp


class PDF(FPDF):
    
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Product Catalog', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_product(self, product):
        title = f"{product['name']} - ${product['price']}"
        body = f"Description: {product['description']}\nAvailability: {product['availability']}"
        self.chapter_title(title)
        self.chapter_body(body)

    def get_pdf_for_catalog(self):  
        catalog = database_util.fetch_catalog()
        pdf = PDF()
        pdf.add_page()
        for product in catalog:
            pdf.add_product(product)
        output_path = os.path.join('static', 'Catalog.pdf')
        pdf.output(output_path)
        return output_path
    
    def read_pdf(self, output_path):
        pass


def extract_text_Pdf(pdf_path):

    with open(pdf_path, 'rb') as pdf_File:
        
        pdf_reader = PyPDF2.PdfFileReader(pdf_File)
        
        text = ""
        
        for num_page in range(pdf_reader.numPages):
            page = pdf_reader.getPage(num_page)
            text += page.extractText()
            
        return text

def divided_text(text):
    text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 900,
            chunk_overlap = 100,
            length_function = len
    )

    chunks = text_splitter.split_text(text)
    return chunks


def make_request(text, model="text-davinci-003", api_key="TU_API_KEY"):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine=model,
        prompt=text,
        max_tokens=100  # Le puse 100, porque creo que es suficiente, pero si querés le podés aumentar
    )
    return response.choices[0].text

def text_process_for_chatgpt(text):
    doc = nlp(text)
    processed_text = ""
    for sent in doc.sents:
        processed_text += sent.text.strip() + " "
    return processed_text.strip()

# Función para procesar el texto con Langchain
def process_with_langchain(chunks, api_key="TU_API_KEY"):
    llm = OpenAI(api_key=api_key)
    prompt = PromptTemplate(
        input_variables=["chunk"],
        template="Please, process the following text: {chunk}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    
    processed_response = []
    for chunk in chunks:
        response = chain.run(chunk)
        processed_response = text_process_for_chatgpt(response)
        processed_response.append(processed_response)
    return " ".join(processed_response)
