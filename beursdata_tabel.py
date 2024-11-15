import pandas as pd 
from json import loads, dumps

def create_tabel():
    file_path = "TSLA_ticker_2015_through_2020.csv"
    df_tsla_beursdata = pd.read_csv(file_path)
    # Tijd is overal 0000000, dus voor nu verwijderd
    df_tsla_beursdata['Date'] = pd.to_datetime(df_tsla_beursdata['Date']).dt.date
    
    # Mbv lambda functie gefilterd op eerste dag van de maand
    df_first_of_month = df_tsla_beursdata[
        df_tsla_beursdata['Date'].apply(lambda x: x.day == 1)
    ]

    print(df_first_of_month.head())


    df_first_of_month = df_first_of_month.dropna()
    result_tsla_beursdata = df_first_of_month.to_json(orient = "records")
    parsed_beursdata = loads(result_tsla_beursdata)

    return parsed_beursdata