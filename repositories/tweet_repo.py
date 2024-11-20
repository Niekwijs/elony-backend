import pyodbc
import logging
from typing import List
from datetime import datetime

from utils.connector import DbConnector


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class TweetRepo:
    con : pyodbc.Connection = None

    def __init__(self, db_connection : DbConnector):
        self.con = db_connection.connection
    
    def get_all(self)-> List[List]:
        data = []

        try:
            with self.con.cursor() as cursor:
                cursor.execute("SELECT * FROM  dbo.tweet_elon_musk;")

                rows : List[pyodbc.Row] = cursor.fetchall()
                
        except Exception as e:
            print(f'Get all went kinda wrong: {e}')
            raise
        return data 

    def get_tweet_by_id(self, id: int):
        result = {}

        try:
            with self.con.cursor() as cursor:
                cursor.execute("SELECT * FROM dbo.tweet_elon_musk WHERE id = ? ;",(id))
                columns = [column[0] for column in cursor.description]
                row: List[pyodbc.Row] = cursor.fetchone()
                
                if row:
                    result = dict(zip(columns, row))


                print(f'[+] for debugging purpose: {result}') 

        except Exception as e:
            print(f'get tweet by id = {id} went wrong!{e}')
            raise
        return result
