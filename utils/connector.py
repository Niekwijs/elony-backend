import pyodbc
from typing import type

class DbConnector:
    
    connection: pyodbc.Connection = None

    def __init__(self):
        self.connect()



    def connect(self)-> None :
        if self.connection and not self.connection.closed:
            print("Connection already active.")
            return

        connection_string = (
        "DRIVER={SQL Server};"        # Driver
        "SERVER=datadbserverdamen.database.windows.net;"         # Naam of IP van de server
        "DATABASE=sebasindebocht;"     # Naam van de database
        "UID=admindamen;"               # Gebruikersnaam
        "PWD=uiop7890UIOP&*();"               # Wachtwoord
        )
        try:
            self.connection = pyodbc.connect(connection_string)
            print("Verbinding succesvol!")
        except pyodbc.Error as e:
            print("Fout bij verbinden:", e)
            raise

    def close(self)-> None:
        if self.connection:
            self.connection.close()
            print("Connection closed.")
