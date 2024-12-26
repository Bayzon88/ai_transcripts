from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

class AIService():
    def __init__(self, transcript=''):
        print('AIService initiated')
        self.transcript = transcript
        self.llm = self.generate_llm_instance()
        
    def generate_llm_instance(self) -> ChatOllama:
        print("Generating LLM Instance")
        return ChatOllama(
        model="qwen2.5-coder:14b",
        temperature=0.3,
        # other params...
        )
    def get_llm_response(self,prompt=f'''Eres un asistente diseñado para ayudar a resumir una clase de francés impartida en español. Cada vez que el usuario te proporcione una transcripción de la clase, deberás generar un resumen que incluya todos los temas tratados en la clase, vocabulario, verbos y sus conjugaciones, y recomendaciones para seguir adelante basadas en lo visto en clase.

                                    **Tu comportamiento:
                                        
                                    -Siempre responderás al usuario en español o inglés, nunca en otro idioma.
                                    -Incluso si el texto que estás resumiendo está en francés u otro idioma, proporciona el resumen traducido al español o inglés.
                                    -Cuando se te pida generar un resumen, utilizarás la transcripción proporcionada por el usuario y generarás un resumen basado en esa transcripción.
                                    -Sé más específico en tus respuestas; proporciona al menos 3 ejemplos para cada punto del resumen.
                                    -Lo que suele contener la transcripción proporcionada por el usuario:

                                    -Una clase de francés impartida por un profesor de habla hispana; a veces encontrarás palabras en español.
                                    -La interacción entre el profesor y los estudiantes. Ocasionalmente, el profesor pide a los estudiantes que respondan a una pregunta o repitan una frase.
                                    -Lo que debes proporcionar:

                                    -Debes responder con un resumen de la clase.
                                    -Debes utilizar la transcripción proporcionada por el usuario para generar el resumen; no inventes información ni añadas contenido que no esté presente.
                                    -DEBES RESPETAR LA ESTRUCTURA DEL RESUMEN COMO SE INDICA A CONTINUACIÓN.
                                    -A las palabras del vocabulario y a los verbos de la seccion verbos, agregale la pronunciacion(fonetica en español). Por ejemplo el verbo 'amour' se pronuncia /ah-moor/
                                    
                                    Finalmente, tu resumen debe estar en español y en un formato estructurado (como se indicó anteriormente) y en formato README.md.

                                        
                         ''') -> str:
        #Call ollama endpoint
       
        messages = [
            (
                "system",
                f"{prompt}",
            ),
            ("human", f'''Haz un resumen de esta transcripcion {self.transcript} de mi clase de frances. Genera el resumen en espano, pero si hay palabras en frances no las traduzcas. 
                                            *Lo que el resumen DEBE contener:
                                            
                                            **Resumen (Obligatorio):
                                                -Presentar todo lo que vimos en clase.
                                                -¿De qué se trató?
                                                -¿Qué tema específico?
                                                -¿Cuáles son los puntos a mejorar?
                                            
                                            *Vocabulario (Obligatorio):
                                                -Palabras que aprendimos durante la clase.
                                                -Enumera las palabras, un ejemplo de cómo usarlas y su traducción al español/inglés.
                                            
                                            *Verbos (Obligatorio):
                                                -El verbo que aprendimos durante la clase.
                                                -Conjugaciones del verbo.
                                                -En qué situaciones se puede usar el verbo y su traducción al español/inglés.
                                                
                                            *Tareas (Opcional):
                                                -Si el profesor asigna tareas, enuméralas.
                                                -Generalmente, las tareas son del libro; por ejemplo, el profesor puede decir: 'Página 40, ejercicios 14, 15 y 16'.
                                                -Esto es opcional; solo si el profesor asigna una tarea, debes mencionarla.
                                            
                                            *Próximos pasos (Opcional):
                                                -Qué hacer a continuación.'''),
            # ("human", f"Dame el resumen de la clase segun tu system prompt"),
        ]
        ai_msg = self.llm.invoke(messages)
     
        return ai_msg       
        


