import pandas as pd 
from json import loads, dumps

def create_grafiek():
    # Inladen van de data (csv-file)
    file_path = "TSLA_ticker_2015_through_2020.csv"
    df_tsla_beursdata = pd.read_csv(file_path)
    
    # 'Date' kolom omzetten naar datetime type
    df_tsla_beursdata['Date'] = pd.to_datetime(df_tsla_beursdata['Date'])
    
    # 'Date' als index om resampling en grouping te vergemakkelijken:
    #   -> Eenvoudiger om op tijd gebaseerde bewerkingen uit te voeren
    #   Bijvoorbeeld: resampling, groeperen en aggregeren op tijdsintervallen
    df_tsla_beursdata.set_index('Date', inplace=True)

    # Bereken gemiddeld TSLA value voor elke maand
    df_monthly_mean = df_tsla_beursdata.resample('ME')['TSLA'].mean()

    # Reset index om 'Date' terug een kolom te make
    df_monthly_mean = df_monthly_mean.reset_index()

    # We knippen de dag eraf (YYYY-MM)
    df_monthly_mean['Date'] = df_monthly_mean['Date'].dt.strftime('%Y-%m')

    # Omzetten naar JSON format
    result_tsla_beursdata = df_monthly_mean.to_json(orient="records")
    parsed_beursdata = loads(result_tsla_beursdata)

    return parsed_beursdata
