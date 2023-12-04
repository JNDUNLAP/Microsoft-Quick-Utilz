from connection.app import login



def get_emails(client_id:str, client_secret:str, email_depth:int) -> object:
    """
        Login -> Get Mailbox -> Read Excel -> Dataframe
    
    Args:
        Client ID - Oauth Creds
        Client Secret - Oauth Creds
        Email Depth - How Many Emails Do You Want ? 
        
    Returns
        emails: object
    """
    account = login(client_id, client_secret)
    mailbox = account.mailbox()
    emails = mailbox.get_messages(limit=email_depth)
    return emails

