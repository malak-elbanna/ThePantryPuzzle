import requests
import json


APP_ID = 'df476c39'
APP_KEY = 'e614a0cd131f19058e22481140bcb6bc'
ENDPOINT_URL = 'https://api.edamam.com/api/recipes/v2'

params = {
    'q': 'chicken',
    'app_id': APP_ID,
    'app_key': APP_KEY,
    'type': 'public'
}

response = requests.get(ENDPOINT_URL, params=params)

if response.status_code == 200:
    data = response.json()
    ingredients_list = []
    count = 0
    for hit in data['hits']:
        for recipe in hit['recipe']['ingredients']:
            ingredient_name = recipe['food']
            count += 1
            ingredients_list.append({
                "Ingredient Id": count,
                "ingredient": ingredient_name
                })


json_object = json.dumps(ingredients_list, indent=1)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)

print("done")
