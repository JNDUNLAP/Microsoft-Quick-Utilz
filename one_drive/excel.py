import pandas as pd 


def get_excel_data(file:object, local_path:str) -> object:
    """
        Read File -> Get Dataframe
    
    Args:

        365 File Object - Excel File in 365
        Local Path - In Your Container
        
    Returns
        Dataframe: object
    """
    try:
        file.download(to_path=local_path)
        df = pd.read_excel(local_path)
        return df
    except Exception as e:
        print(e)
        return None

