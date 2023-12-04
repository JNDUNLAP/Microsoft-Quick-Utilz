from connection.app import login

def get_item(client_id:str, client_secret:str, item_path:str) -> object:
    """
        Login -> Get Item -> Save an Excel -> Read Excel -> Dataframe
    
    Args:
        Client ID - Oauth Creds
        Client Secret - Oauth Creds
        Online Item Path - Path in 365 Onedrive
        Local Path - In Your Container
        
    Returns
        Dataframe: object
    """
    try:
        account = login(client_id, client_secret)
        storage = account.storage()
        my_drive = storage.get_default_drive()
        file = my_drive.get_item_by_path(item_path)
        return file
    except Exception as e:
        print(e)
        return None


