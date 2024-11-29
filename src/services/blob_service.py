import os
from azure.storage.blob import BlobServiceClient
import streamlit as st
from utils.Config import Config

def upload_blob(file, file_name):
  try:
    if Config.STORAGE_CONNECTION_STRING is None or Config.CONTAINER_NAME is None:
      st.error("Error retriving connection parameters. Please Check if they are not empty or if there is a typo")
      return None
    
    blob_service_client = BlobServiceClient.from_connection_string(Config.STORAGE_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=file_name)
    blob_client.upload_blob(file, overwrite=True)
    
    return blob_client.url
  except Exception as e:
    st.error(f"Error sending file to storage. {e}")
    return None