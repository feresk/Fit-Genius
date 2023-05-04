
disease_dict = {
    'diabetes': 0,
    'hypertension': 1,
    'celiac_disease': 2,
    'irritable_bowel_syndrome': 3,
    'heart_disease': 4,
    'kidney_disease': 5,
    'Lactose_intolerance': 6,
    'Gluten_intolerance': 7,
    'Fructose_intolerance': 8,
    'Histamine_intolerance': 9,
    'FODMAP_intolerance': 10
}

allergy_dict = {
    'Peanut_allergy': 0,
    'Tree_nut_allergy': 1,
    'Shellfish_allergy': 2,
    'Fish_allergy': 3,
    'Egg_allergy': 4,
    'Milk_allergy': 5,
    'Soy_allergy': 6,
    'Wheat_allergy': 7,
}



food_categories_extended = ['Baking Ingredients', 'Cakes & Pies', 'Herbs & Spices', 'Beer',
       'Candy & Sweets', 'Pastries, Breads & Rolls', 'Dishes & Meals',
       'Oatmeal, Muesli & Cereals', 'Fast Food', 'Vegetables', 'Legumes',
       'Fish & Seafood', 'Sauces & Dressings', 'Fruits', 'Cheese', 'Soups',
       'Non-Alcoholic Drinks & Beverages', 'Alcoholic Drinks & Beverages',
       'Sausage', 'Fruit Juices', 'Meat', 'Soda & Soft Drinks', 'Ice Cream',
       'Cereal Products', 'Pizza', 'Pasta & Noodles', 'Yogurt', 'Nuts & Seeds',
       'Spreads', 'Pork', 'Potato Products', 'Wine', 'Beef & Veal',
       'Tropical & Exotic Fruits', 'Venison & Game', 'Cold Cuts & Lunch Meat',
       'Sliced Cheese', 'Offal & Giblets', 'Vegetable Oils',
       'Milk, Dairy Products & Eggs', 'Poultry & Fowl', 'Oils & Fats',
       'Canned Fruit', 'Cream Cheese'],

food_categories = ['Pastries, Breads & Rolls', 'Vegetables', 'Fruits', 'Whole Grains', 'Milk, Dairy Products & Eggs', 'Meat', 'Pasta', 'Oils & Fats']

not_for_obese = {
    'Pastries, Breads & Rolls': ['white bread', 'croissants', 'doughnuts', 'white bread', 'bagels', 'muffins'],
    'Vegetables': ['canned vegetables with added salt', 'fried vegetables', 'creamed vegetables', 'potatoes'],
    'Fruits': ['dried fruits with added sugar', 'canned fruits with added sugar', 'fruit juice with added sugar', 'sweetened fruit yogurt'],
    'Whole Grains': ['white rice'],
    'Milk, Dairy Products & Eggs': ['whole milk', 'full-fat cheese', 'butter', 'heavy cream'],
    'Meat': ['processed mea ts', 'fatty cuts of red meat', 'sausages', 'bacon'],
    'Pasta': ['white pasta', 'ramen noodles', 'instant noodles'],
    'Legumes': ['baked beans with added sugar', 'refried beans with added lard', 'fried tofu'],
    'Nuts & Seeds': ['honey-roasted nuts', 'candied nuts', 'trail mix with added sugar'],
    'Oils & Fats': ['lard', 'shortening', 'trans fats', 'mayonnaise'],
    'Herbs & Spices': ['salt', 'sugar', 'ketchup', 'barbecue sauce', 'sweet chili sauce'],
    'Sweets & Drinks': ['soda', 'energy drinks', 'sweetened coffee drinks', 'sweetened tea', 'milkshakes', 'ice cream', 'cake', 'cookies', 'candy']
}
not_for_diabetes = {
    'Pastries, Breads & Rolls': ['sweet potato bread','white bread', 'white rice'],
    'Vegetables': ['potatoes', 'sweet potatos'],
    'Sweets & Drinks' : ['sugar', 'sweets'],
}
not_for_hypertension = {
    'Vegetables': ['canned vegetables'],
    'Meat' : ['red meat'],
    'Legumes': ['canned beans'],
    'Herbs & Spices': ['salt'],
    'Sweets & Drinks' : ['soda','processed foods'],
}
not_for_celiac = {
    'Pastries, Breads & Rolls' : ['wheat', 'whole wheat bread', 'bread', 'crackers',
            'cabbage', 'cauliflower', 'collard greens', 'oatmeal bread'],
    'Pasta' : ['white pasta', 'whole wheat pasta'],
    'Whole Grains' : ['rye', 'oats', 'barley'],
}
not_for_ibs = {
    'Vegetables' : ['arugula', 'bok choy', 'broccoli', 'brussels sprouts'],
    'Milk, Dairy Products & Eggs': ['milk','whole milk', 'Low-fat milk', 'cheese','Full-fat cheese',
            'cottage cheese', 'butter', 'yogurt', 'ice cream', 'plain Greek yogurt', 'Full-fat cheese',
            'hard cheeses', 'ice cream', 'lactose-free milk', 'Lactose-free yogurt', 'Lactose-free cheese'],
    'Legumes': ['beans'],
    'Sweets & Drinks' : ['alcohol'],
}
not_for_heart = {
    'Pastries, Breads & Rolls': ['trans fat pastries'],
    'Milk, Dairy Products & Eggs': ['Full-fat cheese', 'butter', 'Full-fat cheese', 'cured meats'],
    'Meat' : ['processed meats', 'fatty cuts of meat', 'sausages', 'bacon'],
    'Oils & Fats' : ['coconut oil', 'plam oil', 'ghee'],
    'Sweets & Drinks' : ['trans fat sweets', 'cakes', 'biscuits'],
    },
not_for_kidney = {
    'Pastries, Breads & Rolls': ['processed breads'],
    'Milk, Dairy Products & Eggs': ['milk','whole milk', 'Low-fat milk', 'cheese','Full-fat cheese',
            'cottage cheese', 'butter', 'yogurt', 'ice cream', 'plain Greek yogurt', 'Full-fat cheese',
            'hard cheeses', 'ice cream' ],
    'Meat' : ['red meat'],
    'Herbs & Spices': ['salt'],
    'Sweets & Drinks' : ['soda','processed foods'],
}
not_for_peanut_allergy = {
    'Nuts & Seeds' : ['peanuts'],
    'Oils & Fats' : ['peanut butter', 'peanut oil'],
}
not_for_tree_nut_allergy = {
    'Nuts & Seeds' : ['almonds', 'cashews', 'walnuts', 'hazelnuts', 'macadamia nuts']
}
not_for_shellfish_allergy = {
    'Meat' : ['shrimp', 'lobster', 'crab', 'clams', 'mussels', 'oysters'],
}
not_for_fish_allergy = {
    'Meat' : ['fish', 'salmon', 'tuna', 'cod', 'trout', 'tilapia', 'haddock'],
}
not_for_egg_allergy = {
    'Milk, Dairy Products & Eggs': ['eggs', 'mayonnaise'],
}
not_for_milk_allergy = {
    'Milk, Dairy Products & Eggs': ['milk','whole milk', 'Low-fat milk', 'cheese','Full-fat cheese',
            'cottage cheese', 'butter', 'yogurt', 'ice cream', 'plain Greek yogurt', 'Full-fat cheese',
            'hard cheeses', 'ice cream', 'lactose-free milk', 'Lactose-free yogurt', 'Lactose-free cheese'],
}
not_for_soy_allergy = {
    'Milk, Dairy Products & Eggs': ['soy milk'],
    'Meat' : ['tofu'],
    'Legumes' : ['soybeans'],
    'Herbs & Spices' : ['soy sauce'],
}
not_for_wheat_allergy = {
    'Pastries, Breads & Rolls' : ['wheat', 'whole wheat bread', 'bread', 'crackers'],
    'Pasta' : ['white pasta', 'whole wheat pasta'],
}
not_for_lactose = {
    'Milk, Dairy Products & Eggs': ['milk','whole milk', 'Low-fat milk', 'cheese','Full-fat cheese',
            'cottage cheese', 'butter', 'yogurt', 'ice cream', 'plain Greek yogurt', 'Full-fat cheese',
            'hard cheeses', 'ice cream' ],
}
not_for_gluten = {
    'Pastries, Breads & Rolls' : ['wheat', 'whole wheat bread', 'bread', 'crackers', 'oatmeal bread'],
    'Pasta' : ['white pasta', 'whole wheat pasta'],
    'Whole Grains' : ['rye', 'oats', 'barley'],
}
not_for_fructose = {
    'Sweets & Drinks' : ['fruit juice', 'honey', 'agave nectar', 'high fructose corn syrup'],
    },
not_for_histamine = {
    'Pastries, Breads & Rolls'  : ['fermented breads', 'sourdough bread'],
    'Milk, Dairy Products & Eggs': ['aged cheeses'],
    'Meat' : ['smoked meats'],
    'Sweets & Drinks' : ['alcohol'],
}
not_for_fodmap = {
    'Pastries, Breads & Rolls' : ['wheat', 'whole wheat bread', 'bread', 'crackers'],
    'Vegetables' : ['garlic', 'onion'],
    'Fruits' : ['apples', 'peaches', 'watermelon'],
    'Pasta' : ['White pasta', 'whole wheat pasta'],
}

alternatives_dict = {
    'Peanut_allergy': ['almonds', 'cashews', 'walnuts', 'hazelnuts', 'macadamia nuts'],
    'Tree_nut_allergy': ['pumpkin seeds', 'sunflower seeds', 'chia seeds', 'flaxseeds', 'sesame seeds'],
    'Shellfish_allergy': ['chicken', 'turkey', 'beef', 'tofu'],
    'Fish_allergy': ['chicken', 'turkey', 'beef', 'tofu'],
    'Egg_allergy': ['flaxseed', 'chia seeds', 'applesauce', 'silken tofu', 'vinegar'],
    'Milk_allergy': ['almond milk', 'soy milk', 'coconut milk', 'rice milk', 'oat milk'],
    'Soy_allergy': ['lentils', 'chickpeas', 'black beans', 'quinoa', 'tempeh'],
    'Wheat_allergy': ['gluten-free whole grains', 'fruits', 'vegetables', 'lean protein', 'healthy fats'],
}


for_men = {
        'Pastries, Breads & Rolls': ['whole wheat bread', 'whole grain tortillas', 'oatmeal'],
        'Vegetables': ['spinach', 'broccoli', 'kale', 'carrots', 'peppers'],
        'Fruits': ['berries', 'oranges', 'apples', 'bananas', 'mangoes'],
        'Whole Grains': ['whole wheat bread', 'brown rice', 'oatmeal'],
        'Milk, Dairy Products & Eggs': ['low-fat milk', 'plain Greek yogurt', 'cottage cheese', 'eggs'],
        'Meat': ['chicken breast', 'turkey breast', 'fish', 'lean beef'],
        'Pasta': ['whole wheat pasta', 'brown rice pasta', 'quinoa pasta'],
        'Legumes': ['lentils', 'chickpeas', 'black beans', 'mung beans', 'green peas'],
        'Nuts & Seeds': ['almonds', 'walnuts', 'cashews', 'pumpkin seeds', 'chia seeds'],
        'Oils & Fats': ['olive oil', 'avocado', 'nuts', 'seeds'],
        'Herbs & Spices': ['basil', 'garlic','oregano', 'cumin', 'turmeric', 'ginger'],
        'Sweets & Drinks' : ['dark chocolate', 'unsweetened tea', 'coffee', 'honey'],
    }

for_women = {
        'Pastries, Breads & Rolls': ['whole wheat bread', 'whole grain tortillas', 'oatmeal'],
        'Vegetables': ['spinach', 'broccoli', 'kale', 'carrots', 'tomatoes'],
        'Fruits': ['berries', 'oranges', 'apples', 'bananas', 'grapefruit'],
        'Whole Grains': ['whole wheat bread', 'brown rice', 'oatmeal'],
        'Milk, Dairy Products & Eggs': ['low-fat milk', 'plain Greek yogurt', 'cottage cheese', 'eggs'],
        'Meat': ['chicken breast', 'turkey breast', 'fish', 'tofu', 'lean beef'],
        'Pasta': ['whole wheat pasta', 'brown rice pasta', 'quinoa pasta'],
        'Legumes': ['lentils', 'chickpeas', 'black beans', 'mung beans', 'green peas'],
        'Nuts & Seeds': ['almonds', 'walnuts', 'cashews', 'pumpkin seeds', 'chia seeds'],
        'Oils & Fats': ['olive oil', 'avocado', 'nuts', 'seeds'],
        'Herbs & Spices': ['basil', 'oregano', 'cumin', 'turmeric', 'ginger', 'garlic'],
        'Sweets & Drinks' : ['dark chocolate', 'herbal tea', 'coffee', 'honey'],
    }

for_old = {
        'Pastries, Breads & Rolls': ['whole wheat bread', 'whole grain tortillas', 'oatmeal'],
        'Vegetables': ['spinach', 'broccoli', 'kale', 'carrots', 'peppers', 'sweet potatoes'],
        'Fruits': ['berries', 'oranges', 'apples', 'bananas', 'grapefruit', 'prunes'],
        'Whole Grains': ['whole wheat bread', 'brown rice', 'oatmeal', 'barley'],
        'Milk, Dairy Products & Eggs': ['low-fat milk', 'plain Greek yogurt', 'cottage cheese', 'eggs'],
        'Meat': ['chicken breast', 'turkey breast', 'fish', 'lean beef'],
        'Pasta': ['whole wheat pasta', 'brown rice pasta', 'quinoa pasta'],
        'Legumes': ['lentils', 'kidney beans', 'pinto beans', 'mung beans', 'flaxseeds'],
        'Nuts & Seeds': ['almonds', 'walnuts', 'pistachios', 'chia seeds', 'flaxseeds'],
        'Oils & Fats': ['olive oil', 'avocado', 'nuts', 'seeds'],
        'Herbs & Spices': ['basil', 'oregano', 'cumin', 'turmeric', 'ginger', 'garlic'],
        'Sweets & Drinks' : ['yogurt with honey', 'coconut water', 'herbal tea', 'coffee', 'honey']
    }


not_for_men = {
    'Pastries, Breads & Rolls': ['White bread', 'Croissants', 'Doughnuts', 'Danish pastries', 'Cinnamon rolls'],
    'Vegetables': ['Canned vegetables with added sodium', 'Creamed or cheesy vegetables', 'Fried vegetables'],
    'Fruits': ['Canned fruits in syrup', 'Fruit juice with added sugar'],
    'Whole Grains': ['Refined grains like white rice or white pasta'],
    'Milk, Dairy Products & Eggs': ['Full-fat cheese', 'Whole milk', 'Fried eggs with added cheese or meat'],
    'Meat': ['Bacon', 'Sausage', 'Deli meats', 'High-fat red meats'],
    'Pasta': ['Pasta with cream sauce', 'Pasta with heavy meat sauce', 'Refined pasta'],
    'Legumes': ['Lima beans', 'Red kidney beans', 'Navy beans', 'Baked beans'],
    'Nuts & Seeds': ['Candied nuts', 'Honey-roasted nuts', 'Salted nuts'],
    'Oils & Fats': ['Trans fats found in processed foods']
}
not_for_women = {
    'Pastries, Breads & Rolls': ['White bread', 'Croissants', 'Doughnuts', 'Danish pastries', 'Cinnamon rolls'],
    'Vegetables': ['Canned vegetables with added sodium', 'Creamed or cheesy vegetables', 'Fried vegetables'],
    'Fruits': ['Canned fruits in syrup', 'Fruit juice with added sugar'],
    'Whole Grains': ['Refined grains like white rice or white pasta'],
    'Milk, Dairy Products & Eggs': ['Full-fat cheese', 'Whole milk', 'Fried eggs with added cheese or meat'],
    'Meat': ['Bacon', 'Sausage', 'Deli meats', 'High-fat red meats'],
    'Pasta': ['Pasta with cream sauce', 'Pasta with heavy meat sauce', 'Refined pasta'],
    'Legumes': ['Lima beans', 'Red kidney beans', 'Navy beans', 'Baked beans'],
    'Nuts & Seeds': ['Candied nuts', 'Honey-roasted nuts', 'Salted nuts'],
    'Oils & Fats': ['Trans fats found in processed foods']
}
not_for_old = {
    'Pastries, Breads & Rolls': ['White bread', 'Croissants', 'Doughnuts', 'Danish pastries', 'Cinnamon rolls'],
    'Vegetables': ['Canned vegetables with added sodium', 'Creamed or cheesy vegetables', 'Fried vegetables'],
    'Fruits': ['Canned fruits in syrup', 'Fruit juice with added sugar'],
    'Whole Grains': ['Refined grains like white rice or white pasta'],
    'Milk, Dairy Products & Eggs': ['Full-fat cheese', 'Whole milk', 'Fried eggs with added cheese or meat'],
    'Meat': ['Bacon', 'Sausage', 'Deli meats', 'High-fat red meats'],
    'Pasta': ['Pasta with cream sauce', 'Pasta with heavy meat sauce', 'Refined pasta'],
    'Legumes': ['Lima beans', 'Red kidney beans', 'Navy beans', 'Baked beans'],
    'Nuts & Seeds': ['Salted nuts', 'Sugared nuts, Candied nuts'],
    'Oils & Fats': ['Trans fats found in processed foods']
}


for_obese = {
    'Pastries, Breads & Rolls': ['whole wheat bread', 'whole grain tortillas', 'oatmeal'],
    'Vegetables': ['spinach', 'broccoli', 'kale', 'carrots', 'bell peppers', 'cucumbers'],
    'Fruits': ['berries', 'oranges', 'apples', 'pears', 'kiwi', 'grapefruit'],
    'Whole Grains': ['quinoa', 'brown rice', 'barley', 'millet', 'oat bran'],
    'Milk, Dairy Products & Eggs': ['low-fat milk', 'plain Greek yogurt', 'cottage cheese', 'eggs', 'reduced-fat cheese'],
    'Meat': ['chicken breast', 'turkey breast', 'fish', 'lean beef'],
    'Pasta': ['whole wheat pasta', 'brown rice pasta', 'quinoa pasta', 'zucchini noodles'],
    'Legumes': ['lentils', 'chickpeas', 'black beans', 'mung beans', 'green peas'],
    'Nuts & Seeds': ['almonds', 'walnuts', 'pistachios', 'chia seeds', 'flaxseeds'],
    'Oils & Fats': ['olive oil', 'avocado oil', 'nuts', 'seeds'],
    'Herbs & Spices': ['cinnamon', 'turmeric', 'ginger', 'garlic', 'oregano', 'cumin'],
    'Sweets & Drinks': ['water', 'unsweetened tea', 'coffee', 'sparkling water']
}
for_diabetes = {
    'Pastries, Breads & Rolls': ['whole wheat bread', 'whole grain tortillas', 'oatmeal'],
    'Vegetables': ['spinach', 'broccoli', 'kale'],
    'Fruits': ['berries', 'oranges', 'apples', 'lemon', 'lime'],
    'Whole Grains': ['quinoa', 'brown rice', 'bulgur'],
    'Milk, Dairy Products & Eggs': ['low-fat milk', 'plain Greek yogurt', 'cottage cheese', 'eggs'],
    'Meat': ['chicken breast', 'turkey breast', 'fish'],
    'Pasta': ['whole wheat pasta', 'brown rice pasta', 'quinoa pasta'],
    'Legumes' : ['mung beans', 'green peas'],
    'Nuts & Seeds' : ['almonds', 'walnuts', 'pistachios', 'chia seeds', 'flaxseeds'],
    'Oils & Fats' : ['olive oil', 'avocado oil', 'coconut oil', 'nuts'],
    'Herbs & Spices': ['cinnamon', 'turmeric', 'ginger', 'fenugreek', 'garlic', 'oregano'],
    'Sweets & Drinks' : ['dark chocolate', 'unsweetened tea'],
}
for_hypertension = {
    'Pastries, Breads & Rolls': ['whole grain bread', 'whole wheat tortillas', 'pita bread'],
    'Vegetables': ['leafy greens', 'tomatoes', 'cucumber'],
    'Fruits': ['berries', 'bananas', 'apples'],
    'Whole Grains': ['brown rice', 'quinoa', 'oats'],
    'Milk, Dairy Products & Eggs': ['low-fat milk', 'plain Greek yogurt', 'cottage cheese', 'eggs'],
    'Meat': ['chicken breast', 'fish', 'tofu'],
    'Pasta': ['whole wheat pasta', 'brown rice pasta', 'quinoa pasta'],
    'Legumes' : ['kidney beans', 'lima beans'],
    'Nuts & Seeds' : ['pumpkin seeds', 'sunflower seeds', 'almonds', 'pistachios', 'walnuts'],
    'Oils & Fats' : ['olive oil', 'avocado oil', 'coconut oil', 'nuts'],
    'Herbs & Spices': ['garlic', 'turmeric', 'ginger', 'cinnamon', 'hawthorn', 'basil'],
    'Sweets & Drinks' : ['water', 'unsweetened tea', 'coffee'],
}
for_celiac = {
    'Pastries, Breads & Rolls': ['gluten-free bread', 'rice crackers', 'gluten-free tortillas'],
    'Vegetables': ['spinach', 'tomatoes', 'bell peppers'],
    'Fruits': ['apples', 'bananas', 'oranges'],
    'Whole Grains': ['rice', 'quinoa', 'buckwheat'],
    'Milk, Dairy Products & Eggs': ['almond milk', 'coconut milk yogurt', 'hard cheeses', 'eggs'],
    'Meat': ['chicken', 'fish', 'tofu'],
    'Pasta': ['gluten-free pasta', 'zucchini noodles', 'spaghetti squash'],
    'Legumes' : ['kidney beans', 'lima beans'],
    'Nuts & Seeds' : ['chia seeds', 'flaxseeds', 'sesame seeds', 'pumpkin seeds', 'sunflower seeds'],
    'Oils & Fats' : ['olive oil', 'coconut oil', 'avocado oil', 'butter'],
    'Herbs & Spices': ['oregano', 'basil', 'thyme', 'sage', 'rosemary', 'fennel'],
    'Sweets & Drinks' : ['dark chocolate', 'fruit salad', 'coconut milk ice cream', 'almond milk hot chocolate', 'honey)'],
}
for_ibs = {
    'Pastries, Breads & Rolls': ['whole wheat bread', 'oatmeal bread', 'sourdough bread'],
    'Vegetables': ['carrots', 'celery', 'cucumber'],
    'Fruits': ['bananas', 'blueberries', 'strawberries'],
    'Whole Grains': ['oatmeal', 'quinoa', 'brown rice'],
    'Milk, Dairy Products & Eggs': ['lactose-free milk', 'plain Greek yogurt', 'hard cheeses'],
    'Meat': ['chicken breast', 'fish', 'tofu'],
    'Pasta': ['brown rice pasta', 'quinoa pasta', 'zucchini noodles'],
    'Legumes' : ['mung beans', 'green peas'],
    'Nuts & Seeds' : ['almonds', 'pumpkin seeds', 'sunflower seeds', 'chia seeds', 'flaxseeds'],
    'Oils & Fats' : ['olive oil', 'coconut oil', 'avocado oil', 'ghee'],
    'Herbs & Spices': ['peppermint', 'fennel', 'ginger', 'turmeric', 'chamomile', 'oregano'],
    'Sweets & Drinks' : ['fruit smoothies', 'herbal tea', 'almond milk latte', 'chia pudding', 'honey'],
}
for_heart = {
    'Pastries, Breads & Rolls': ['Whole grain bread', 'Whole wheat pita bread', 'Oatmeal muffins'],
    'Vegetables': ['Broccoli', 'Spinach', 'Kale', 'Sweet potatoes', 'Tomatoes'],
    'Fruits': ['Berries', 'Apples', 'Oranges', 'Pears', 'Lemon', 'Lime', 'citrus fruits'],
    'Whole Grains': ['Brown rice', 'Quinoa', 'Whole wheat pasta'],
    'Milk, Dairy Products & Eggs': ['Low-fat milk', 'Yogurt', 'Cheese', 'eggs'],
    'Meat': ['Skinless chicken', 'Fish', 'Lean cuts of beef'],
    'Pasta': ['Whole wheat pasta', 'Brown rice pasta'],
    'Legumes' : ['kidney beans', 'lima beans'],
    'Nuts & Seeds' : ['walnuts', 'almonds', 'flaxseeds', 'chia seeds', 'pumpkin seeds'],
    'Oils & Fats' : ['olive oil', 'avocado oil', 'canola oil', 'nuts'],
    'Herbs & Spices': ['garlic', 'turmeric', 'ginger', 'cinnamon', 'oregano', 'hawthorn'],
    'Sweets & Drinks' : ['water', 'unsweetened tea', 'coconut water', 'citrus fruits', 'honey'],
}
for_kidney = {
    'Pastries, Breads & Rolls': ['White bread', 'White bagels', 'White rolls', 'White tortillas'],
    'Vegetables': ['Cabbage', 'Cauliflower', 'Eggplant', 'Peppers', 'Zucchini'],
    'Fruits': ['Apples', 'Blueberries', 'Cranberries', 'Grapes', 'Pineapple'],
    'Whole Grains': ['White rice', 'White pasta', 'Couscous'],
    'Milk, Dairy Products & Eggs': ['Milk', 'eggs', 'Yogurt', 'Ice cream'],
    'Meat': ['Beef', 'Lamb'],
    'Pasta': ['White pasta', 'Couscous'],
    'Legumes' : ['kidney beans', 'lima beans'],
    'Nuts & Seeds' : ['pistachios', 'almonds', 'walnuts', 'hemp seeds', 'chia seeds'],
    'Oils & Fats' : ['olive oil', 'avocado oil', 'coconut oil', 'butter'],
    'Herbs & Spices': ['garlic', 'turmeric', 'ginger', 'cinnamon', 'oregano', 'dandelion'],
    'Sweets & Drinks' : ['water', 'herbal tea', 'coconut water', 'unsweetened almond milk', 'honey'],
}
for_lactose = {
    'Pastries, Breads & Rolls': ['Sourdough bread', 'French bread', 'Pita bread'],
    'Vegetables': ['Broccoli', 'Spinach', 'Kale', 'Sweet potatoes', 'Tomatoes'],
    'Fruits': ['Bananas', 'Oranges', 'Strawberries'],
    'Whole Grains': ['Oats', 'Brown rice', 'Quinoa', 'Barley'],
    'Milk, Dairy Products & Eggs': ['Lactose-free milk', 'Lactose-free yogurt', 'Lactose-free cheese', 'Soy milk'],
    'Meat': ['Chicken', 'Fish', 'Beef', 'Lamb'],
    'Pasta': ['rice pasta', 'quinoa pasta', 'chickpea pasta'],
    'Legumes' : ['kidney beans', 'lima beans'],
    'Nuts & Seeds' : ['almonds', 'hazelnuts', 'walnuts', 'pumpkin seeds', 'sesame seeds'],
    'Oils & Fats' : ['olive oil', 'avocado oil', 'coconut oil', 'ghee'],
    'Herbs & Spices': ['ginger', 'cumin', 'coriander', 'cinnamon', 'nutmeg', 'cardamom'],
    'Sweets & Drinks' :  ['yogurt with honey', 'coconut macaroons', 'chia seed pudding', 'honey'],
}
for_gluten = {
    'Pastries, Breads & Rolls': ['Gluten-free bread', 'Gluten-free bagels', 'Gluten-free muffins'],
    'Vegetables': ['Broccoli', 'Spinach', 'Kale', 'Sweet potatoes', 'Tomatoes'],
    'Fruits': ['Apples', 'Bananas', 'Grapes', 'Oranges', 'Strawberries'],
    'Whole Grains': ['Amaranth', 'Buckwheat', 'Corn', 'Millet', 'Rice', 'Sorghum', 'Teff'],
    'Milk, Dairy Products & Eggs': ['Milk', 'Yogurt', 'Cheese'],
    'Meat': ['Beef', 'Chicken', 'Fish', 'Lamb'],
    'Pasta': ['Gluten-free pasta'],
    'Legumes' : ['kidney beans', 'lima beans'],
    'Nuts & Seeds' : ['pumpkin seeds', 'sunflower seeds', 'sesame seeds', 'flaxseeds', 'chia seeds'],
    'Oils & Fats' : ['olive oil', 'coconut oil', 'avocado oil', 'butter'],
    'Herbs & Spices': ['oregano', 'basil', 'thyme', 'sage', 'rosemary', 'fennel'],
    'Sweets & Drinks' : ['fruit salad', 'gluten-free baked goods', 'coconut milk ice cream', 'almond milk hot chocolate', 'honey'],
}
for_fructose = {
    'Pastries, Breads & Rolls': ['Sourdough bread', 'Oat bread', 'Sourdough pancakes'],
    'Vegetables': ['Lettuce', 'Cucumber', 'Carrots', 'Bell peppers'],
    'Fruits': ['Bananas', 'Grapes', 'Oranges', 'Strawberries'],
    'Whole Grains': ['Brown rice', 'Quinoa', 'Buckwheat'],
    'Milk, Dairy Products & Eggs': ['Lactose-free milk', 'Lactose-free cheese', 'Lactose-free yogurt'],
    'Meat': ['Beef', 'Chicken', 'Turkey', 'Fish'],
    'Pasta': ['Gluten-free pasta'],
    'Legumes' : ['kidney beans', 'lima beans'],
    'Nuts & Seeds' : ['almonds', 'hazelnuts', 'walnuts', 'pumpkin seeds', 'sunflower seeds'],
    'Oils & Fats' : ['olive oil', 'coconut oil', 'avocado oil', 'ghee'],
    'Herbs & Spices': ['ginger', 'cinnamon', 'turmeric', 'coriander', 'fennel', 'anise'],
    'Sweets & Drinks' :  ['fruit smoothies', 'coconut milk ice cream', 'almond milk latte', 'chia pudding', 'honey']
}
for_histamine = {
    'Pastries, Breads & Rolls': ['Rye bread', 'Spelt bread', 'Rye crispbread'],
    'Vegetables': ['Zucchini', 'Squash', 'Cabbage', 'Potatoes'],
    'Fruits': ['Bananas', 'Peaches', 'Pears', 'Mangoes'],
    'Whole Grains': ['Brown rice', 'Quinoa', 'Buckwheat'],
    'Milk, Dairy Products & Eggs': ['Lactose-free milk', 'Lactose-free cheese', 'Lactose-free yogurt'],
    'Meat': ['Beef', 'Chicken', 'Turkey', 'Fish'],
    'Pasta': ['Gluten-free pasta'],
    'Legumes' : ['kidney beans', 'lima beans'],
    'Nuts & Seeds' : ['hemp seeds', 'pumpkin seeds', 'sunflower seeds', 'sesame seeds', 'chia seeds'],
    'Oils & Fats' : ['olive oil', 'coconut oil', 'avocado oil', 'ghee'],
    'Herbs & Spices': ['ginger', 'turmeric', 'garlic', 'cinnamon', 'oregano', 'basil'],
    'Sweets & Drinks' : ['herbal tea', 'coconut water', 'water with lemon and mint', 'fresh fruit', 'honey'],
}
for_fodmap =  {
    'Pastries, Breads & Rolls': ['Gluten-free bread', 'Gluten-free muffins', 'Sourdough bread'],
    'Vegetables': ['Zucchini', 'Cucumber', 'Carrots', 'Bell peppers'],
    'Fruits': ['Bananas', 'Blueberries', 'Oranges', 'Strawberries'],
    'Whole Grains': ['Oats', 'Quinoa', 'Brown rice'],
    'Milk, Dairy Products & Eggs': ['Lactose-free milk', 'Lactose-free cheese', 'Lactose-free yogurt'],
    'Meat': ['Beef', 'Chicken', 'Turkey', 'Fish'],
    'Pasta': ['Gluten-free pasta', 'Brown rice pasta'],
    'Legumes' : ['kidney beans', 'lima beans'],
    'Nuts & Seeds' : ['chia seeds', 'pumpkin seeds', 'sunflower seeds', 'sesame seeds', 'walnuts'],
    'Oils & Fats' : ['olive oil', 'avocado oil', 'coconut oil', 'butter'],
    'Herbs & Spices': ['ginger', 'turmeric', 'cumin', 'coriander', 'basil', 'oregano'],
    'Sweets & Drinks' : ['fruit salad', 'fresh fruit smoothies', 'chia seed pudding', 'gluten-free baked goods', 'honey']
}

#
# foods = ['almond milk', 'amaranth', 'apples', 'bananas', 'barley', 'beef', 'bell peppers', 'berries', 'blueberries', 'broccoli',
#      'brown rice', 'brown rice pasta', 'buckwheat', 'bulgur', 'cabbage', 'carrots', 'cauliflower', 'celery', 'cheese', 'chicken',
#      'chicken breast', 'chickpea pasta', 'coconut milk yogurt', 'corn', 'cottage cheese', 'couscous', 'cranberries', 'cucumber',
#      'eggplant', 'fish', 'french bread', 'gluten-free bagels', 'gluten-free bread', 'gluten-free muffins', 'gluten-free pasta',
#      'gluten-free tortillas', 'grapes', 'hard cheeses', 'ice cream', 'kale', 'lactose-free cheese', 'lactose-free milk', 'lactose-free yogurt',
#      'lamb', 'leafy greens', 'lean cuts of beef', 'lettuce', 'low-fat milk', 'mangoes', 'milk', 'millet', 'oat bread', 'oatmeal', 'oatmeal bread',
#      'oatmeal muffins', 'oats', 'oranges', 'peaches', 'pears', 'peppers', 'pineapple', 'pita bread', 'plain greek yogurt', 'potatoes', 'quinoa',
#      'quinoa pasta', 'rice', 'rice crackers', 'rice pasta', 'rye bread', 'rye crispbread', 'skinless chicken', 'sorghum', 'sourdough bread',
#      'sourdough pancakes', 'soy milk', 'spaghetti squash', 'spelt bread', 'spinach', 'squash', 'strawberries', 'sweet potatoes', 'teff', 'tofu',
#      'tomatoes', 'turkey', 'turkey breast', 'white bagels', 'white bread', 'white pasta', 'white rice', 'white rolls', 'white tortillas',
#      'whole grain bread', 'whole grain tortillas', 'whole wheat bread', 'whole wheat pasta', 'whole wheat pita bread', 'whole wheat tortillas',
#      'yogurt', 'zucchini', 'zucchini noodles','olive oil', 'avocado oil', 'coconut oil']

good_for_all = {
    'Pastries, Breads & Rolls': ['Whole grain bread', 'Oatmeal bread', 'Ezekiel bread', 'Sourdough bread', 'Sweet potato bread'],
    'Vegetables': ['Spinach', 'Kale', 'Broccoli', 'Cauliflower', 'Carrots', 'Sweet potato', 'Zucchini', 'Bell peppers'],
    'Fruits': ['Apples', 'Berries', 'Melons', 'Grapes', 'Peaches', 'Plums', 'Pears', 'Oranges'],
    'Whole Grains': ['Brown rice', 'Quinoa', 'Bulgur', 'Oats', 'Millet', 'Whole wheat pasta'],
    'Milk, Dairy Products & Eggs': ['Almond milk', 'Coconut milk', 'Cashew milk', 'Lactose-free milk', 'Plain yogurt', 'Greek yogurt', 'Cottage cheese'],
    'Meat': ['Skinless chicken breast', 'Turkey breast', 'Fish', 'Lean cuts of beef'],
    'Pasta': ['Whole wheat pasta', 'Brown rice pasta', 'Quinoa pasta', 'Lentil pasta'],
    'Legumes': ['lentils', 'chickpeas', 'black beans'],
    'Nuts & Seeds' : ['almonds', 'walnuts', 'pistachios', 'chia seeds', 'flaxseeds', 'hemp seeds'],
    'Oils & Fats' : ['olive oil', 'avocado oil'],
    'Herbs & Spices' : ['turmeric', 'cinnamon', 'garlic', 'ginger', 'rosemary', 'oregano', 'basil', 'sage', 'thyme'],
    'Sweets & Drinks' : ['dark chocolate', 'unsweetened tea', 'water', 'fruit-infused water', 'herbal tea']
}

# food_dict = {
#     'Pastries, Breads & Rolls' : {'whole grain bread', 'sourdough bread', 'whole wheat pita bread', 'gluten-free tortillas', 'white tortillas',
#                     'whole wheat tortillas', 'whole grain tortillas', 'oat bread', 'white bread', 'oatmeal muffins', 'whole wheat bread',
#                     'gluten-free bagels', 'gluten-free muffins', 'sourdough pancakes', 'rye bread', 'gluten-free bread', 'ezekiel bread',
#                     'pita bread', 'oatmeal', 'rye crispbread', 'spelt bread', 'french bread', 'sweet potato bread', 'oatmeal bread',
#                     'rice  crackers', 'white rolls', 'white bagels'},
#     'Vegetables' : {'broccoli', 'leafy greens', 'cucumber', 'squash', 'peppers', 'carrots', 'potatoes', 'zucchini', 'sweet potato', 'tomatoes',
#                     'bell peppers', 'lettuce', 'cabbage', 'celery', 'kale', 'eggplant', 'spinach', 'sweet potatoes', 'cauliflower'},
#     'Fruits' : {'peaches', 'melons', 'apples', 'pineapple', 'pears', 'mangoes', 'blueberries', 'cranberries', 'strawberries', 'bananas',
#                     'oranges', 'grapes', 'berries', 'plums'},
#     'Whole Grains' : {'whole wheat pasta', 'rice', 'buckwheat', 'brown rice', 'bulgur', 'teff', 'white pasta', 'oats', 'white rice', 'corn',
#                     'oatmeal', 'quinoa', 'couscous', 'millet', 'sorghum', 'barley', 'amaranth'},
#     'Milk, Dairy Products & Eggs' : {'cashew milk', 'hard cheeses', 'cottage cheese', 'almond milk', 'lactose-free cheese', 'lactose-free milk',
#                     'soy milk', 'coconut milk', 'cheese', 'coconut milk yogurt', 'yogurt', 'plain greek yogurt', 'plain yogurt', 'greek yogurt',
#                     'low-fat milk', 'milk', 'ice cream', 'lactose-free yogurt'},
#     'Meat' : {'beef', 'lamb', 'chicken breast', 'chicken', 'tofu', 'fish', 'skinless chicken breast', 'lean cuts of beef', 'turkey breast', 'turkey', 'skinless chicken'},
#     'Pasta' : {'whole wheat pasta', 'chickpea pasta', 'couscous', 'gluten-free pasta', 'lentil pasta', 'white pasta', 'spaghetti squash',
#                     'quinoa pasta', 'rice pasta', 'zucchini noodles', 'brown rice pasta'},
#     'Oils & Fats' : {'canola oil', 'butter', 'coconut oil', 'nuts', 'avocado oil', 'olive oil', 'ghee'},
#  }

unhealthy_foods = ["processed foods", "sugary drinks", "fried foods", "candy", "refined grains", "alcohol", "highly processed snack foods", "High-fat dairy products"]

"""Peanuts
Tree nuts
Shellfish
Fish
Eggs
Milk
Soy
Wheat"""
