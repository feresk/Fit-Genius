
from pydantic import BaseModel
from fastapi import FastAPI

import numpy as np
import joblib
import allGoodDiets as gd
import LoadDietModel as ldm
import LoadWorkoutModel_ForestModel as lwm
app = FastAPI()



class ModelInputs(BaseModel) :
    age : int
    gender : int
    height : float
    weight : int
    goal : int
    level : int
    lifestyle : int
    session_time : int
    diabetes : int
    hypertension : int
    high_cholesterol : int
    osteoporosis : int
    arthritis : int
    copd : int
    stroke : int
    celiac_disease : int
    irritable_bowel_syndrome : int
    heart_disease : int
    kidney_disease : int
    lactose_intolerance : int
    gluten_intolerance : int
    fructose_intolerance : int
    histamine_intolerance : int
    fodmap_intolerance : int
    peanut_allergy : int
    tree_nut_allergy : int
    shellfish_allergy : int
    fish_allergy : int
    egg_allergy : int
    milk_allergy : int
    soy_allergy : int
    wheat_allergy : int


@app.get("/")
def index():
    print('hy')
    return {"messagee": "Hello, World!"}


@app.post('/predict')
def predict_diet(data : ModelInputs) :
    data = data.dict()
    # print(data)
    print('wow')

    age = data['age']
    gender = data['gender']
    height = data['height']
    weight = data['weight']
    goal = data['goal']
    level = data['level']
    lifestyle = data['lifestyle']
    session_time =data['session_time']
    diabetes = data['diabetes']
    hypertension = data['hypertension']
    high_cholesterol = data['high_cholesterol']
    osteoporosis = data['osteoporosis']
    arthritis = data['arthritis']
    copd = data['copd']
    stroke = data['stroke']
    celiac_disease = data['celiac_disease']
    irritable_bowel_syndrome = data['irritable_bowel_syndrome']
    heart_disease = data['heart_disease']
    kidney_disease = data['kidney_disease']
    lactose_intolerance = data['lactose_intolerance']
    gluten_intolerance = data['gluten_intolerance']
    fructose_intolerance = data['fructose_intolerance']
    histamine_intolerance = data['histamine_intolerance']
    fodmap_intolerance = data['fodmap_intolerance']
    peanut_allergy = data['peanut_allergy']
    tree_nut_allergy = data['tree_nut_allergy']
    shellfish_allergy = data['shellfish_allergy']
    fish_allergy = data['fish_allergy']
    egg_allergy = data['egg_allergy']
    milk_allergy = data['milk_allergy']
    soy_allergy = data['soy_allergy']
    wheat_allergy = data['wheat_allergy']

    digestive_disorders = celiac_disease or irritable_bowel_syndrome or lactose_intolerance or gluten_intolerance or fructose_intolerance or histamine_intolerance or fodmap_intolerance

    # APIKEY = insert your api key

    predDiet = ldm.makePrediction([age,gender,height,weight,goal,diabetes,hypertension,celiac_disease,irritable_bowel_syndrome,heart_disease,kidney_disease,
    lactose_intolerance,gluten_intolerance,fructose_intolerance,histamine_intolerance,fodmap_intolerance,
    peanut_allergy,tree_nut_allergy,shellfish_allergy,fish_allergy,egg_allergy,milk_allergy,soy_allergy,wheat_allergy])


    predWorkout = lwm.makePrediction(APIKEY , [age,gender,height,weight,goal,level,lifestyle,session_time,diabetes,hypertension,high_cholesterol,heart_disease,digestive_disorders,osteoporosis,arthritis,copd,stroke])
    # predWorkout = lwm.makePrediction(feres1)
    return predDiet+'\n'+predWorkout
