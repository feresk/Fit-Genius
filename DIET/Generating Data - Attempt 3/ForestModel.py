
import pandas as pd
import numpy as np
import joblib
import pickle
import allGoodDiets as gd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier

from numba import jit,cuda

print('hi')

data = pd.read_csv("sorted_good_diet_data.csv")
data = data.dropna(axis=0)

def changedData(data):
    newData = data.copy(deep=True)
    newData['Diet_ID'] = newData['Diet_ID'].astype('int64')

    return newData

dietData = changedData(data).drop(['Diet'],axis=1)

print('oh...')

newData = dietData
feat = list(newData.columns)[:-1]
feat.remove('Goal')
target = list(newData.columns)[-1]
# scaler = StandardScaler()
# scaler.fit(newData.drop(['Diet_ID','Goal'],axis=1))

# features = pd.DataFrame(data=scaler.transform(newData.drop(['Diet_ID','Goal'],axis=1)), columns=feat)
features = pd.DataFrame(data=(newData.drop(['Diet_ID','Goal'],axis=1)), columns=feat)
print(features)
# pca = PCA(n_components=12)
# features = pca.fit_transform(features)
#
result =  newData[target]


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
with open('../DietModel.pkl', 'wb') as f:
    pickle.dump(finalModel, f)





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
