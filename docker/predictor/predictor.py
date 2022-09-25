from keras import models
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
from pickle import load


class Ella:
    MAXLEN_PAD = 40

    def __init__(self, model_path, tokenizer_path):
        self.model = models.load_model(model_path)
        with open(tokenizer_path, "rb") as tk_file:
            self.tokenizer = load(tk_file)

    def get_predict(self, string: str, maxlen_pad: int = MAXLEN_PAD):
        string = string.lower()
        sequences = self.tokenizer.texts_to_sequences([string])
        entry = pad_sequences(sequences, padding='post', maxlen=maxlen_pad)
        pred = np.asarray(self.model.predict(entry)).reshape(-1)
        return (np.asarray(["none", "racism", "sexism"])[pred.argmax()])


