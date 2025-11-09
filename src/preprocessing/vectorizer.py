"""
Sentence to vector conversion using Word2Vec.
"""
import numpy as np
from gensim.models import Word2Vec
from src.utils import config


def tokenize_sentences(sentences):
    """
    Tokenize sentences into words.

    Args:
        sentences: List of sentence strings

    Returns:
        list: List of tokenized sentences
    """
    return [sentence.lower().split() for sentence in sentences]


def train_word2vec(tokenized_sentences):
    """
    Train Word2Vec model on tokenized sentences.

    Args:
        tokenized_sentences: List of tokenized sentences

    Returns:
        Word2Vec: Trained model
    """
    model = Word2Vec(
        sentences=tokenized_sentences,
        vector_size=config.WORD2VEC_VECTOR_SIZE,
        window=config.WORD2VEC_WINDOW,
        min_count=config.WORD2VEC_MIN_COUNT,
        workers=config.WORD2VEC_WORKERS,
        epochs=config.WORD2VEC_EPOCHS
    )
    return model


def sentence_to_vector(sentence, model):
    """
    Convert sentence to vector by averaging word vectors.

    Args:
        sentence: Tokenized sentence (list of words)
        model: Trained Word2Vec model

    Returns:
        NumPy array: Sentence vector
    """
    vectors = [
        model.wv[word] for word in sentence
        if word in model.wv
    ]

    if len(vectors) == 0:
        return np.zeros(config.WORD2VEC_VECTOR_SIZE)

    return np.mean(vectors, axis=0)


def vectorize_sentences(sentences):
    """
    Convert all sentences to vectors using Word2Vec.

    Args:
        sentences: List of sentence strings

    Returns:
        NumPy array: Matrix of sentence vectors
    """
    tokenized = tokenize_sentences(sentences)
    model = train_word2vec(tokenized)

    vectors = [sentence_to_vector(sent, model) for sent in tokenized]
    return np.array(vectors)
