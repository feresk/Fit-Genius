
import numpy as np
import pandas as pd
import random as rd


data = pd.read_csv("sorted_good_diet_data.csv")
print(data.Diet_ID.value_counts().index.shape)
print(data['Diet_ID'].isna().sum())
data = data.dropna(axis=0)
print(data.shape)
#
# data = pd.read_csv("good_diet_data.csv")
# unique_diets = pd.read_csv("diet_lists.csv")
#
# unique_diets['Diet_ID'] = unique_diets.index
#
#
# for i in range(unique_diets.Diet.shape[0]) :
#     unique_diets.Diet[i] = str(dict(sorted(eval(unique_diets.Diet[i]).items(), key=lambda x:x[1])))
#
# for i in range(data.Diet.shape[0]) :
#     data.Diet[i] = str(dict(sorted(eval(data.Diet[i]).items(), key=lambda x:x[1])))
#
#
# data = data.join(unique_diets.set_index("Diet"), on='Diet')
#
# print(data)
# print(data['Diet_ID'].isna().sum())
#
# data.to_csv("sorted_good_diet_data.csv",index=False)
