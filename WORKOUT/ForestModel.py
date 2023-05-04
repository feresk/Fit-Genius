
import pandas as pd
import numpy as np
import joblib
import pickle
import workoutDict as wd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
# from sklearn.ensemble import ExtraTreesClassifier
# from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier

from numba import jit,cuda



data = pd.read_csv("indexed_final_fitness_data.csv")
data = data.dropna(axis=0)
# print(data)

def changedData(data):
    newData = data.copy(deep=True)
    for i in range(data.shape[0]):
        newData['Workout_ID'] = newData['Workout_ID'].astype('int64')

    return newData

workoutData = changedData(data).drop(['Workout'],axis=1)

newData = changedData(workoutData)
feat = list(newData.columns)[:-1]
print(feat)
target = list(newData.columns)[-1]

# scaler = StandardScaler()
# scaler.fit(newData.drop(['Workout_ID'],axis=1))
# features = pd.DataFrame(data=scaler.transform(newData.drop(['Workout_ID'],axis=1)), columns=feat)

features = pd.DataFrame(data=newData.drop(['Workout_ID'],axis=1), columns=feat)

result =  newData[target]
print(features)
# @jit(target_backend='cuda')
print("Model Starting...")
def Model(classifier, ne=20, md=15, rd= 42,) :
    xTrain, xTest, yTrain, yTest = train_test_split(features, result, test_size=.2, random_state=rd)
    # clf = classifier(n_estimators=ne, max_depth=md)
    clf = classifier()
    clf.fit(xTrain, yTrain)
    y_pred = clf.predict(xTest)
    accuracy = accuracy_score(yTest, y_pred)
    print("Accuracy:", accuracy)
    # print('R² Training Data: ', clf.score(xTrain,yTrain))
    # print('R² Test Data: ', clf.score(xTest,yTest))
    return clf

finalModel = Model(DecisionTreeClassifier)
with open('./WorkoutModel.pkl', 'wb') as f:
    pickle.dump(finalModel, f)

# joblib.dump(finalModel, "./WorkoutModel.joblib")

# finalModel = Model(RandomForestClassifier,  20)



# def makePrediction(featureList) :
#     featureList.pop(4)
#     featureList = np.array(featureList).reshape(1,-1)
#     diet = gd.all_good_diets[finalModel.predict(featureList)[0]]
#     print(f'Your Diet Plan is :')
#     for i in diet :
#         print(i,':',diet[i])
#
# person = [22,0,1.90,85,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# # makePrediction(person)
