from db_class import *

# Define a class recipe
class Recipe(Connectdb):

# Define methods

    # Shows one recipe in the recipe table
    def read_one(self, name):
        query = self.filter_query(f"SELECT * FROM Recipes WHERE Recipe_Name = '{name}'").fetchone()
        return query

    # Shows all recipes in the recipe table
    def read_all(self):
        query = self.filter_query(f"SELECT * FROM Recipes")
        while True:
            record = query.fetchone()
            if record is None:
                break
            print('Recipe: ' + record[0], 'Ingredients: ' + record[1], 'Instructions: ' + record[2], 'Postcode: ' + record[3])

    # Creates new recipe in the recipe table
    def new(self, recipe_name, ingredients, instructions, postcode):
        self.filter_query(f"INSERT INTO Recipes (Recipe_Name, Ingredients, Instructions, Postcode) VALUES {recipe_name, ingredients, instructions, postcode}")
        self.conn_db.commit()

    # Deletes one recipe from the recipe table
    def destroy_one(self, name):
        self.filter_query(f"DELETE FROM Recipes WHERE Recipe_Name = '{name}'")
        self.conn_db.commit()
