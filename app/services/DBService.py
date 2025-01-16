
from dataclasses import dataclass
import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

@dataclass
class DBService:
    test: str = 'test'
    host:str = os.getenv('host')
    database:str = os.getenv('database')
    user:str = os.getenv('user')
    password:str = os.getenv('password')
    
    def create_db_connection(self):
        print(os.getenv('host'))
        try:
            conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            
                )
            return (conn.cursor(), conn)
        except Exception as exc:
            print(exc)
    
    def close_db_connection(self,cursor, conn):
        cursor.close()
        conn.close()
    
    def execute_similarity_search(self, ):
        print('Executing Similarity Search')
      
    def call_database(self):
        try:
            cursor,conn = self.create_db_connection()
            cursor.execute("SELECT * FROM items")
            rows = cursor.fetchall()
            for row in rows:
                uid, name = row
                print(name)
            
            self.close_db_connection(cursor, conn)
        except Exception as err:
            print("THERE IS AN ERROR ", err)
    
    
    
if __name__ == '__main__': 
    dbService = DBService()
    dbService.call_database()