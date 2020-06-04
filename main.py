import json
import requests

import spacy

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

'''
 The API request path builder with mandatory data
 Format: https://api.edamam.com/search?q={FOOD_NAME}&app_id=${YOUR_APP_ID}&app_key=${YOUR_APP_KEY}
'''

# Edamam Recpie Search API Constants
food = "pizza"
app_id = ""
app_key = ""

# Building API path and retrieving required information
edmam_api_path = "https://api.edamam.com/search?q=" + food + "&app_id=" + app_id + "&app_key=" + app_key

# API Request Info Parsing
recipe_response = requests.get(edmam_api_path)
recipe_response_dict = json.loads(recipe_response.text)

source_url = recipe_response_dict["hits"][0]["recipe"]["url"]
ingredients = recipe_response_dict["hits"][0]["recipe"]["ingredients"]

# Log at this point to ensure that the program is running properly
print(recipe_response)
print(recipe_response_dict)

print(ingredients)
print(source_url)

# Webscrape and parse via bueatiful soup to get the html document from the recipe url
recipe_html_doc_request = Request(source_url, headers={"User-Agent": "Chrome/51.0.2704.84"})
recipe_html_doc = urlopen(recipe_html_doc_request).read()

print(recipe_html_doc)

# Beautiful Soup HTML document parser
recipe_soup_parser = BeautifulSoup(recipe_html_doc, 'html.parser')

# Retrieve neccesary document details
recipe_article_content = recipe_soup_parser.findAll("div", {"class": "article-content"})

print("All good!")