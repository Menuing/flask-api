from joblib import load
from flask import Response
import json
import numpy as np
import pandas as pd

class RecipePredictionController(object):
    def __init__(self, model_path):
        self.model = load(model_path)


    def predict(self, request):
        vector = self.getIngList(request.args.getlist('listIngRecipe'))
        
        vector.extend(
        [
            request.args.get('numIngUser'),
            request.args.get('rating')
        ])
        
        res = {
            "prediction": int(self.model.predict(
                np.array(vector, dtype=float).reshape(1, -1)
            )[0])
            ,
            "probabilityDislike": self.model.predict_proba(
                np.array(vector, dtype=float).reshape(1, -1)
            )[0][0]
            ,
            "probabilityLike": self.model.predict_proba(
                np.array(vector, dtype=float).reshape(1, -1)
            )[0][1]
        }

        return Response(json.dumps(res), status=200)

    def getIngList(self, userIngr):
        ingredients = pd.DataFrame([[0]*668], columns=allowed_ingr)
        ingredients[userIngr] = 1
        return ingredients.iloc[0].values.tolist()









allowed_ingr =['alabama', 'alaska', 'alcoholic', 'almond', 'amaretto', 'anchovy',
'anise', 'anniversary', 'anthony bourdain', 'aperitif',
'appetizer', 'apple', 'apple juice', 'apricot', 'arizona',
'artichoke', 'arugula', 'asian pear', 'asparagus', 'aspen',
'atlanta', 'australia', 'avocado', 'back to school',
'backyard bbq', 'bacon', 'bake', 'banana', 'barley', 'basil',
'bass', 'bastille day', 'bean', 'beef', 'beef rib', 'beef shank',
'beef tenderloin', 'beer', 'beet', 'bell pepper', 'berry',
'beverly hills', 'birthday', 'biscuit', 'bitters', 'blackberry',
'blender', 'blue cheese', 'blueberry', 'boil', 'bok choy',
'bon appétit', 'bon appetit', 'boston', 'bourbon', 'braise',
'bran', 'brandy', 'bread', 'breadcrumbs', 'breakfast', 'brie',
'brine', 'brisket', 'broccoli', 'broccoli rabe', 'broil',
'brooklyn', 'brown rice', 'brownie', 'brunch', 'brussel sprout',
'buffalo', 'buffet', 'bulgaria', 'bulgur', 'burrito', 'butter',
'buttermilk', 'butternut squash', 'butterscotch/caramel',
'cabbage', 'cake', 'california', 'calvados', 'cambridge',
'campari', 'camping', 'canada', 'candy', 'candy thermometer',
'cantaloupe', 'capers', 'caraway', 'cardamom', 'carrot', 'cashew',
'casserole/gratin', 'cauliflower', 'caviar', 'celery', 'chambord',
'champagne', 'chard', 'chartreuse', 'cheddar', 'cheese', 'cherry',
'chestnut', 'chicago', 'chicken', 'chickpea', 'chile',
'chile pepper', 'chili', 'chill', 'chive', 'chocolate',
'christmas', 'christmas eve', 'cilantro', 'cinco de mayo',
'cinnamon', 'citrus', 'clam', 'clove', 'cobbler/crumble',
'cocktail', 'cocktail party', 'coconut', 'cod', 'coffee',
'coffee grinder', 'cognac/armagnac', 'collard greens', 'colorado',
'columbus', 'condiment', 'condiment/spread', 'connecticut',
'cook like a diner', 'cookbook critic', 'cookie', 'cookies',
'coriander', 'corn', 'cornmeal', 'costa mesa', 'cottage cheese',
'couscous', 'crab', 'cranberry', 'cranberry sauce', 'cream cheese',
'créme de cacao', 'crêpe', 'creme de cacao', 'cuba', 'cucumber',
'cumin', 'cupcake', 'currant', 'curry', 'custard', 'dairy',
'dairy free', 'dallas', 'date', 'deep-fry', 'denver', 'dessert',
'digestif', 'dill', 'dinner', 'dip', 'diwali',
'dominican republic', 'dorie greenspan', 'double boiler',
'dried fruit', 'drink', 'drinks', 'duck', 'easter', 'eau de vie',
'edible gift', 'egg', 'egg nog', 'eggplant', 'egypt',
'emeril lagasse', 'endive', 'engagement party', 'england',
'entertaining', 'epi + ushg', 'epi loves the microwave',
'escarole', 'fall', 'family reunion', 'fat free', "father's day",
'fennel', 'feta', 'fig', 'fish', 'flaming hot summer',
'flat bread', 'florida', 'fontina', 'food processor',
'fortified wine', 'fourth of july', 'france', 'frangelico',
'frankenrecipe', 'freeze/chill', 'freezer food', 'friendsgiving',
'frittata', 'fritter', 'frozen dessert', 'fruit', 'fruit juice',
'fry', 'game', 'garlic', 'georgia', 'germany', 'gin', 'ginger',
'goat cheese', 'goose', 'gouda', 'gourmet', 'graduation', 'grains',
'grand marnier', 'granola', 'grape', 'grapefruit', 'grappa',
'green bean', 'green onion/scallion', 'grill', 'grill/barbecue',
'ground beef', 'ground lamb', 'guam', 'guava', 'haiti', 'halibut',
'halloween', 'ham', 'hamburger', 'hanukkah', 'harpercollins',
'hawaii', 'hazelnut', 'healdsburg', 'healthy', 'herb',
'high fiber', 'hollywood', 'hominy/cornmeal/masa', 'honey',
'honeydew', "hors d'oeuvre", 'horseradish', 'hot drink',
'hot pepper', 'house & garden', 'house cocktail', 'houston',
'hummus', 'ice cream', 'ice cream machine', 'iced coffee',
'iced tea', 'idaho', 'illinois', 'indiana', 'iowa', 'ireland',
'israel', 'italy', 'jalapeño', 'jam or jelly', 'jamaica', 'japan',
'jerusalem artichoke', 'juicer', 'jícama', 'kahlúa', 'kale',
'kansas', 'kansas city', 'kentucky', 'kentucky derby',
'kid-friendly', 'kidney friendly', 'kirsch', 'kitchen olympics',
'kiwi', 'kosher', 'kosher for passover', 'kumquat', 'kwanzaa',
'labor day', 'lamb', 'lamb chop', 'lamb shank', 'lancaster',
'las vegas', 'lasagna', 'leafy green', 'leek', 'legume', 'lemon',
'lemon juice', 'lemongrass', 'lentil', 'lettuce', 'lima bean',
'lime', 'lime juice', 'lingonberry', 'liqueur', 'lobster',
'london', 'long beach', 'los angeles', 'louisiana', 'louisville',
'low cal', 'low carb', 'low cholesterol', 'low fat', 'low sodium',
'low sugar', 'low/no sugar', 'lunar new year', 'lunch', 'lychee',
'macadamia nut', 'macaroni and cheese', 'maine', 'mandoline',
'mango', 'maple syrup', 'mardi gras', 'margarita', 'marinade',
'marinate', 'marsala', 'marscarpone', 'marshmallow', 'martini',
'maryland', 'massachusetts', 'mayonnaise', 'meat', 'meatball',
'meatloaf', 'melon', 'mexico', 'mezcal', 'miami', 'michigan',
'microwave', 'midori', 'milk/cream', 'minneapolis', 'minnesota',
'mint', 'mississippi', 'missouri', 'mixer', 'molasses',
'monterey jack', 'mortar and pestle', "mother's day", 'mozzarella',
'muffin', 'mushroom', 'mussel', 'mustard', 'mustard greens',
'nancy silverton', 'nebraska', 'nectarine', 'new hampshire',
'new jersey', 'new mexico', 'new orleans', "new year's day",
"new year's eve", 'new york', 'no meat, no problem',
'no sugar added', 'no-cook', 'non-alcoholic', 'noodle',
'north carolina', 'nut', 'nutmeg', 'oat', 'oatmeal', 'octopus',
'ohio', 'oklahoma', 'okra', 'oktoberfest', 'olive', 'omelet',
'one-pot meal', 'onion', 'orange', 'orange juice', 'oregano',
'oregon', 'organic', 'orzo', 'oscars', 'oyster',
'pacific palisades', 'paleo', 'pan-fry', 'pancake', 'papaya',
'paprika', 'parade', 'paris', 'parmesan', 'parsley', 'parsnip',
'party', 'pasadena', 'passion fruit', 'passover', 'pasta',
'pasta maker', 'pastry', 'pea', 'peach', 'peanut', 'peanut butter',
'peanut free', 'pear', 'pecan', 'pennsylvania', 'pepper', 'pernod',
'persian new year', 'persimmon', 'peru', 'pescatarian',
'philippines', 'phyllo/puff pastry dough', 'pickles', 'picnic',
'pie', 'pine nut', 'pineapple', 'pistachio', 'pittsburgh', 'pizza',
'plantain', 'plum', 'poach', 'poblano', 'poker/game night',
'pomegranate', 'pomegranate juice', 'poppy', 'pork', 'pork chop',
'pork rib', 'pork tenderloin', 'port', 'portland', 'pot pie',
'potato', 'potato salad', 'potluck', 'poultry', 'poultry sausage',
'pressure cooker', 'prosciutto', 'providence', 'prune', 'pumpkin',
'punch', 'purim', 'quail', 'quiche', 'quick & easy',
'quick and healthy', 'quince', 'quinoa', 'rabbit', 'rack of lamb',
'radicchio', 'radish', 'raisin', 'ramadan', 'ramekin', 'raspberry',
'raw', 'red wine', 'rhode island', 'rhubarb', 'rice', 'ricotta',
'roast', 'root vegetable', 'rosemary', 'rosh hashanah/yom kippur',
'rosé', 'rub', 'rum', 'rutabaga', 'rye', 'saffron', 'sage', 'sake',
'salad', 'salad dressing', 'salmon', 'salsa', 'san francisco',
'sandwich', 'sandwich theory', 'sangria', 'santa monica',
'sardine', 'sauce', 'sausage', 'sauté', 'scallop', 'scotch',
'seafood', 'seattle', 'seed', 'self', 'semolina', 'sesame',
'sesame oil', 'shallot', 'shavuot', 'shellfish', 'sherry',
'shower', 'shrimp', 'side', 'simmer', 'skewer', 'slow cooker',
'smoker', 'smoothie', 'snapper', 'sorbet', 'soufflé/meringue',
'soup/stew', 'sour cream', 'sourdough', 'south carolina', 'soy',
'soy free', 'soy sauce', 'spain', 'sparkling wine', 'spice',
'spinach', 'spirit', 'spring', 'spritzer', 'squash', 'squid',
'st. louis', "st. patrick's day", 'steak', 'steam', 'stew',
'stir-fry', 'stock', 'strawberry', 'stuffing/dressing',
'sugar conscious', 'sugar snap pea', 'sukkot', 'summer',
'super bowl', 'suzanne goin', 'sweet potato/yam', 'swiss cheese',
'switzerland', 'swordfish', 'taco', 'tailgating', 'tamarind',
'tangerine', 'tapioca', 'tarragon', 'tart', 'tea', 'tennessee',
'tequila', 'tested & improved', 'texas', 'thanksgiving', 'thyme',
'tilapia', 'tofu', 'tomatillo', 'tomato', 'tortillas', 'tree nut',
'tree nut free', 'triple sec', 'tropical fruit', 'trout', 'tuna',
'turnip', 'utah', "valentine's day", 'vanilla', 'veal', 'vegan',
'vegetable', 'vegetarian', 'venison', 'vermont', 'vermouth',
'vinegar', 'virginia', 'vodka', 'waffle', 'walnut', 'wasabi',
'washington', 'washington, d.c.', 'watercress', 'watermelon',
'wedding', 'weelicious', 'west virginia', 'westwood',
'wheat/gluten-free', 'whiskey', 'white wine', 'whole wheat',
'wild rice', 'windsor', 'wine', 'winter', 'wisconsin', 'wok',
'yellow squash', 'yogurt', 'yonkers', 'yuca', 'zucchini',
'cookbooks', 'leftovers', 'snack', 'snack week', 'turkey']