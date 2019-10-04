from db_class import *
from recipe_class import*

db_recipes = Recipe()

db_recipes.read_all()

# db_recipes.new('Chocolate Cake', 'Chocolate, Flour, Eggs, Sugar', 'Bake the Cake', 'EC1V 0ES')

# print(db_recipes.read_one('Chocolate Cake'))