import os
from dotenv import load_dotenv

# Load variables .env
load_dotenv()

class Config:
    key = os.getenv('KEY_IA')
    model = os.getenv('MODEL')
    token_verify = os.getenv('TOKEN_VERIFY')
    whatsapp_token = os.getenv('WHATSAPP_TOKEN')
    whatsapp_url = os.getenv('WHATSAPP_URL')
    
  
    