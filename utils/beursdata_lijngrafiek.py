import matplotlib
matplotlib.use('Agg')

import pandas as pd 
import matplotlib.pyplot as plt
from json import loads, dumps
from io import BytesIO
from pathlib import Path

def create_grafiek_matplotlib():
    # Inladen van de data (csv-file)
    file_path = "./data/TSLA ticker 2015 through 2020.csv"

    try:
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

        # Plotten van de grafiek met matplotlib
        plt.figure(figsize=(15,6))  # Grootte van de grafiek aanpassen
        plt.plot(df_monthly_mean['Date'], df_monthly_mean['TSLA'], marker='o', color='b', linestyle='-', linewidth=2)

        # Titel en labels toevoegen
        plt.title('Gemiddelde TESLA-waarde per Maand (2015-2020)', fontsize=14)
        plt.xlabel('Datum (Maand)', fontsize=12)
        plt.ylabel('Gemiddelde TESLA Waarde', fontsize=12)

        # Draai de x-as labels voor betere leesbaarheid
        plt.xticks(rotation=45)

        # Zorgt ervoor dat alles netjes in de grafiek past
        plt.tight_layout()  
        # plt.show() # Toon de plot

        # Sla de grafiek op als afbeelding in PNG formaat
        # plt.savefig('beursdata_lijngrafiek.png') 
        # plt.close()  # Sluit de plot af

        # Toon een bericht om aan te geven dat de afbeelding is opgeslagen
        # print("De grafiek is opgeslagen als 'beursdata_lijngrafiek.png'.")

        # Converteer grafiek naar een BytesIO-object
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)
        plt.close()
    except Exception as e:
        print(e)
        raise e

    return img_buffer