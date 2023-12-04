from O365 import Account
import os
from dotenv import load_dotenv

load_dotenv()

def login(client_id:str, client_secret:str):
    """
    Login to general account
    
    Args:
        None
        
    Returns
        account:object 
    """
    try:
        client_id = os.getenv('CLIENT_ID_JD')
        client_secret = os.getenv('SECRET_VALUE_JD')
        account = Account(credentials = (client_id, client_secret))
        return account
    except Exception as e:
        print(e)

