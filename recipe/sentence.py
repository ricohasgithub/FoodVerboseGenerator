import spacy

class Sentence:

    def __init__(self, source_sentence):
        self.sentence = source_sentence.split(" ")
        self.dep_types = ["NA", "nsubj", "aux", "ROOT", "prep", "pcomp", "compound", "dobj", "quantmod", "pobj"]
        self.pos_types = ["PROPN", "VERB", "ADP", "NOUN", "SYM", "NUM"]

    def in_length(self):
        if len(self.sentence) > 3:
            return True
        else:
            return False
    
    # Default vectorization method: Syntatic dependency
    def vectorize(self, nlp):
        vector = []
        doc = nlp(self.sentence)
        for token in doc:
            vector.append(vector_dep_value(token.dep_))
        self.vector = vector
        return vector

    # Pos vectorization (Simple UPOS part-of-speech tag)
    def lemma_vectorize(self, nlp):
        vector = []
        doc = nlp(self.sentence)
        for token in doc:
            vector.append(vector_pos_value(token.pos_))
        self.vector = vector
        return vector

    # Tagging methods for vectorization

    def vector_dep_value(self, type):
        return self.dep_types.index(type)

    def vector_pos_value(self, type):
        return self.pos_types.index(type)

    def print_self(self):
        for word in self.sentence:
            print(word, end = " ")
        print()