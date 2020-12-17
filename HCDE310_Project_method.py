import requests, json, random

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

def name_search(query, cuisine = None, diet = None, excludeIngredients = None,intolerances = None,number = 3,dishtype = "main course"):
# The dishtype of the recipes. 
# One of the following: main course, side dish, dessert, appetizer, salad, bread, breakfast, soup, beverage, sauce, or drink.
# a recipe search based on a dish name return a json object
	url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
	querystring = {"query":query, "diet": diet, "excludeIngredients":excludeIngredients,"intolerances":intolerances,"number":number,"offset":"0","type":dishtype}
	headers = {
	    'x-rapidapi-key': "a5130286cbmshec7ab533ae5ae67p1a53d7jsnbd7dd4050ed4",
	    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
	    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	response = response.json()
	return response
import requests

def ingredients_search(ingredients, number = 3,ranking = 1):
# a recipe search based on ingredients return a json object
# Whether to maximize used ingredients (1) or minimize missing ingredients (2) first.
	url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"
	querystring = {"ingredients":ingredients,"number":number,"ranking":ranking,"ignorePantry":"true"}
	headers = {
	    'x-rapidapi-key': "a5130286cbmshec7ab533ae5ae67p1a53d7jsnbd7dd4050ed4",
	    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
	    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	response = response.json()
	return response

def findcommon(id):
# get one recipe that similar to the id given
	url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/" + str(id) + "/similar"
	headers = {
	    'x-rapidapi-key': "a5130286cbmshec7ab533ae5ae67p1a53d7jsnbd7dd4050ed4",
	    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
	    }
	response = requests.request("GET", url, headers=headers).json()
	placeholder = random.sample(response, k = 1)
	return placeholder

def steps(id):
	# return a json object with all the steps of making the input recipe
	instruction_url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"
	instruction_querystring = {"stepBreakdown":"true"}
	instruction_headers = {
    'x-rapidapi-key': "a5130286cbmshec7ab533ae5ae67p1a53d7jsnbd7dd4050ed4",
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }
	instruction_url = instruction_url + str(id) + "/analyzedInstructions"
	instruction_response = requests.request("GET", instruction_url, headers=instruction_headers, params=instruction_querystring)
	instruction_response = instruction_response.json()
	return instruction_response[0]['steps']

def random():
	# method for a random recipe
	url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"
	querystring = {"number":"1"}
	headers = {
	    'x-rapidapi-key': "a5130286cbmshec7ab533ae5ae67p1a53d7jsnbd7dd4050ed4",
	    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
	    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	response = response.json()
	return response['recipes'][0]

def printsteps(instruction_response):
	for step in instruction_response:
		print(step['number'])
		print(step['step'])
		print("--------")

def meal_plan(timeFrame = 'day', targetCalories = None, diet = None, exclude = None):
	url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"
	querystring = {"timeFrame":timeFrame,"targetCalories":targetCalories,"diet":diet,"exclude":exclude}
	headers = {
	    'x-rapidapi-key': "a5130286cbmshec7ab533ae5ae67p1a53d7jsnbd7dd4050ed4",
	    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
	    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	response = response.json()
	return response

# "imageUrls"
# Test code below
# {'id': 492564, 'title': 'Falafel Burgers with Feta Cucumber Sauce', 'readyInMinutes': 50, 'servings': 6, 'sourceUrl': 'https://www.cinnamonspiceandeverythingnice.com/falafel-burgers-with-feta-tzatziki-sauce/', 'openLicense': 0, 'image': 'falafel-burgers-with-feta-tzatziki-sauce-492564.jpg'}
# cuisine = None, diet = None, excludeIngredients = None,intolerances = None,number = 3,dishtype = "main course"
# print(name_search('apple'))
# # print("------")
# # print(findcommon(245166))
# print("------")
# for item in meal_plan(timeFrame = 'week')['items']:
# 	print(json.loads(item['value'])['title'])
# 	print("-------")