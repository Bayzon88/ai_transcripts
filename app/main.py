
import os
from dotenv import load_dotenv
from utils.video_to_audio.VideoToAudio import VideoToAudio
from utils.audio_to_text.AudioToText import AudioToText
from services.AIService import AIService
load_dotenv('.env.instructions')

#Read Instructions file 
file_path = os.getenv('file_path')


def get_audio_from_video() -> None :
    #Get Audio from video
    videoToAudio = VideoToAudio() 
    videoToAudio.extract_audio_from_video(input_file_path=file_path)



def get_transcript() -> str: 
    #Convert audio to text using whisper
    audioToText = AudioToText()

    audio_chunks = audioToText.create_audio_chunks()
    audioToText.generate_transcript(audio_chunks=audio_chunks)  
    audioToText.print_audio_transcription()
    return audioToText.transcript

def generate_transcript_summary(transcript='') -> str:
    aiService = AIService(transcript=transcript)
    return aiService.get_llm_response(prompt="Create a summary")

# with open('./utils/audio_to_text/transcript.txt','r',encoding='utf-8') as file:
#     transcript = file.read()
#     response = generate_transcript_summary(transcript=transcript)    
#     print(response.content)

get_audio_from_video()
transcript = get_transcript()
response = generate_transcript_summary(transcript=transcript)
print(response.content)





