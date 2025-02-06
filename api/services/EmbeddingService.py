from dataclasses import dataclass
from typing import List
from dotenv import load_dotenv
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
load_dotenv()

@dataclass
class EmbeddingService:
    transcript : str 
    
    def generate_transcript_embedding(self) :
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
            length_function=len,
            is_separator_regex=False
        )
        text_chunks = text_splitter.split_text(self.transcript)
        return self.generate_ollama_embeddings(text_chunks=text_chunks)
    
    def generate_ollama_embeddings(self,text_chunks) :
        embed = OllamaEmbeddings(model=os.getenv('embedding_model'))
        
        embeddings = embed.embed_documents(text_chunks)
        # embeddings = embed.embed_query(text_chunks[1])
        
        return embeddings
    
       
if __name__ == '__main__':
    # with open(os.path.join(os.getcwd(),'test.txt'), 'r') as file: 
    #     text = file.read()
    #     embeddingService = EmbeddingService(f'''{text}''')
    #     embeddings = embeddingService.generate_transcript_embedding()
    #     print(embeddings)
    
    text = 'who is snape'
    embedding_service = EmbeddingService(transcript=text)
    vectorized_text = embedding_service.generate_transcript_embedding()
    print(vectorized_text)