class Sentence:

    def __init__(self, source_sentence):
        self.sentence = source_sentence.split(" ")

    def in_length(self):
        if len(self.sentence) > 3:
            return True
        else:
            return False