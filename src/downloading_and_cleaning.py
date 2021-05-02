import os
import src.downloading_and_cleaning as dc

def download_dataset():
    '''Downloads a dataset from kaggle and only keeps the csv in your data file. Beware of your own data structure:
    this creates a data directory and also moves all the .csv files next to your jupyter notebooks to it.
    Takes: url from kaggle
    Returns: a folder with the downloaded csv
    '''
    
    #Gets the name of the dataset.zip
    url = "https://www.kaggle.com/ryanstonebraker/friends-transcript"
    
    #Gets the name of the dataset.zip
    endopint = url.split("/")[-1]
    user = url.split("/")[-2]
    
    #Download, decompress and leaves only the csv
    download = f"kaggle datasets download -d {user}/{endopint}"
    decompress = f"tar -xzvf {endopint}.zip"
    delete = f"rm -rf {endopint}.zip"
    make_directory = "mkdir data"
    lista = "ls >> archivos.txt"
    
    for i in [download, decompress, delete, make_directory, lista]:
        os.system(i)
    
    #Gets the name of the csv (you should only have one csv when running this code)
    lista_archivos = open('archivos.txt').read()
    nueva = lista_archivos.split("\n")
    
    #Moves the .csv into the data directory
    for i in nueva:
        if i.endswith(".csv"):
            move_and_delete = f"mv {i} data/dataset.csv; rm archivos.txt"
            return os.system(move_and_delete)


def create(df,column,list_):
    """
    Creates a subdataframe with those values of the given column present in the given list 
    Args:
        df (dataframe): dataframe to work with 
        column (series): column of the dataframe to be filtered on
        list_ (list): list with the values that are used for filtering 
    Returns:
        The subdataframe
    """
    return df[df[column].isin(list_)]


def cleaning(df,main_characters):
    """
    Cleans a dataframe.
    Args:
        df (df): the dataframe that wants to be cleaned
    Returns:
        The dataframe cleaned
    """
    df = df.drop_duplicates()
    df.dropna(axis = 0, how="all",inplace=True)
    df['author'].apply(lambda x: x.capitalize())
    df = dc.create(df,"author",main_characters)
    df = df.drop(["quote_order"],axis=1)
    df=df.reset_index()
    df['season'] = df['season'].astype('int').astype('str')
    df['episode_number'] = df['episode_number'].astype('int').astype('str')
    return df

