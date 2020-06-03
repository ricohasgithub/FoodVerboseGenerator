import json
import requests

'''
 The API request path builder with mandatory data
 Format: https://api.edamam.com/search?q={FOOD_NAME}&app_id=${YOUR_APP_ID}&app_key=${YOUR_APP_KEY}
'''

food = "pizza"
app_id = ""
app_key = ""

edmam_api_path = "https://api.edamam.com/search?q=" + food + "&app_id=" + app_id + "&app_key=" + app_key

recipe_response = requests.get(edmam_api_path)
recipe_response_dict = json.loads(recipe_response.text)

ingredients = recipe_response_dict["hits"][0]["recipe"]["ingredients"]

print(recipe_response)
print(recipe_response_dict)

print(ingredients)

print("All good!")