import pandas as pd

def write_author(author_dict):
    df = pd.DataFrame.from_dict(author_dict, orient="index")
    df.to_csv('my_csv.csv', mode='a')
