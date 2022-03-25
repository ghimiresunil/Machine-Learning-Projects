import string
import re

def preprocess(text):
    sentences = text.strip().split(u"।")
    # sentences = re.sub(r'\s', '', sentences)
    sentences= [i.replace("\u202f", "") for i in sentences]
    sentences= [i.replace("\xa0", "") for i in sentences]
    sentences = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in sentences]
    return sentences 
