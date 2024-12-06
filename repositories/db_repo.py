import pyodbc  # Maakt verbinding met database via ODBC-drivers. Hiermee kun je SQL-query's uitvoeren.
import logging  # Python-module voor het vastleggen van foutmeldingen en waarschuwingen.
from typing import List
from utils.connector import DbConnector

# Logging configureren om foutmeldingen duidelijk weer te geven
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Klasse om met de 'dikke buiken'-database te communiceren
class DikkeBuikenRepo:
    
    con: pyodbc.Connection = None  # Variabele om de databaseconnectie op te slaan

    def __init__(self, db_connection: DbConnector):
        """
        Functie die de databaseconnectie initialiseert.

        Parameters:
        - db_connection: Een DbConnector-object dat verantwoordelijk is 
          voor het maken van een verbinding met de database.
        
        Returns: None
        """
        self.con = db_connection.connection  # Verbind met de database

    def get_all_weights(self) -> List[dict]:
        """
        Functie die alle records ophaalt uit de tabel dbo.weight_table.

        Returns:
        - Een lijst met dictionaries, waarbij elk dictionary de kolommen
          'Year' en 'AverageWeight' bevat.
        """
        data = []  # Lijst om de resultaten op te slaan
        try:
            # Cursor om SQL-commando's uit te voeren
            with self.con.cursor() as cursor:
                # SQL-query om Year en AverageWeight op te halen uit dbo.weight_table
                cursor.execute("SELECT Year, AverageWeight FROM dbo.weight_table;")
                
                # Haal alle rijen op uit het resultaat van de query
                rows: List[pyodbc.Row] = cursor.fetchall()

                # Itereer over de rijen en voeg de gegevens toe aan de lijst
                for row in rows:
                    data.append({
                        "Year": row[0], 
                        "AverageWeight": row[1]
                    })
                print(data)

        except Exception as e:
            # Log een foutmelding als er iets misgaat
            logger.error(f"Fout bij het ophalen van gegevens: {e}")
            raise

        return data
