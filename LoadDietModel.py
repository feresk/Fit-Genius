
import pandas as pd
import numpy as np
import pickle
import allGoodDiets as gd
import warnings
import openai

# Disable all warnings
warnings.filterwarnings('ignore')


with open('./DIET/DietModel.pkl', 'rb') as f:
  finalModel  = pickle.load(f)

# foodData = pd.read_csv("food_data.csv")
#
# def pandasToList(foodItem) :
#     res = []
#     res.append(foodData[foodData.Food  == foodItem].Calories.values[0])
#     res.append(foodData[foodData.Food  == foodItem].Protein.values[0])
#     res.append(foodData[foodData.Food  == foodItem].Carbs.values[0])
#     return res


def makePrediction(APIKEY, featureList) :
    a = featureList[0]
    ge = featureList[1]
    h = featureList[2]
    w = featureList[3]
    go = featureList[4]
    featureList.pop(4)
    featureList = np.array(featureList).reshape(1,-1)
    diet = gd.all_good_diets[finalModel.predict(featureList)[0]]
    bmr_men = ( 88.362 + (13.397 * w ) + (4.799 * h * 100 ) - (5.677 * a ) )
    bmr_women = ( 447.593 + (9.247 * w ) + (3.098 * h * 100) - (4.330 * a ) )
    calories_per_meal_men =  ( bmr_men * (  go*.35 + .85 ) )  // 3
    calories_per_meal_wommen = ( bmr_women * ( go*.35 + .85 ) )  //  3
    calories_per_meal = ge * calories_per_meal_men + (1-ge) * calories_per_meal_wommen
    protein_per_meal = 0.8 * w
    carbs_per_meal = ( calories_per_meal * (go*.1 + .35) ) // 4
    fibers_per_meal = ( go*.1+.15 ) * w // 3

    dietString = f'Your Calories need for each meal is :  {calories_per_meal}\n'
    dietString += f'Your Protein need for each meal is :  {protein_per_meal}\n'
    dietString += f'Your Carbs need for each meal is :  {carbs_per_meal}\n'
    dietString += f'Your Fibers need for each meal is :  {fibers_per_meal}\n'
    dietString += f'Your Diet Plan is :'
    for i in diet :
        dietString += f'{i} : {diet[i]}\n'

    openai.api_key = APIKEY
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
            "content" : 'Give me 3 meals (breakfast, lunch, dinner) as (1,2,3) each having 3 food items with their quantaties (gram) from followwing the diet plan.'+dietString+
                'Answer in the following way :  '
                '{\n'
                ' "meal_id" : meal_id_number,\n'
                ' "calories": ,\n'
                ' "protein": ,\n'
                ' "carbs": ,\n'
                ' "fibers": ,\n'
                ' "ingredients" : [ \n'
                '   {"ingredient_id": 1, "name": "", "quantity": },\n'
                '   {"ingredient_id": 2, "name": "", "quantity": },\n'
                '   {"ingredient_id": 3, "name": "", "quantity": } \n'
                '   ] \n'
                '}\n'
            }
        ]
    )

    return output.choices[0].message.content


# feres = [22,0,1.9,85,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# res = makePrediction(feres)
# print(res)
