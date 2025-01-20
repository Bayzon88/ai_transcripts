

from dataclasses import dataclass
from langchain_core.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from DBService import DBService
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain

@dataclass
class AIAssistantService:
    chat_ollama = ChatOllama(model="qwen2.5-coder:14b",temperature=0.3)
    
    
    def get_llm_response(self,user_prompt):
        #Get initial context from database 
        dbService = DBService() 
        similarity_search_result = dbService.perform_similarity_search(prompt=user_prompt)  
        print(similarity_search_result)
        #Generate chat template with initial context
        template = """You are an assistant that will answer user's question, you will only answer based on the information 
                    inside your context, you can't make stuff up, if you don't know the answer just say you don't know
                    {context}
                    
                    Question: {question} 
                    """
        prompt_template = PromptTemplate(template=template)
        formatted_prompt = prompt_template.format(context=similarity_search_result[0][0],question=user_prompt)
        
        #Request response from the LLM 
        response = self.chat_ollama.invoke(formatted_prompt)
        print(response.content)
        
        
        
if __name__ == '__main__':
    ai_assistant = AIAssistantService()
    ai_assistant.get_llm_response(user_prompt='who are the professors')
    