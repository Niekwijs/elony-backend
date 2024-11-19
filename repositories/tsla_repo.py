import pyodbc
import logging
from typing import List
from datetime import datetime

from utils.connector import DbConnector


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)



class TslaRepo:
    con: pyodbc.Connection = None

    def __init__(self, db_connection : DbConnector):
        self.con = db_connection.connection
    
    def get_all(self)-> List[List]:
        data = []

        try:
            with self.con.cursor() as cursor:
                
                cursor : pyodbc.Cursor = self.con.cursor()

                cursor.execute("SELECT * FROM  dbo.tsla_ticker_2015_2020;")

                rows : List[pyodbc.Row] = cursor.fetchall()
                
                for row in rows:
                    date_str = row[0]
                    tsla_value = row[1]

                    date_obj = datetime.fromisoformat(date_str)

                    iso_date = date_obj.replace(tzinfo=None).isoformat() + "Z"
                
                    data.append({
                        "Date": iso_date,
                        "Tsla": tsla_value
                    })
        except Exception as e:
            print(f'Get all went kinda wrong: {e}')
            raise
        return data 



