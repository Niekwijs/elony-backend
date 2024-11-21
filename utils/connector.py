import pyodbc
from typing import Optional

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
        connection_string = (
            "DRIVER={SQL Server};"  # Driver
            "SERVER=datadbserverdamen.database.windows.net;"  # Server address
            "DATABASE=staging_elony;"  # Database name
            "UID=admindamen;"  # Username
            "PWD=uiop7890UIOP&*();"  # Password (consider using environment variables or secure storage for credentials)
        )
        try:
            self.connection = pyodbc.connect(connection_string)
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