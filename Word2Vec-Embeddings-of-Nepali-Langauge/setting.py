import os

ROOT = os.path.dirname(os.path.abspath(__file__))
tempStorage = os.path.join(ROOT,'tempStorage')

'''<------------Directory Absolute Paths------------------------------>'''
RootDir = os.path.dirname(os.path.abspath(__file__))
InputDir = os.path.join(RootDir,'input')

'''<-------Raw Text files--------->'''
raw_text_files = os.path.join(InputDir,'raw_text/raw_text.txt')

'''<-------Raw Text files--------->'''
stop_words = os.path.join(InputDir,'stopwords/stopwords.txt')