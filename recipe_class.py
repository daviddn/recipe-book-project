from db_class import *

# Define a class recipe
class Recipe(Connectdb):

    # Define methods

    # read() (have this on db_class)
    # - read one object
    def read_one(self, name):
        query = self.filter_query(f"SELECT * FROM Recipes WHERE Recipe_Name = '{name}'").fetchone()
        return query

    # all() (have this on db_class)
    def read_all(self):
    # - gets all the instances from DB
        query = self.filter_query(f"SELECT * FROM Recipes")
        while True:
            record = query.fetchone()
            if record is None:
                break
            print('Recipe: ' + record[0], 'Ingredients: ' + record[1], 'Instructions: ' + record[2], 'Postcode: ' + record[3])

    # new()
    def new(self, recipe_name, ingredients, instructions, postcode):
        self.cursor.execute(f"INSERT INTO Recipes (Recipe_Name, Ingredients, Instructions, Postcode) VALUES {recipe_name, ingredients, instructions, postcode}")
        self.conn_db.commit()

        # destroy() - one object
    def destroy(self):
        pass
