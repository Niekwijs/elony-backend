import pyodbc
from typing import Optional

from utils.pyodbc_utils import handle_datetimeoffset

class DbConnector:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connect()
        return cls._instance

    def __init__(self):
        pass 

    def _connect(self):

        server = 'datadbserverdamen.database.windows.net'
        database = 'staging_elony'
        username = 'admindamen'
        password = 'uiop7890UIOP&*()'
        driver = '{ODBC Driver 17 for SQL Server}'
        try:
            self.connection = pyodbc.connect(
            f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
            )
            self.connection.add_output_converter(-155, handle_datetimeoffset)
            print("Verbinding succesvol!")
        except pyodbc.Error as e:
            print("Fout bij verbinden:", e)
            raise

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = DbConnector() 
        return cls._instance

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")
            self.connection = None 