import os
from dotenv import load_dotenv
load_dotenv()

class Config:
  CONTAINER_NAME = os.getenv("CONTAINER_NAME")
  STORAGE_NAME = os.getenv("STORAGE_NAME")
  STORAGE_CONNECTION_STRING = os.getenv("STORAGE_CONNECTION_STRING")
  KEY = os.getenv("KEY")
  ENDPOINT = os.getenv("ENDPOINT")