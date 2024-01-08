import os
from os.path import isfile, join
import spacy
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd


class VectorDB:
    INDEX_FILE = 'data.index'
    DATA_FILE = 'data.csv'
    
    def __init__(self) -> None:
        self.index = None
        self.model = SentenceTransformer("paraphrase-mpnet-base-v2")
    
    def __chunk_transcript(self, directory, file_name):
        lines = []
        with open(os.path.join(directory, file_name)) as f:
            data = f.read()
            
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(data)
        sentences = list(doc.sents)

        for sentence in sentences:
            lines.append([str(sentence), file_name])

        return lines
    
    def build_index(self, input_path, db_path):
        files = [os.path.basename(f) for f in os.listdir(input_path) if isfile(join(input_path, f))]

        sentences = []
        
        for filename in files:
            sentences += self.__chunk_transcript(input_path, filename)        
        
        self.df = pd.DataFrame(sentences, columns = ['text', 'doc'])
        embeddings  = self.model.encode(self.df['text'])

        vector_dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(vector_dimension)
        faiss.normalize_L2(embeddings)
        self.index.add(embeddings)
        
        self.df.to_csv(os.path.join(db_path, self.DATA_FILE), encoding='utf-8')
        faiss.write_index(self.index, os.path.join(db_path, self.INDEX_FILE))        
        
    def load_index(self, db_path):
        self.index = faiss.read_index(os.path.join(db_path, self.INDEX_FILE))
        self.df = pd.read_csv(os.path.join(db_path, self.DATA_FILE))
        
    def search(self, text, top=5):        
        search_vector = self.model.encode(text)
        _vector = np.array([search_vector])
        faiss.normalize_L2(_vector)
        
        k = top
        distances, ann = self.index.search(_vector, k=k)
        results = pd.DataFrame({'distances': distances[0], 'ann': ann[0]})        
        merge = pd.merge(results, self.df, left_on='ann', right_index=True)[['distances', 'text','doc']]
        
        return merge
