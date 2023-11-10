import os
from dotenv import load_dotenv

load_dotenv()

bind = f'{os.environ.get("HOST") or "127.0.0.1"}:{os.environ.get("PORT") or 8000}'
user = os.environ.get("USER") or 'jasurbek'
workers = 2
timeout = 120
