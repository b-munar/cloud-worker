import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    USERNAME=os.getenv("USERNAME")
    HOST=os.getenv("HOST")
    DATABASE=os.getenv("DATABASE")
    PASSWORD=os.getenv("PASSWORD")
    PORT_DB=os.getenv("PORT_DB")
    GOOGLE_CLOUD_PROJECT=os.getenv("GOOGLE_CLOUD_PROJECT")