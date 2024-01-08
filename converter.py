
import os
from os import listdir
from os.path import isfile, join
import moviepy.editor as mp 
import speech_recognition as sr 


class Converter:
    WAV = 'wav'
    TEXT = 'txt'
    
    def _get_files(self, path):
        return [os.path.basename(f) for f in listdir(path) if isfile(join(path, f))]
    
    def _get_output_file_name(self, input_file, new_path, new_extension):
        output_file = '{}.{}'.format(input_file[:(len(input_file)-4)], new_extension)
        new_output_file = os.path.join(new_path, output_file)
        return new_output_file
    

class VideoConverter(Converter):
    
    def convert(self, input_path, output_path):
        file_names = self._get_files(input_path)
        for file_name in file_names:
            video = mp.VideoFileClip(os.path.join(input_path, file_name)) 
            audio_file = video.audio 
            audio_file_path = self._get_output_file_name(file_name, output_path, self.WAV)
            audio_file.write_audiofile(audio_file_path)
    
    
class AudioConverter(Converter):
    
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer() 
        
    def convert(self, input_path, output_path, language="en-US"):
        file_names = self._get_files(input_path)

        for file_name in file_names:
            print('AudioConverter - Converting audio to text for {}'.format(file_name))            
            with sr.AudioFile(os.path.join(input_path, file_name)) as source: 
                data = self.recognizer.record(source) 
                # recognize_google is used only for tests. Use recognize_google_cloud or others for 
                # better results. 
                text = self.recognizer.recognize_google(data, language=language) 
                transcript_file_path = self._get_output_file_name(file_name, output_path, self.TEXT)
                with open(transcript_file_path, 'w', encoding='utf-8') as f:
                    f.write(text)
            print('AudioConverter - Done.')