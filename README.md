# using-azure-features-to-detect-document-fraud

A project showcasing how to use Azure Document Intelligence to detect frauds in credit cards.

# Initial Setup (Azure Portal):

Resources you have to create:
* Document intelligence
* Storage account
  * When creating the resouce, set the `primary service` as `Azure Files`
  * When creation is done, allow `Allow Blob anonymous access` going to `Settings > Configuration` and set this option as `Enabled`

# Running the project (vscode or any preferred editor)
1. On `.env` file, set the variables with the access keys of your resources you've created on Azure Portal
2. On your terminal:
     * Run the command `pip install -r requirements.txt`. This will install all the dependencies
     * Run the command `streamlit run .\src\app.py`. This will open an interative screen so you can upload files and check the results
