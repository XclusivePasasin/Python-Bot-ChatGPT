import mysql.connector

class DataBase:
    
    @staticmethod
    def get_db_connection():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='Online_Shop'
        )

    @staticmethod
    def fetch_catalog():
        connection = DataBase.get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT name, price, description, availability FROM Products")
        catalog = cursor.fetchall()
        cursor.close()
        connection.close()
        return catalog
