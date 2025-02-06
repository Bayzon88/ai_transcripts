

from dataclasses import dataclass
from langchain_core.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from DBService import DBService
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain

@dataclass
class AIAssistantService:
    chat_ollama = ChatOllama(model="d",temperature=0.3)
    
    
    def get_llm_response(self,user_prompt):
        #Get initial context from database 
        dbService = DBService() 
        similarity_search_result = dbService.perform_similarity_search(prompt=user_prompt)  
        
        #Generate chat template with initial context
        template = """You are an assistant that will answer user's question, you will only answer based on the information 
                    inside your context, you can't make stuff up, you'll check your context before answering, if the context contains information
                    about the user's question, then you can respond, otherwise just say i don't know. 
                    {context}
                    
                    Question: {question} 
                    """
        prompt_template = PromptTemplate(template=template)
        
        #Retrieve all results from similarity search 
        context = "".join([search_result[0].page_content for search_result in similarity_search_result])
        # context = ""
        #Create formatted prompt
        formatted_prompt = prompt_template.format(context=context,question=user_prompt)
        
        #Request response from the LLM 
        response = self.chat_ollama.invoke(formatted_prompt)
        print(response.content)
        
        
        
if __name__ == '__main__':
    ai_assistant = AIAssistantService()
    ai_assistant.get_llm_response(user_prompt='give me a list of all professor')
    