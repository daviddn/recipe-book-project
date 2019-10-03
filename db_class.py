import pyodbc

# Define a class to access our db

class Connectdb():
    # have the characterstics to access the db
    def __init__(self, server = 'localhost, 1433', database = 'CookingSpartans', username = 'SA', password = 'Passw0rd2018'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_nwdb.cursor()

    def filter_query(self, query):
        return self.cursor.execute(query)

    def read_one(self, number):
        query = self.filter_query(f"SELECT * FROM Recipes WHERE RecipeID = {number}").fetchone()
        return query
    # Define methods
        # read() (have this on db_class)
            # - read one object
        # all() (have this on db_class)
            # -  gets all the instances from DB
            # gets each record
            # create individual instances of recipes
            # store them in a list
            # return list