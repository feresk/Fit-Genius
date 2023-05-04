import requests
import json

url = "http://127.0.0.1:8000/predict"
# create a dictionary of input data
input_data = {
    "age": 20,
    "gender": 1,
    "height": 1.80,
    "weight": 70,
    "goal": 1,
    "level" : 3,
    "lifestyle" : 0,
    "session_time" : 15,
    "diabetes": 0,
    "hypertension": 1,
    "high_cholesterol": 0,
    "osteoporosis": 0,
    "arthritis": 0,
    "copd": 0,
    "stroke" : 0,
    "celiac_disease": 0,
    "irritable_bowel_syndrome": 0,
    "heart_disease": 0,
    "kidney_disease": 0,
    "lactose_intolerance": 1,
    "gluten_intolerance": 0,
    "fructose_intolerance": 0,
    "histamine_intolerance": 1,
    "fodmap_intolerance": 0,
    "peanut_allergy": 0,
    "tree_nut_allergy": 0,
    "shellfish_allergy": 0,
    "fish_allergy": 0,
    "egg_allergy": 0,
    "milk_allergy": 0,
    "soy_allergy": 0,
    "wheat_allergy": 0
}
# convert the dictionary to a JSON string
input_data_json = json.dumps(input_data)
# print(input_data_json)
# set the content type of the request to JSON
headers = {"Content-Type": "application/json"}

# make the POST request with the input data as the request body
response = requests.post(url, data=input_data_json, headers=headers)

# print the response from the server
print(response.json())
