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



def send_email( client_id:str, client_secret:str, recepients:str,  message_subject:str, message_body:str):
    """
        Login -> New Message -> Send Message
    
    Args:
        Client ID - Oauth Creds
        Client Secret - Oauth Creds
        Message Subject - How Many Emails Do You Want ? 
        
    Returns
        emails: object
    """

    
    try:
        account = login(client_id, client_secret)
        m = account.new_message()
        m.to.add(recepients)
        m.subject = message_subject
        m.body = f"""<html>
                    <head>
                    <style>
                    
                    </style>
                    </head>
                    <body>
                        <p>VICTORY!!<p>
                        {message_body}
                    </body>
                    </html> 
                    """   
        m.send()
        print("Email Sent")
    except Exception as e:
        print("Email Failed to Send")
        print(e)