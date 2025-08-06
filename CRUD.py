from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for the Animal collection in MongoDB"""

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34419
        DB = 'AAC'
        COL = 'animals'
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Complete this create method to implement the C in CRUD.
    def create(self, data: dict) -> bool:
        if data is not None:
            # data should be a dictionary
            self.database.animals.insert_one(data)
            # Return -> “True” if successful insert
            return True
        else:
            # User did not provide something to create.
            return False
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, query: dict) -> list:
        # Important: Be sure to use find() instead of find_one() when developing your method. 
        # Hint: You must work with the MongoDB cursor returned by the find() method.
        if query is not None:
            cursor = self.collection.find(query or {})
            results = []
            for document in cursor:
                results.append(document)
            # Return -> result in a list if the command is successful
            return results
        else:
            # User did not provide something to read.
            raise Exception("Nothing to read, because queury paramter is empty.")
    
    # An Update method that queries for and changes document(s) from a specified MongoDB database and specified collection
    def update(self, query: dict, new_values: dict) -> int:
        if query and new_values:
            # Check for a match
            cursor = self.collection.find(query)
            # Check for a match
            matches = list(cursor)
            
            if matches:
                # Input -> arguments to function should be the key/value lookup pair
                update_op = {"$set": new_values}

                # MongoDB driver update_one() or update_many() API call.
                result = self.collection.update_many(query, update_op)

                # Return -> The number of objects modified in the collection.
                return result.modified_count
            else:
                raise Exception("Nothing to update, because the provided query does not exist.")
        else:
            # user did not provide a query to update or provide a new update.
            raise Exception("Nothing to update, because either query or new value parameters are empty.")
    
    # Function to delete an entry. 
    def delete(self, query: dict) -> int:
        if query is not None:
            # Set the cursor to the enter query
            cursor = self.collection.find(query)
            # Check for a match
            matches = list(cursor)
            
            if matches:
                print("Matches: ", len(matches))
                # Delete documents
                result = self.collection.delete_many(query)
                # Return -> The number of objects removed from the collection.
                return result.deleted_count
            else:
                raise Exception("Nothing to delete, because query does not exist.")
        else:
            # User did not enter anything to delete.
            raise Exception("Nothing to delete, because query parameter is empty.")
