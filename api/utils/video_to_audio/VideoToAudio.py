import subprocess
import os

class VideoToAudio():   
    def __init__(self):
        pass
    
    def extract_audio_from_video(self,input_file_path): 
        print(input_file_path)
        #Create Output filepath 
        name = os.path.basename(input_file_path) 
        output_file_path = f'{os.getcwd()}\\api\\utils\\video_to_audio\\extracted_audio.mp3'
        
        #Delete Existing file 
        self.delete_existing_audio_file(output_file_path)
        print("DELETED")
        #Function will use ffmpeg to extract the audio from a video recorded with OBS 
        try:
            #.wav
            # command = [
            #     'ffmpeg',
            #     '-i', input_video,    # Input file
            #     '-vn',               # Disable video recording
            #     '-acodec', 'pcm_s16le',  # Specify PCM signed 16-bit little-endian codec
            #     '-ar', '16000',      # Set audio sampling rate to 16,000 Hz
            #     '-ac', '1',          # Set number of audio channels to 1 (mono)
            #     output_audio
            # ]
        
            #.mp3
            command = [
            'ffmpeg',
            '-i', input_file_path,    # Input file
            '-vn',                # Disable video recording
            '-acodec', 'libmp3lame',  # Specify MP3 codec
            '-q:a', '2',          # Set audio quality (0 = best, 9 = worst)
            output_file_path          # Output file (e.g., 'output_audio.mp3')
            ]

            #execute the process in the command line
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as err:
            print(f"An error ocurred {err}")    

    def delete_existing_audio_file(self, output_file_path): 
        try:
            if os.path.isfile:
                os.remove(output_file_path) #Remove extracted_audio.mp3
            print("All Files deleted")
        except Exception as err:
            print(err) 
        

