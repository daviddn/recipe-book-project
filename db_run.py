from db_class import *
from recipe_class import*

db_recipes = Recipe()

# db_recipes.destroy_one('Chocolate Cake')

# db_recipes.read_all()

# db_recipes.new('Chocolate Cake', 'Chocolate, Flour, Eggs, Sugar', 'Bake the Cake', 'EC1V 0ES')

# print(db_recipes.read_one('Chocolate Cake'))

# db_recipes.get_post_code('Grilled Chicken')

# db_recipes.update_one('postcode', 'E1 3FD', 'Grilled Chicken')

db_recipes.write_to_file('recipe.txt', 'Grilled Chicken')