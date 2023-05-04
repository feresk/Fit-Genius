

import numpy as np
import tensorflow as tf
import workoutDict as wd
import pickle
import openai


with open('./WORKOUT/WorkoutModel.pkl', 'rb') as f:
  finalModel  = pickle.load(f)
#
# def makePrediction0(featureList) :
#   featureList.pop(6)
#   featureList.pop(6)
#   featureList = np.array(featureList).reshape(1, -1)
#   prediction = finalModel.predict(featureList)
#   return wd.allWorkouts[prediction[0]], finalModel.predict_proba(featureList)

def makePrediction(APIKEY, featureList) :
    a = featureList[0]
    ge = featureList[1]
    h = featureList[2]
    w = featureList[3]
    go = featureList[4]
    le =  featureList[5]
    li = featureList[6]
    total_workout_time = featureList[7]
    featureList.pop(7)
    featureList.pop(6)

    featureList = np.array(featureList).reshape(1, -1)
    prediction = finalModel.predict(featureList)
    exerciseList =  wd.allWorkouts[prediction[0]]

    openai.api_key = APIKEY
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
            "content" : 'Give an estimate of each MET using the following list'+f'{exerciseList}'
                'Answer in the following way :  '
                "[ a list of METs without exercises' names ]"
            }
        ]
    )

    def exerciseTime(i) :

        gender_factor = ge * .1 + .9
        age_factor = 1 + (0.02 * (a - 20))
        bmi_factor = ( w / h ** 2 ) <= 24.9
        weight_factor = bmi_factor * .9 + (1-bmi_factor) * 1.1
        above_avg_height =  h >= ( ge * 1.73 + (1-ge) * 1.6 )
        height_factor = above_avg_height * 1.1 + (1-above_avg_height) * .9

        goal_factor = go * .3 + .5
        level_factor = le * .3 + .5
        lifestyle_factor = li * .1 + .9

        number_of_exercises = 5 if len(exerciseList) > 5 else len(exerciseList)

        intensity_factor = (goal_factor * level_factor * lifestyle_factor) / (gender_factor * age_factor * height_factor * weight_factor)

        metList = eval(output.choices[0].message.content)
        if type(metList)==list :    intensity_factor = (intensity_factor + metList[i]) / 3.5

        time_per_exercise = (total_workout_time * intensity_factor) / number_of_exercises
        return f'{int(time_per_exercise)}mn, {int((time_per_exercise-int(time_per_exercise))*60)}s '

    workoutString = '"workoutPlan_id": 110,\n'
    workoutString += '"exercices": [\n'
    for i,k in zip(exerciseList,range(len(exerciseList))) :
        workoutString += '  {\n'
        workoutString += f'     "exercice_id": {k},\n'
        workoutString += f'     "isDone": false, \n'
        workoutString += f'     "name": "{i}",\n'
        workoutString += f'     "duration": "{exerciseTime(k)}",\n'
        workoutString += '  },\n'
        if k>5 : break;
    workoutString += ']'

    return workoutString

# feres1 = [22,0,1.67,71,1,2,0,20,0,1,1,0,1,0,0,0,0]
# feres1 = [22,1,1.90,90,3,2,1,10,0,0,0,0,0,0,0,0,0]
# print(makePrediction(feres1))
