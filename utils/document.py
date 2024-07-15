from fpdf import FPDF
from utils.database import DataBase as database_util
import os 

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