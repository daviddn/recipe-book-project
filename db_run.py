from db_class import *

db_recipes = Connectdb()

print(db_recipes.read_one('1'))