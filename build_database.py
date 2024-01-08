from vector_db import VectorDB
from converter import AudioConverter, VideoConverter


if __name__ == '__main__':
    videos_path = 'videos'
    audio_path = 'audios'
    transcripts_path = 'transcripts'
    index_path = 'db'

    skip = input('Do you want skip any stage? (1: Video to audio, 2: Audio to text):')
    
    if skip != '1' and skip != '2': 
        print('Converting videos to audio...')
        video_converter = VideoConverter()
        video_converter.convert(videos_path, audio_path)
    
    if skip != '2':     
        print('Converting audio to text...')
        audio_converter = AudioConverter()
        audio_converter.convert(audio_path, transcripts_path)
    
    print('Creating the vector database')
    vector_db = VectorDB()
    vector_db.build_index(transcripts_path, index_path)
    