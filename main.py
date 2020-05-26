import requests

'''
 The API request path builder with mandatory data
 Format: https://api.edamam.com/search?q={FOOD_NAME}&app_id=${YOUR_APP_ID}&app_key=${YOUR_APP_KEY}
'''

food = ""
app_id = ""
app_key = ""

edmam_api_path = "https://api.edamam.com/search?q=" + food + "&app_id=" + app_id + "$app_key" + app_key

recipe_request = requests.get(edmam_api_path)

print("All good!")