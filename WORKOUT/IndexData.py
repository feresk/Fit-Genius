
import pandas as pd
import numpy as np
import workoutDict as wd


data = pd.read_csv("final_fitness_data.csv")
data = data.dropna(axis=0)
print(data)

idlist = []
for i in range(data.shape[0]) :
    for j in wd.allWorkouts.keys() :
        if eval(data.Workout[i]) == wd.allWorkouts[j] :
             idlist.append(j)

data['Workout_ID'] = idlist
data.to_csv("indexed_final_fitness_data.csv", index=False)

# data = pd.read_csv("indexed_final_fitness_data.csv")
# data = data.dropna(axis=0)
# print(data.shape)
