
from dataclasses import dataclass
import os
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
import psycopg2
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from langchain_postgres import PGVector
from langchain_postgres.vectorstores import PGVector

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
    
    
    def insert_embeddings_in_database(self,embeddings: List[List[float]]):
        connection = f'''postgresql+psycopg://{self.user}:{self.password}@{self.host}:5432/{self.database}'''  # Uses psycopg3!
        collection_name = "my_docs"

        embedding = OllamaEmbeddings(model=os.getenv('embedding_model'))
        vectors = embedding.embed_query('THIS IS A TEST OF THE EMBEDDINGS')
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
            length_function=len,
            is_separator_regex=False
        )
        # loader = TextLoader()
        text_chunks = text_splitter.split_text('''In this video, we will go through how to sell a lot through the backhand. 
                    Find the project you want to sell a lot for in the drop-down list, then select Active Siting. 
                    
                    Select the Search Lots drop-down. You can search for a lot by lot number, model name, elevation, or model type. Once you've selected your search criteria, select Search. 
                    At the top of the page,  there is a legend which represents the icons used within the active sighting. You can only sell a lot with the available green checkmark symbol. 
                    Select sell and if it's an individual or corporate sale. And enter in your password. You have option to add a note if you wish. Select the sell button. 
                    The lot is now sold. The next step is to.  go back to the project menu and click on sales list. This is where you can see all the lots that have been sold. 
                    The lot you just sold will be at the top of the list. 
                    Click the sales sheet button. Here you can fill in all the required purchaser information and other relevant fields for the sale.  Thank you.''')
        print(text_chunks[0])
        # vector_store = PGVector(
        #     embeddings=vectors,
        #     collection_name=collection_name,
        #     connection=connection,
        #     use_jsonb=True,
        # )
        vetor_store = PGVector.from_texts(embedding=vectors,texts=text_chunks,collection_name=collection_name,connection=connection)
        # vector_store.add_embeddings(embeddings=vectors,texts=text_chunks,)
        
    
      
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
    dbService.insert_embeddings_in_database([1,2,3])
    
    