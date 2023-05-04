
import numpy as np
import pandas as pd
from dietDict import *

def low(l) :
    res = []
    for i in l :
        res.append(i.lower())
    return res;

def uni(d1, d2) :
    res = {}
    for i in d1.keys() : res[i] = set()
    for i in d1.keys() :
        res[i] = set(low(d1[i])).union(set(low(d2[i])))
    return res

dict = uni(uni(uni(uni(uni(uni(uni(uni(uni(uni(uni(uni(uni(uni(uni(for_men , for_women ),for_old),for_obese),
        for_diabetes),for_hypertension),for_celiac),for_ibs),for_heart),for_kidney),for_lactose),
        for_gluten), for_fructose),for_histamine),for_fodmap),good_for_all);

for i in dict :
    print(i,':',dict[i])

print()
print(dict.values())

l = dict.values()
s = set()
for i in l :
    s = s.union(i)
print(len(s))
print(s)


food = ['oatmeal bread', 'gluten-free bread', 'coconut milk ice cream', 'oatmeal', 'chicken breast', 'brown rice', 'anise', 'kale', 'brown rice pasta', 'avocado', 'grapes', 'oregano', 'ginger', 'tomatoes', 'broccoli', 'cauliflower', 'amaranth', 'sorghum', 'sweet potato bread', 'spelt bread', 'coconut water', 'reduced-fat cheese', 'water with lemon and mint', 'olive oil', 'coriander', 'dandelion', 'rice', 'black beans', 'nuts', 'oat bread', 'barley', 'hard cheeses', 'cinnamon', 'chickpea pasta', 'lemon', 'cucumber', 'garlic', 'rice pasta', 'melons', 'fresh fruit', 'white pasta', 'white bread', 'strawberries', 'dark chocolate', 'bell peppers', 'nutmeg', 'unsweetened almond milk', 'tofu', 'hawthorn', 'eggplant', 'lactose-free yogurt', 'whole wheat tortillas', 'lentil pasta', 'zucchini noodles', 'whole grain bread', 'cardamom', 'quinoa pasta', 'zucchini', 'seeds', 'almond milk hot chocolate', 'white rice', 'pears', 'thyme', 'white tortillas', 'buckwheat', 'whole wheat pasta',
 'gluten-free muffins', 'almond milk', 'gluten-free pasta', 'skinless chicken breast', 'pinto beans', 'coffee', 'rye bread', 'butter', 'basil', 'whole wheat pita bread', 'cottage cheese', 'fruit-infused water', 'bulgur', 'plain yogurt', 'french bread', 'cranberries', 'hazelnuts', 'rice crackers', 'millet', 'oatmeal muffins', 'bananas', 'ghee', 'whole grain tortillas', 'corn', 'rye crispbread', 'fresh fruit smoothies', 'peppermint', 'blueberries', 'peaches', 'ezekiel bread', 'sweet potatoes', 'cumin', 'unsweetened tea', 'chia seeds', 'fruit smoothies', 'pita bread', 'kidney beans', 'greek yogurt', 'canola oil', 'sage', 'citrus fruits', 'kiwi', 'teff', 'milk', 'coconut milk', 'skinless chicken', 'potatoes', 'sourdough bread', 'turkey', 'cucumbers', 'chicken', 'almonds', 'flaxseeds', 'eggs', 'lentils', 'oats', 'lima beans', 'cheese', 'pineapple', 'herbal tea', 'lactose-free milk', 'chia seed pudding', 'mung beans', 'white bagels', 'plain greek yogurt', 'pistachios', 'walnuts', 'gluten-free baked goods', 'low-fat milk', 'grapefruit', 'lime', 'hemp seeds', 'fennel', 'turmeric', 'rosemary', 'cashew milk', 'mangoes', 'lactose-free cheese', 'chamomile', 'fenugreek', 'sweet potato', 'coconut oil', 'fish', 'sesame seeds', 'honey', 'chia pudding', 'prunes', 'water', 'sourdough pancakes', 'lean beef', 'spaghetti squash', 'sunflower seeds', 'celery', 'lettuce', 'plums', 'beef', 'squash', 'cabbage', 'carrots', 'coconut macaroons', 'turkey breast', 'lean cuts of beef', 'oranges', 'pumpkin seeds', 'chickpeas', 'green peas', 'almond milk latte', 'spinach', 'cashews', 'ice cream', 'leafy greens', 'coconut milk yogurt', 'soy milk', 'berries', 'couscous', 'gluten-free tortillas', 'whole wheat bread', 'gluten-free bagels', 'quinoa', 'lamb', 'sparkling water', 'yogurt with honey', 'yogurt', 'avocado oil', 'peppers', 'oat bran', 'white rolls', 'apples', 'fruit salad']

calories = [271, 253, 222, 389, 165, 111, 337, 49, 375, 160, 69, 265, 80, 18, 34, 25, 371, 339, 269, 261, 19, 106, 0, 884, 23, 365, 339, 347, 77, 246, 352, 247, 103, 370, 29, 15, 149, 352, 34, 57, 131, 265, 32, 546, 20, 525, 17, 76, 53, 25, 54, 256, 367, 17, 14, 236, 311, 17, 17, 26, 130, 57, 57, 85, 343, 92, 311, 17, 131, 165, 143, 0, 257, 717, 23, 275, 98, 0, 83, 63, 266, 46, 628, 389, 378, 376, 89, 900, 284, 86, 338, 50, 70, 57, 39, 217, 86, 375, 1, 486, 59, 275, 127, 97, 884, 315, 47, 61, 367, 42, 230, 165, 77, 216, 104, 16, 239, 579, 534, 155, 116, 389, 338, 402, 50, 1, 42, 140, 105, 266, 97, 557, 654, 255, 42, 37, 30, 526, 31, 312, 131, 230, 60, 407, 429, 7, 86, 862, 208, 222, 304, 383, 240, 0, 337, 165, 42, 578, 14, 34, 38, 25, 25, 23, 165, 31, 49, 138, 47, 559, 364, 81, 41, 23, 553, 207, 50, 77, 54, 57, 112, 235, 247, 260, 275, 258, 0, 146, 59, 884, 20, 246, 279, 57, 60]

protein = [9.5, 2.8, 2.5, 16.9, 31.0, 2.6, 17.6, 4.3, 8.1, 2.0, 0.7, 2.3, 0.9, 0.9, 2.8, 1.9, 13.6, 11.3, 4.4, 10.4, 0.72, 18.4, 0, 0.2, 2.7, 21.6, 21.4, 8.9, 10.7, 25.0, 3.4, 1.2, 3.4, 3.4, 1.1, 0.6, 6.4, 5.8, 0.8, 0.7, 5, 8.1, 0.7, 7.8, 0.9, 5.8, 0.5, 8, 1.3, 0.9, 4, 7.4, 27, 2.4, 1.5, 9.4, 13.1, 1.8, 1.4, 4.3, 1.2, 0.4, 0.4, 1.4, 13.3, 12.6, 3.3, 0.5, 5.5, 31, 9, 0.1, 6.8, 0.9, 3.2, 8.6, 11, 0, 3, 6, 8.8, 0.4, 14.1, 7.8, 11, 6.2, 1.1, 0, 7.6, 3.2, 9, 0.6, 0.5, 0.7, 0.9, 9.4, 1.6, 17.8, 0, 16.5, 0.6, 8.7, 9, 10, 0, 10.6, 0.9, 1.1, 13.3, 3.4, 2.3, 31, 1.6, 7.4, 25.8, 0.7, 27, 21.2, 18.3, 12.6, 9, 13.2, 15.6, 25.1, 0.5, 0, 3.4, 7.1, 7.1, 7.1, 20.6, 21.2, 20.3, 5.8, 3.4, 0.8, 0.7, 29.0, 1.2, 2.5, 1.1, 1.0, 0.6, 32.0, 3.7, 1.2, 2.1, 1.1, 26.0, 12.6, 0.3, 8.6, 1.2, 0.0, 7.0, 21.0, 1.2, 20.0, 1.1, 1.0, 0.9, 1.1, 0.9, 0.9, 31.0, 1.5, 6.0, 25.0, 0.9, 29.84, 19.3, 5.42, 0.61, 2.86, 18.22, 3.44, 3.3, 1.27, 3.3, 0.74, 3.79, 5.5, 9.27, 10.43, 4.43, 20.26, 0, 5.98, 3.98, 0.1, 0.99, 16.89, 8.4, 1.2, 0.4]

carbs = [46.3, 45.9, 26.8, 66.3, 0, 23.5, 50.02, 8.8, 75.5, 8.5, 18.1, 9.3, 18.8, 3.9, 6.6, 5.2, 65.25, 72.9, 51.6, 48.8, 3.71, 4.82, 0, 0, 15.1, 62.4, 43.8, 44.8, 54.5, 44.8, 74.9, 63.2, 67.6, 67.6, 9.3, 2.2, 33, 76, 8.3, 14, 25, 49, 8, 31, 6.3, 49, 0.6, 1.5, 12.3, 5.7, 5, 59, 63, 30, 2.7, 47, 59, 3.1, 3.1, 3.9, 25, 15, 15, 18, 71, 24, 55, 0.6, 25, 0, 27, 0, 47.5, 0.1, 2.7, 51.4, 3.4, 0, 18.6, 4.7, 49.2, 12.2, 17, 81.6, 73.9, 59.3, 22.8, 0, 49.6, 18.7, 62.9, 10.5, 14.5, 14.5, 9.5, 39, 20.1, 44.2, 0, 42.1, 14.3, 52.8, 22.8, 3.4, 0, 68.2, 11.3, 14.7, 73.9, 4.7, 6.3, 1.8, 17.1, 44.7, 0.6, 2.2, 0, 21.7, 28.9, 1.1, 63.4, 66.3, 63.4, 4.7, 13.1, 0, 4.5, 4.9, 4.3, 4.8, 28.1, 27.1, 13.7, 30.0, 4.7, 10.6, 10.1, 8.6, 15.7, 48.0, 6.6, 3.5, 14.7, 0.0, 56.3, 59.5, 21.4, 3.3, 0.0, 0.2, 82.4, 19.1, 58.0, 0.0, 45.7, 0.0, 10.9, 7.5, 2.2, 3.3, 9.5, 8.0, 11.7, 4.8, 0.0, 5.1, 5.6, 0.0, 11.75, 10.71, 61.01, 14.46, 3.52, 2.63, 30.19, 24.21, 4.03, 4.33, 4.12, 14.49, 23.22, 41.84, 47.04, 50.43, 57.13, 0, 0.04, 19.92, 3.56, 0.34, 4.91, 53.14, 49.2, 11.45, 15.32]

data = np.concatenate((np.array(food).reshape(-1,1), np.array(calories).reshape(-1,1), np.array(protein).reshape(-1,1), np.array(carbs).reshape(-1,1)),axis=1)
data = pd.DataFrame(data=data, columns=['Food','Calories','Protein','Carbs'])

data.to_csv('food_data.csv', index=False)
