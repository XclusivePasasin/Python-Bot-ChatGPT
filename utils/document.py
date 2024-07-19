from utils.database import DataBase as database_util
import os

class Document:

    @staticmethod
    def get_text_for_catalog():
        catalog = database_util.fetch_catalog()
        output_path = os.path.join('static', 'Catalog.txt')
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write("Product Catalog\n")
            file.write("=" * 50 + "\n\n")
            for product in catalog:
                title = f"{product['name']} - ${product['price']}"
                body = f"Description: {product['description']}\nAvailability: {product['availability']}\n"
                file.write(title + "\n")
                file.write(body + "\n")
                file.write("-" * 50 + "\n\n")
        return output_path


