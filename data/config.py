import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("TOKEN"))
HOST = str(os.getenv("HOST"))
USER = str(os.getenv("USER"))
DB_PASSWORD = str(os.getenv("DB_PASSWORD"))
DB_NAME = str(os.getenv("DB_NAME"))

admin_id = [
    635915647
]

