import whisper
from pydub import AudioSegment
import os

# model = whisper.load_model("turbo")
# result = model.transcribe("frances_12-12.mp3")

class AudioToText():
    def __init__(self):
        self.model = whisper.load_model("turbo")
        self.transcript : list[str]  = []   
        self.audio_file_name = f'{os.getcwd()}\\utils\\video_to_audio\\extracted_audio.mp3'
        self.audio_chunks_path_folder = f'{os.getcwd()}\\utils\\audio_to_text\\audio_chunks'

    #Delete files in a folder
    def delete_files_in_folder(self):
        #Check if the audio_chunks folder exists
        if not os.path.exists(self.audio_chunks_path_folder):
            os.makedirs(self.audio_chunks_path_folder)
            print(f"Folder created in {self.audio_chunks_path_folder}")
        else:
            try:
                for file_name in os.listdir(path=self.audio_chunks_path_folder):
                    file_path = os.path.join(self.audio_chunks_path_folder,file_name) #Generate path to the file 
                    if os.path.isfile:
                        os.remove(file_path)
                print("All Audio Chunks deleted")
            except Exception as err:
                print(err) 
            
        
    #Generate audio chunks to be processed one by one by Whisper
    def create_audio_chunks(self,chunk_length_ms=30000, overlap_ms=0): 
        #Get audio information
        audio = AudioSegment.from_mp3(self.audio_file_name)
        chunks = []
        start = 0 #Start pointer
        
        #Build chunks 
        while start < len(audio):
            end = start + chunk_length_ms
            chunks.append(audio[start:end]) #append current chunk(30s)
            start += chunk_length_ms - overlap_ms #New start will be the start plus the chunk size minus the overlap 
        return chunks
            
    
    def generate_transcript(self,audio_chunks) -> None:
        #Delete all files inside the chunks folder
        for i,audio in enumerate(audio_chunks):  
        
            #export chunk into a temporary audio file
            temp_audio_file_name = f'{self.audio_chunks_path_folder}\\chunk_{i}.mp3'
            temp_chunk = audio.export(temp_audio_file_name,format="mp3")
            result = self.model.transcribe(temp_audio_file_name)
            self.transcript.append(result['text'])
         
            # # make log-Mel spectrogram and move to the same device as the model
            # mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

            # # detect the spoken language
            # _, probs = model.detect_language(mel)
            # print(f"Detected language: {max(probs, key=probs.get)}")

            # # decode the audio
            # options = whisper.DecodingOptions()
            # result = whisper.decode(model, mel, options)
            # transcript.append(result.text)
    
    # Print the transcription
    def print_audio_transcription(self) -> str:
        with open(f'{os.getcwd()}\\utils\\audio_to_text\\transcript.txt', 'w',encoding='utf-8') as file: 
            transcript_text = ' '.join(self.transcript)
            file.write(transcript_text) 
        self.delete_files_in_folder()
        
        


