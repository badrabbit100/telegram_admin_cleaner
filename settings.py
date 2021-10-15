import os
from dotenv import load_dotenv
load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
session_id = os.getenv('SESSION_ID')
channel_name = os.getenv('CHANNEL_NAME')
limit_messages_to_clean = 20
