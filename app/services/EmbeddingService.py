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
        
        return embeddings
    
       
# if __name__ == '__main__':
#     embeddingService = EmbeddingService(f'''  In this video, we will go through how to sell a lot through the backhand. 
#  Find the project you want to sell a lot for in the drop-down list, then select Active Siting. 
 
#  Select the Search Lots drop-down. You can search for a lot by lot number, model name, elevation, or model type. Once you've selected your search criteria, select Search. 
#  At the top of the page,  there is a legend which represents the icons used within the active sighting. You can only sell a lot with the available green checkmark symbol. 
#  Select sell and if it's an individual or corporate sale. And enter in your password. You have option to add a note if you wish. Select the sell button. 
#  The lot is now sold. The next step is to.  go back to the project menu and click on sales list. This is where you can see all the lots that have been sold. 
#  The lot you just sold will be at the top of the list. 
#  Click the sales sheet button. Here you can fill in all the required purchaser information and other relevant fields for the sale.  Thank you.''')
#     embeddings = embeddingService.generate_transcript_embedding()
#     print(embeddings)