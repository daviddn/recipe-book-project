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

    # Update one recipe in the recipe table
    def update_one(self, column, updated_value, name):
        self.filter_query(f"UPDATE Recipes SET {column} = '{updated_value}' WHERE Recipe_Name = '{name}'")
        self.conn_db.commit()

    # Deletes one recipe from the recipe table
    def destroy_one(self, name):
        self.filter_query(f"DELETE FROM Recipes WHERE Recipe_Name = '{name}'")
        self.conn_db.commit()

    # Gets one postcode from recipes list
    def read_postcode(self, name):
        query = self.filter_query(f"SELECT Postcode FROM Recipes WHERE Recipe_Name = '{name}'").fetchone()[0]
        return query

    # Returns postcode from looking up postcode returned from table on postcodes.io api
    def get_post_code(self, name):
        got_postcode = self.read_postcode(name)
        request_postcode = requests.get(f"http://api.postcodes.io/postcodes/{got_postcode}".lower().strip())
        converted_postcode = request_postcode.json()
        postcode = converted_postcode['result']['postcode']
        return postcode

    # Write postcode to file
    def write_to_file(self, file, name):
        try:
            with open(file, 'a') as opened_file:
                opened_file.write(f"{self.read_one(name)}\n")

        except FileNotFoundError:
            print('File not found')