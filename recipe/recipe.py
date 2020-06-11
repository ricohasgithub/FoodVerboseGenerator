from recipe.sentence import Sentence

class Recipe:

    def __init__(self, recipe_food_name, recipe_source_url, recipe_content):
        self.r_food = recipe_food_name
        self.r_url = recipe_source_url
        self.r_content = recipe_content

        self.split_recipe(recipe_content)

    def split_recipe(self, recipe_content):
        # First replace all blank lines with periods (used to account for lists of data)
        recipe_content.replace("\n", ".")
        # All the sentences in the input string
        all_sentences = recipe_content.split(".")
        # List for all sentences that pass the minimum word length requirement
        sentences = []
        
        # Iterate through all sentences in the all_sentences list and append each sentence that is greater than the minimum length to the sentences list
        for c_sentence in all_sentences:
            # Create an insance of the current sentence in the body string
            c_sentence_inst = Sentence(c_sentence)
            # Check test
            if c_sentence_inst.in_length() == True:
                sentences.append(c_sentence_inst)

        self.r_sentences = sentences

    def tensorize(self):
        tensor = []
        for sentence in self.r_sentences:
            tensor.append(sentence.vectorize())
        self.r_tensor = tensor
        return tensor

    def print_body(self):
        # Equivalence of a Java toString method but prints it as well
        print("Source Food: " + self.r_food)
        print("Source URL: " + self.r_url)
        for sentence in self.r_sentences:
            sentence.print_self()