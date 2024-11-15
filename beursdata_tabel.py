import pandas as pd 
from json import loads, dumps

def create_tabel():
    file_path = "TSLA_ticker_2015_through_2020.csv"
    df_tsla_beursdata = pd.read_csv(file_path)
    df_tsla_beursdata['Date'] = pd.to_datetime(df_tsla_beursdata['Date'])
    df_tsla_beursdata['Date'] = df_tsla_beursdata['Date'].dt.date           # tijd is in elke kolom 0000000, dus voor nu verwijderd.
    
    print(df_tsla_beursdata.head())

    df_tsla_beursdata = df_tsla_beursdata.dropna()
    result_tsla_beursdata = df_tsla_beursdata.to_json(orient = "records")
    parsed_beursdata = loads(result_tsla_beursdata)

    return parsed_beursdata

# create_tabel()