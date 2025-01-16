
import os
from dotenv import load_dotenv
from services.EmbeddingService import EmbeddingService
from services.DBService import DBService
from utils.video_to_audio.VideoToAudio import VideoToAudio
from utils.audio_to_text.AudioToText import AudioToText
from services.AIService import AIService
load_dotenv('.env.instructions')

#Read Instructions file 
file_path = os.getenv('file_path')


# def get_audio_from_video() -> None :
#     #Get Audio from video
#     videoToAudio = VideoToAudio() 
#     videoToAudio.extract_audio_from_video(input_file_path=file_path)



# def get_transcript() -> str: 
#     #Convert audio to text using whisper
#     audioToText = AudioToText()

#     audio_chunks = audioToText.create_audio_chunks()
#     audioToText.generate_transcript(audio_chunks=audio_chunks)  
#     audioToText.print_audio_transcription()
#     return audioToText.transcript

# def generate_transcript_summary(transcript='') -> str:
#     aiService = AIService(transcript=transcript)
#     return aiService.get_llm_response(prompt="Create a summary")

# with open('./utils/audio_to_text/transcript.txt','r',encoding='utf-8') as file:
#     transcript = file.read()
#     response = generate_transcript_summary(transcript=transcript)    
#     print(response.content)

# get_audio_from_video()
# transcript = get_transcript()
# response = generate_transcript_summary(transcript=transcript)
# print(response.content)


#********************** INSERT VECTORS INTO DATABASE ***********************
embeddingService = EmbeddingService(transcript=f'''  In this video, we will go through how to sell a lot through the backhand. 
#  Find the project you want to sell a lot for in the drop-down list, then select Active Siting. 
 
#  Select the Search Lots drop-down. You can search for a lot by lot number, model name, elevation, or model type. Once you've selected your search criteria, select Search. 
#  At the top of the page,  there is a legend which represents the icons used within the active sighting. You can only sell a lot with the available green checkmark symbol. 
#  Select sell and if it's an individual or corporate sale. And enter in your password. You have option to add a note if you wish. Select the sell button. 
#  The lot is now sold. The next step is to.  go back to the project menu and click on sales list. This is where you can see all the lots that have been sold. 
#  The lot you just sold will be at the top of the list. 
#  Click the sales sheet button. Here you can fill in all the required purchaser information and other relevant fields for the sale.  Thank you.''')
embeddings = embeddingService.generate_transcript_embedding()

db_service = DBService()
db_service.insert_embeddings_in_database(embeddings=embeddings)



