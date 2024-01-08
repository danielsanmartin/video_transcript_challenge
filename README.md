# Video sentence searcher

This project is an example of how to apply NLP for search sentences in videos.

## Description

In this project state of the art technologies were used in order to allow users loading mp4 files from a folder, build a superfast database and find similar contents in video transcriptions.

## Getting Started

### Dependencies

* Python 3.7
* Libraries listed into requirements.txt

### Installing

* Create a virtual environment. Activate it. In Windows you can use the command bellow:
```
virtualenv venv
```

* Install the libraries listed in the file requirements.txt

```
pip install -r requirements.txt
```
* Create the appropriate folder structure in the project root:
```
videos - to include videos.
audios - stores the audios extracted from videos.
transcripts - stores the transcription from audios.
db - stores the vector index and sentences.
```

### Executing program

How to run the program:

#### Create the Database 

The first step is create the vector database based on videos transcriptions.

* Include the videos (max. 10mb) in "videos" directory or use the sample videos.
* Run the command bellow to process the videos.
```
python build_database.py
```
This script will perform the following tasks:

* Converts videos files in audios files, and save them into "audios" folder;
* Transcripts audio files, save each one in "transcript" folder;
* Extract sentences, save them into a file (data.csv), create a vector index (data.index), and save them into "db" folder.

#### Perform searches

Run the command bellow:

```
python search.py
```

The script will ask for the text you want search in the files.

## Authors

Contributors names and contact info

Daniel San Martin [https://www.linkedin.com/in/daniel-sanmartin/]

