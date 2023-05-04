
import numpy as np
import pandas as pd
import dietDict as d
import random as rd


def low(l) :
    res = []
    for i in l :
        res.append(i.lower())
    return res;

def uni(d1, d2) :
    res = {}
    for i in d1.keys() : res[i] = set()
    for i in d1.keys() :
        if i in d2.keys() : res[i] = set(low(d1[i])).union(set(low(d2[i])))
        else : res[i] = set(low(d1[i]))
    return res

def inter(d1, d2) :
    res = {}
    for i in d1.keys() : res[i] = set()
    for i in d1.keys() :
        if i in d2.keys() :
            res[i] = set(low(d1[i])).intersection(set(low(d2[i])))
            if len(res[i]) == 0 : res[i] = set(low(d2[i]))
        else : res[i] = set(low(d1[i]))
    return res

def minus(d1, d2) :
    res = {}
    for i in d1.keys() : res[i] = set()
    for i in d1.keys() :
        if i in d2.keys() : res[i] = set(low(d1[i])) - (set(low(d2[i])))
        else : res[i] = set(low(d1[i]))
    return res

medCond = {
    'Diabetes': 0,
    'Hypertension': 1,
    'Celiac_disease': 2,
    'Irritable_bowel_syndrome': 3,
    'Heart_disease': 4,
    'Kidney_disease': 5,
    'Lactose_intolerance': 6,
    'Gluten_intolerance': 7,
    'Fructose_intolerance': 8,
    'Histamine_intolerance': 9,
    'FODMAP_intolerance': 10,
    'Peanut_allergy': 11,
    'Tree_nut_allergy': 12,
    'Shellfish_allergy': 13,
    'Fish_allergy': 14,
    'Egg_allergy': 15,
    'Milk_allergy': 16,
    'Soy_allergy': 17,
    'Wheat_allergy': 18,
}

n=150000
age = [rd.randint(16,75) for i in range(n)]
gender = rd.choices([0,1],k=n)
weight = [rd.randint(40,120) for i in range(n)]
height = [rd.uniform(1.4,2) for i in range(n)]
goal = rd.choices([1,3],k=n)


age = np.array(age).reshape(-1,1)
gender = np.array(gender).reshape(-1,1)
weight = np.array(weight).reshape(-1,1)
height = np.array(height).reshape(-1,1)
goal = np.array(goal).reshape(-1,1)

bmi = weight / height ** 2 ;
# print(bmi)

data = np.concatenate((age,gender,height,weight,goal),axis=1)
data = pd.DataFrame(data=data, columns=['Age','Gender','Height','Weight','Goal'])

for cond in list(medCond.keys()) :
    globals()[cond.lower()] = np.array([np.random.choice([0,1], p=[0.8,0.2]) for i in range(n)]).reshape(-1,1)

data = np.concatenate((age, gender, height, weight, goal, diabetes,
    hypertension, celiac_disease, irritable_bowel_syndrome, heart_disease,
    kidney_disease, lactose_intolerance, gluten_intolerance,
    fructose_intolerance, histamine_intolerance, fodmap_intolerance,
    peanut_allergy, tree_nut_allergy, shellfish_allergy, fish_allergy,
    egg_allergy, milk_allergy, soy_allergy, wheat_allergy),axis=1)
data = pd.DataFrame(data=data, columns=['Age','Gender','Height','Weight','Goal']+list(medCond.keys()))

target = [[] for i in range(n) ]
#
diet = d.good_for_all
for i in range(n) :
    if gender[i] == 0 :
        diet = uni(diet,d.for_women)
        if age[i] < 65 :
            if bmi[i] < 30 :
                target[i] = diet
            else :
                diet = inter(diet,d.for_obese)
                target[i] = diet
        elif age[i] >= 65 :
            diet = inter(diet,d.for_old)
            if bmi[i] < 30 :
                target[i] = diet
            else :
                diet = inter(diet,d.for_obese)
                target[i] = diet
    elif gender[i] == 1 :
        diet = uni(diet,d.for_men)
        if age[i] < 65 :
            if bmi[i] < 30 :
                target[i] = diet
            else :
                diet = inter(diet,d.for_obese)
                target[i] = diet
        elif age[i] >= 65 :
            diet = inter(diet,d.for_old)
            if bmi[i] < 30 :
                target[i] = diet
            else :
                diet = inter(diet,d.for_obese)
                target[i] = diet

# age, gender, height, weight, goal, diabetes,
# hypertension, celiac_disease, irritable_bowel_syndrome, heart_disease,
# kidney_disease, lactose_intolerance, gluten_intolerance,
# fructose_intolerance, histamine_intolerance, fodmap_intolerance,
# peanut_allergy, tree_nut_allergy, shellfish_allergy, fish_allergy,
# egg_allergy, milk_allergy, soy_allergy, wheat_allergy

for i in range(n) :
    diet = target[i]
    if diabetes[i] == 1 :
        diet = inter(diet,d.for_diabetes)
        target[i] = diet
        #if len(target[i]) == 0 : target[i] = d.for_diabetes
    if hypertension[i] == 1 :
        diet = inter(diet,d.for_hypertension)
        target[i] = diet
        #if len(target[i]) == 0 : target[i] = d.for_hypertension
    if celiac_disease[i] == 1 :
        diet = inter(diet, d.for_celiac)
        target[i] = diet
        #if len(target[i]) == 0 : target[i] = d.for_celiac
    if irritable_bowel_syndrome[i] == 1 :
        diet = inter(diet,d.for_ibs)
        target[i] = diet
        #if len(target[i]) == 0 : target[i] = d.for_ibs
    if heart_disease[i] == 1 :
        diet = inter(diet, d.for_heart)
        target[i] = diet
        #if len(target[i]) == 0 : target[i] = d.for_heart
    if kidney_disease[i] == 1 :
        diet = inter(diet,d.for_kidney )
        target[i] = diet
        #if len(target[i]) == 0 : target[i] = d.for_kidney
    if lactose_intolerance[i] == 1 :
        diet = inter(diet,d.for_lactose)
        target[i] = diet
        #if len(target[i]) == 0 : target[i] = d.for_lactose
    if gluten_intolerance[i] == 1 :
        diet = inter(diet,d.for_gluten)
        target[i] = diet
        #if len(target[i]) == 0 : target[i] = d.for_gluten
    if fructose_intolerance[i] == 1 :
        diet = inter(diet,d.for_fructose)
        target[i] = diet
        #if len(target[i]) == 0 : target[i] = d.for_fructose
    if histamine_intolerance[i] == 1 :
        diet = inter(diet,d.for_histamine)
        target[i] = diet
        #if len(target[i]) == 0 : target[i] = d.for_histamine
    if fodmap_intolerance[i] == 1 :
        diet = inter(diet,d.for_fodmap)
        target[i] = diet
        #if len(target[i]) == 0 : target[i] = d.for_fodmap
######
    if peanut_allergy[i] == 1 :
        diet = minus(diet,d.not_for_peanut_allergy)
        target[i] = diet
    if tree_nut_allergy[i] == 1 :
        diet = minus(diet,d.not_for_tree_nut_allergy)
        target[i] = diet
    if shellfish_allergy[i] == 1 :
        diet = minus(diet,d.not_for_shellfish_allergy)
        target[i] = diet
    if fish_allergy[i] == 1 :
        diet = minus(diet,d.not_for_fish_allergy)
        target[i] = diet
    if egg_allergy[i] == 1 :
        diet = minus(diet,d.not_for_egg_allergy)
        target[i] = diet
    if milk_allergy[i] == 1 :
        diet = minus(diet,d.not_for_milk_allergy)
        target[i] = diet
    if soy_allergy[i] == 1 :
        diet = minus(diet,d.not_for_soy_allergy)
        target[i] = diet
    if wheat_allergy[i] == 1 :
        diet = minus(diet,d.not_for_wheat_allergy)
        target[i] = diet


data['Diet'] = target
diet_data = pd.DataFrame(data=data.Diet.value_counts().index, columns=['Diet'])

data.to_csv('good_diet_data.csv', index=False)
diet_data.to_csv('diet_lists.csv', index=False)


dt={}
k = 0
for i in data.Diet.value_counts().index :
    dt[k] = i
    k += 1

f = 'all_good_diets = {\n'
for i in dt.keys():
    f += f"{i} : {dt[i]},\n"
f += '}'
with open("allGoodDiets.py","w") as file :
    file.write(f)

print('Done')
