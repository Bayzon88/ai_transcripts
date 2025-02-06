
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
from langchain_community.document_loaders import TextLoader

from EmbeddingService import EmbeddingService

load_dotenv()

@dataclass
class DBService:
    test: str = 'test'
    host:str = os.getenv('host')
    database:str = os.getenv('database')
    user:str = os.getenv('user')
    password:str = os.getenv('password')
    connection: str = f'''postgresql+psycopg://{user}:{password}@{host}:5432/{database}'''  
    collection_name : str = "my_docs"
    ollamaEmbeddings = OllamaEmbeddings(model=os.getenv('embedding_model'))
    text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
            length_function=len,
            is_separator_regex=False
        )
    
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
       
    
    def insert_embeddings_in_database(self,file_path):
        #Load document with full text 
        loader = TextLoader(file_path=file_path)
        documents = loader.load()
        
        #Divide text into chunks
        
        text_chunks = self.text_splitter.split_documents(documents=documents)
        db = PGVector.from_documents(documents=text_chunks,embedding=self.ollamaEmbeddings,collection_name=self.collection_name,connection=self.connection)      
        # query = 'how to purchase a house?'
        # print(db.similarity_search_with_score(query=query,k=2))
    
    def perform_similarity_search(self,prompt: str):
        
        db = PGVector(connection=self.connection, collection_name=self.collection_name,embeddings=self.ollamaEmbeddings)
        
        #Vectorize the prompt 
        vectorized_prompt = self.ollamaEmbeddings.embed_query(prompt)
        # return db.similarity_search_by_vector(embedding=vectorized_prompt,filter={"source": "G:\\AI\\ai_transcripts\\test.txt"})
        return db.similarity_search_with_score(prompt, k=50)
        
      
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
    pass
    # dbService = DBService()
    # file_path = os.path.join(os.getcwd(),'test.txt')
    # dbService.insert_embeddings_in_database(file_path=file_path)
    # similarity_search_result = dbService.perform_similarity_search(prompt='who are the potters')
    # print(similarity_search_result)

    
    