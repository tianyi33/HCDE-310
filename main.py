from flask import Flask, render_template, request
# By default, App Engine will look for an app called `app` in `main.py`.
from HCDE310_Project_method import random, name_search, meal_plan
import logging, json
app =Flask(__name__)

@app.route("/")
def home():
	""" This is the main page """
	return render_template('homepage_template.html')

@app.route("/lucky")
def lucky():
	""" This will call for a random recipe page """
	reci = random()
	return render_template('lucky_template.html', reci = reci)

@app.route("/reci_list")
def reci_list():
	""" This is the main recipe making page """
	return render_template('reci_list.html')

@app.route("/reci_list/feed")
def reci_list_feed():
	""" After user add text in the text box. Navigate them to this page """
	name = request.args.get('dishname')
	allergies = request.args.get('allergies')
	diet = request.args.get('diet')
	cuisine = request.args.get('cuisine')
	dish = request.args.get('dish')
	if name:
	# if the name of the dish is requested, it will take them to this page
		temp = name_search(name,intolerances = allergies, diet = diet, dishtype = dish, cuisine = cuisine)
		return render_template('reci_list.html', dish = temp, allergies = allergies, diet = diet, dishtype = dish, cuisine = cuisine)
	else:
	#if not, return a error message
		return render_template('reci_list.html', error="You need to put a name first")


@app.route("/mealplan/feed")
def mealplan_feed():
	time = request.args.getlist('timepicker')
	if(request.args.get('allergy')):
		allergy = request.args.get('allergy')
	else:
		allergy = None
	if(request.args.get('targetCalories')):
		targetCalories = request.args.get('targetCalories')
	else:
		targetCalories = None
	if (request.args.get('diet')):
		diet = request.args.get('diet')
	else:
		diet = None
	temp = []
	if (time[0] == 'day'):
  		time = 'day'
  		plan = meal_plan(timeFrame=time,targetCalories=targetCalories, diet = diet, exclude = allergy)
	else:
  		time = 'week'
  		plan = meal_plan(timeFrame=time,targetCalories=targetCalories, diet = diet, exclude = allergy)
  		for item in plan['items']:
  			temp.append(json.loads(item['value']))
  		plan = temp
	return render_template('mealplan.html', plan = plan, time = time,targetCalories=targetCalories)
# {% if plan != "" %}
# 		<div class="container">
#   <div class="row align-self-start">
#     	<div class="col-3">
# 	<a href="/reci_list" ><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-arrow-left-short" viewBox="0 0 16 16">
#   <path fill-rule="evenodd" d="M12 8a.5.5 0 0 1-.5.5H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5a.5.5 0 0 1 .5.5z"/>
# </svg></a>
# </div>
# <div class="col-8">
# 	</div>
# 	</div>
# 	</div>
# 	<h3 style="text-align: center;color:white"><strong>We can't create a meal plan fits your requirement, but here is a picture of a cute dog</strong></h3>
# 	<img class="mx-auto d-block" src='https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=2098&q=80' alt="Card image cap" style="height:650px; width: 1000px;align-content: center;">

# {% else %}
@app.route("/mealplan")
def mealplan():
	""" This is the main mealplan making page """
	return render_template('mealplan.html')

if __name__=="__main__":
# Used when running locally only. 
# When deploying to Google AppEngine, a webserver process will
# serve your app. 
	app.run(host="localhost", port=8086, debug=True)