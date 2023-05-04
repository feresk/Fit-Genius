import numpy as np
import random as rd
import pandas as pd
from workoutDict import dict,filter

medCond = {'None':-1,
        'Healthy':0,
        'Diabetes':1,
        'High_blood_pressure':2,
        'High_cholesterol':3,
        'Heart_disease':4,
        'Digestive_disorders':5,
        'Osteoporosis':6,
        'Arthritis':7,
        'COPD':8,
        'Stroke':9}

n=50000
age = [rd.randint(16,75) for i in range(n)]
gender = rd.choices([0,1],k=n)
weight = [rd.randint(40,120) for i in range(n)]
height = [rd.uniform(1.4,2) for i in range(n)]
level = rd.choices([1,3],k=n)
goal = rd.choices([1,3],k=n) #1 : yodh3of #2: yismin #3: muscles


age = np.array(age).reshape(-1,1)
gender = np.array(gender).reshape(-1,1)
weight = np.array(weight).reshape(-1,1)
height = np.array(height).reshape(-1,1)
level = np.array(level).reshape(-1,1)
goal = np.array(goal).reshape(-1,1)

bmi = weight / height ** 2 ;
# print(bmi)


data = np.concatenate((age,gender,height,weight,goal,level),axis=1)
data = pd.DataFrame(data=data, columns=['Age','Gender','Height','Weight','Goal','Level'])

for cond in list(medCond.keys())[2:] :
    globals()[cond.lower()] = np.array([np.random.choice([0,1], p=[0.8,0.2]) for i in range(n)]).reshape(-1,1)




# np.random.shuffle(age)
# np.random.shuffle(gender)
# np.random.shuffle(strength)
# np.random.shuffle(endurance)
# np.random.shuffle(flexibility)


target = [[] for i in range(n) ]

def inter(l1,l2) : return set(l1).intersection(l2)
def uni(l1,l2) : return set(l1).union(l2)

#print(inter(uni(filter['for_female'],filter['for_male&female'])-set(filter['not_for_diabetes']),set(filter['for_diabetes'])))


for i in range(n):
    if gender[i] == 0 :
        workout = uni(filter['for_female'],filter['for_male&female'])
        workout = uni(workout,filter['for_beginner'])
        workout = uni(workout,filter['for_advanced'])
        if age[i] < 60 :
            if bmi[i] < 30 :
                if goal[i] == 1 :
                    workout = inter(workout,filter['for_weight_loss'])
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    elif level[i] == 2 :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = uni(workout - set(filter['for_beginner']), filter['for_advanced'])
                        target[i] = (workout)
                else :
                    workout = inter(workout, uni(filter['for_muscle_gain'],filter['for_fit']))
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    elif level[i] == 2 :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = uni(workout - set(filter['for_beginner']), filter['for_advanced'])
                        target[i] = (workout)
            else :
                workout = inter(workout,filter['for_fat'])
                if goal[i] == 1 :
                    workout = inter(workout,filter['for_weight_loss'])
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    elif level[i] == 2 :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = uni(workout - set(filter['for_beginner']), filter['for_advanced'])
                        target[i] = (workout)
                elif goal[i] > 1  :
                    workout = inter(workout, uni(filter['for_muscle_gain'],filter['for_fit']))
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    elif level[i] == 2 :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = uni(workout - set(filter['for_beginner']), filter['for_advanced'])
                        target[i] = (workout)
        elif age[i] >= 60 :
            workout = (workout - set(filter['not_for_old'])) - set(filter['for_advanced'])
            if bmi[i] < 30 :
                if goal[i] == 1 :
                    workout = inter(workout,filter['for_weight_loss'])
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)
                else :
                    workout = inter(workout, uni(filter['for_muscle_gain'],filter['for_fit']))
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)
            else :
                workout = inter(workout,filter['for_fat'])
                if goal[i] == 1 :
                    workout = inter(workout,filter['for_weight_loss'])
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)
                else :
                    workout = inter(workout, uni(filter['for_muscle_gain'],filter['for_fit']))
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)
    elif gender[i] == 1 :
        workout = set(dict.keys())
        if age[i] < 60 :
            if bmi[i] < 30 :
                if goal[i] == 1 :
                    workout = inter(workout,filter['for_weight_loss'])
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    elif level[i] == 2 :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = uni(workout - set(filter['for_beginner']), filter['for_advanced'])
                        target[i] = (workout)
                else :
                    workout = inter(workout, uni(filter['for_muscle_gain'],filter['for_fit']))
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    elif level[i] == 2 :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = uni(workout - set(filter['for_beginner']), filter['for_advanced'])
                        target[i] = (workout)
            else :
                workout = inter(workout,filter['for_fat'])
                if goal[i] == 1 :
                    workout = inter(workout,filter['for_weight_loss'])
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    elif level[i] == 2 :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = uni(workout - set(filter['for_beginner']), filter['for_advanced'])
                        target[i] = (workout)
                elif goal[i] > 1 :
                    workout = inter(workout, uni(filter['for_muscle_gain'],filter['for_fit']))
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    elif level[i] == 2 :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = uni(workout - set(filter['for_beginner']), filter['for_advanced'])
                        target[i] = (workout)
        else :
            workout = (workout - set(filter['not_for_old'])) - set(filter['for_advanced'])
            if bmi[i] < 30 :
                if goal[i] == 1 :
                    workout = inter(workout,filter['for_weight_loss'])
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)
                else :
                    workout = inter(workout, uni(filter['for_muscle_gain'],filter['for_fit']))
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)
            else :
                workout = inter(workout,filter['for_fat'])
                if goal[i] == 1 :
                    workout = inter(workout,filter['for_weight_loss'])
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)
                else :
                    workout = inter(workout, uni(filter['for_muscle_gain'],filter['for_fit']))
                    if level[i] == 1 :
                        workout = inter(workout, filter['for_beginner'])
                        target[i] = (workout)
                    else :
                        workout = workout - set(filter['for_beginner'])
                        target[i] = (workout)

for i in range(n) :
    workout = target[i]
    if diabetes[i] == 1 :
        # workout = workout - set(filter['not_for_diabetes'])
        workout = inter(workout,filter['for_diabetes'])
        target[i] = (workout)
        if len(target[i]) == 0 :
            target[i] = set(filter['for_diabetes'])
    if high_blood_pressure[i] == 1 :
        workout = inter(workout,filter['for_hbp'])
        target[i] = (workout)
        if len(target[i]) == 0 :
            target[i] = set(filter['for_hbp'])
    if high_cholesterol[i] == 1 :
        workout = inter(workout,filter['for_cholesterol'])
        target[i] = (workout)
        if len(target[i]) == 0 :
            target[i] = set(filter['for_hbp'])
    if heart_disease[i] == 1 :
        workout = inter(workout,filter['for_heart'])
        target[i] = (workout)
        if len(target[i]) == 0 :
            target[i] = set(filter['for_heart'])
    if digestive_disorders[i] == 1 :
        workout = inter(workout,filter['for_digestive'])
        target[i] = (workout)
        if len(target[i]) == 0 :
            target[i] = set(filter['for_digestive'])
    if osteoporosis[i] == 1 :
        workout = inter(workout,filter['for_osteo'])
        target[i] = (workout)
        if len(target[i]) == 0 :
            target[i] = set(filter['for_osteo'])
    if arthritis[i] == 1 :
        workout = inter(workout,filter['for_arthritis'])
        target[i] = (workout)
        if len(target[i]) == 0 :
            target[i] = set(filter['for_arthritis'])
    if copd[i] == 1 :
        workout = inter(workout,filter['for_copd'])
        target[i] = (workout)
        if len(target[i]) == 0 :
            target[i] = set(filter['for_copd'])
    if stroke[i] == 1 :
        workout = inter(workout,filter['for_stroke'])
        target[i] = (workout)
        if len(target[i]) == 0 :
            target[i] = set(filter['for_stroke'])

k=1
for i in target :
    if not len(i) :
        print(data.iloc[k])
        print(bmi[k])
        print(i)
    k += 1

data = np.concatenate((age, gender, height, weight, goal, level, diabetes,
    high_blood_pressure, high_cholesterol, heart_disease, digestive_disorders,
    osteoporosis, arthritis, copd, stroke),axis=1)
data = pd.DataFrame(data=data, columns=['Age','Gender','Height','Weight','Goal','Level']+list(medCond.keys())[2:])

data['Workout'] = target
# data['Workout_ID'] =


print(data.head(12))

# data.to_csv('final_fitness_data.csv', index=False)

d={}
k = 0
for i in data.Workout.value_counts().index :
    d[k] = i
    k += 1

for i in d.keys():
    print(f"'{i}' : {d[i]}',")


# for i in range(n) :
#     workout = target[i]
#     if diabetes[i] == 1 :
#




# MAKING DICTIONARY
# d={}
# k=0
# for i in data.Workout.value_counts().index :
#     d[i] = k
#     k += 1
#
# for i in d.keys():
#     print(f"'{i}' : {d[i]},")
