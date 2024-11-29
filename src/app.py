import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card

def configure_interface():
  """
  Set up a simple front to upload a file.
  """

  st.title("Upload your file")
  uploaded_file = st.file_uploader("Choose your file", type=["png", "jpg", "jpeg"])

  if uploaded_file:
    file_name = uploaded_file.name

    blob_url = upload_blob(uploaded_file, file_name)
    if blob_url:
      st.write(f"File {file_name} sent successfully to the Azure Blob Storage")
      credit_card_info = analyze_credit_card(blob_url)
      show_image_and_validation(blob_url, credit_card_info)
    else:
      st.write(f"Error on sending the file {file_name}.")

def show_image_and_validation(blob_url:str, credit_card_info:str):
  """
    Return the result of the validation

    Parameters
    ----------
    blob_url : str
        The blob storage url of the uploaded file.
    credit_card_info : str
        The analysis of the uploaded credit card.

    Returns
    -------
    None.

  """
  st.image(blob_url, caption="Image sent", use_column_width=True)
  st.write("Validation results")
  if credit_card_info and credit_card_info["card_name"]:
    st.markdown("<h1 style='color: green; '> Card is valid</h1>", unsafe_allow_html=True)
    st.write(f"Holder name: {credit_card_info['card_name']}")
    st.write(f"Bank Name: {credit_card_info['bank_name']}")
    st.write(f"Expiry Date: {credit_card_info['expiry_date']}")
  else:
    st.markdown(f"<h1 style='color: red;'>Card is invalid</h1>", unsafe_allow_html=True)
    st.write("This card is not valid")

if __name__ == "__main__":
  configure_interface()