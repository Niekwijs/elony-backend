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

                columns = [column[0] for column in cursor.description]
                rows = cursor.fetchall()
                
                for row in rows:
                    data.append(dict(zip(columns, row)))
                
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

        except Exception as e:
            print(f'get tweet by id = {id} went wrong!{e}')
            raise
        return result

    def check_if_saved(self,  tweet_id: int)-> bool:
        res: bool = False
        try:
            with self.con.cursor() as cursor:
                cursor.execute("Select * FROM dbo.is_saved_tweet WHERE tweet_elon_musk_id = ?;",(tweet_id))

                row: List[pyodbc.Row] = cursor.fetchall()

                res = len(row)> 0

        except Exception as e:
            print(f'Check if tweet is saved went wrong with: {e}')
            raise
        return res
    
    def save_tweet_by_id(self, tweet_id: int): 
        res= {}


        # check if tweet id exists
        if len(self.get_tweet_by_id(tweet_id)) == 0:
            res["message"] = f'Tweet with id {tweet_id} does not exist in table dbo.tweet_elon_musk'
            return res             

        # check if not already saved
        if self.check_if_saved(tweet_id):
            res['message'] = f'tweet with id {tweet_id} is already saved!'
            return res
        
        else:
            try: 
                with self.con.cursor() as cursor:
                    cursor.execute("INSERT INTO dbo.is_saved_tweet (tweet_elon_musk_id) VALUES ((SELECT id FROM dbo.tweet_elon_musk WHERE id = ?));",(tweet_id)) 

                    self.con.commit() 
                    res["message"] = f"Tweet with id {tweet_id} has been successfully saved."
                    res["success"] = True
            except Exception as e:
                    print(f'Something went wrong wen savind the tweet with {e}')
                    res["message"] = f"Failed to save tweet with id {tweet_id}."
                    res["success"] = False
            return res
        
    def get_three_after_date(self, date):
        data = []

        try:
            with self.con.cursor() as cursor:
                cursor.execute("""SELECT TOP 3 * 
                                FROM dbo.tweet_elon_musk
                                WHERE created_at >= ?
                                ORDER BY created_at; """, (date))

                columns = [column[0] for column in cursor.description]
                rows = cursor.fetchall()

                if len(rows) == 0:
                    data.append( {"error" : "There are no tweets before or after this date"})
                    return data
                
                for row in rows:
                    data.append(dict(zip(columns, row)))

                
        except Exception as e:
            print(f'Get all went kinda wrong: {e}')
            raise
        return data 