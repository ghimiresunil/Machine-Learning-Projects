import os
from gensim.models.word2vec import Word2Vec

def load_vector():
    root_path = os.path.dirname(os.path.abspath('__file__'))
    base_folder = os.path.join(root_path, "pretrained_word2vec_model")
    word_vector = Word2Vec.load(base_folder + '/nepaliW2V_5Million.model')
    return word_vector
