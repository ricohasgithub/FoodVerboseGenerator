import spacy

class Sentence:

    def __init__(self, source_sentence):
        self.sentence = source_sentence.split(" ")
        self.dep_types = ["na", "nsubj", "aux", "ROOT", "prep", "pcomp", "compound", "dobj", "quantmod", "pobj"]

    def in_length(self):
        if len(self.sentence) > 3:
            return True
        else:
            return False
    
    def vectorize(self, nlp):
        vector = []
        doc = nlp(self.sentence)
        for token in doc:
            vector.append(vector_value(token.dep_))
        self.vector = vector
        return vector

    def vector_value(self, type):
        return self.dep_types.index(type)

    def print_self(self):
        for word in self.sentence:
            print(word, end = " ")
        print()