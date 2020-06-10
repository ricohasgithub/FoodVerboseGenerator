class Recipe:

    def __init__(self, recipe_food_name, recipe_source_url, recipe_content):
        self.r_food = recipe_food_name
        self.r_url = recipe_source_url
        self.r_content = recipe_content

    def split_recipe(self, recipe_content):
        sentences = recipe_content.split(".")
        self.r_senteces = sentences