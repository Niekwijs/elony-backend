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
                    cursor.close()
        except Exception as e:
            print(f'Get all went kinda wrong: {e}')
            raise
        return data 
    
    def get_by_date_range(self, start_date : str, end_date : str) -> List[List]:
        data = []
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        start_date_offset = start_date.strftime("%Y-%m-%dT%H:%M:%S+00:00")
        end_date_offset = end_date.strftime("%Y-%m-%dT%H:%M:%S+00:00")

        try:
            with self.con.cursor() as cursor:

                cursor.execute("SELECT Date_typed, TSLA FROM  dbo.tsla_ticker_2015_2020 WHERE Date_typed BETWEEN ? AND ?", (start_date_offset, end_date_offset))

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
            print(f"Get tsla by range went wrong: {e}")
            raise
        return data