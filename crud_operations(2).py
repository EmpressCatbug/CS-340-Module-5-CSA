from pymongo import MongoClient, errors

class CRUD:
    """CRUD operations for a specified MongoDB collection."""

    def __init__(self, user, password, host, port, db_name, collection_name):
        """Initialize the MongoClient and access the MongoDB databases and collections."""
        try:
            self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}')
            self.database = self.client[AAC]
            self.collection = self.database[animals]
            print("MongoDB connection established.")
        except errors.ConnectionFailure as e:
            print(f"Could not connect to MongoDB: {e}")

    def create(self, document):
        """Insert a document into the specified MongoDB collection.
        
        Args:
            document (dict): A set of key/value pairs in the format acceptable to the MongoDB driver insert API call.
        
        Returns:
            bool: True if the insert is successful else False.
        """
        if document is not None and isinstance(document, dict):
            try:
                self.collection.insert_one(document)
                return True
            except Exception as e:
                print(f"An error occurred while inserting data: {e}")
                return False
        else:
            print("Invalid document. Please provide a dictionary.")
            return False

    def read(self, query):
        """Query for documents in the specified MongoDB collection."""
        if query is not None and isinstance(query, dict):
            try:
                cursor = self.collection.find(query)
                return list(cursor)
            except Exception as e:
                print(f"An error occurred while querying data: {e}")
                return []
        else:
            print("Invalid query. Please provide a dictionary.")
            return []

    def update(self, query, new_values):
        """Update documents in the specified MongoDB collection.
        
        Args:
            query (dict): A key/value lookup pair to use with the MongoDB driver find API call.
            new_values (dict): A set of key/value pairs in the data type acceptable to the MongoDB driver update API call.
        
        Returns:
            int: The number of documents modified.
        """
        if query is not None and isinstance(query, dict) and new_values is not None and isinstance(new_values, dict):
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except Exception as e:
                print(f"An error occurred while updating data: {e}")
                return 0
        else:
            print("Invalid input. Please provide dictionaries for query and new values.")
            return 0

    def delete(self, query):
        """Delete documents from the specified MongoDB collection.
        
        Args:
            query (dict): A key/value lookup pair to use with the MongoDB driver find API call.
        
        Returns:
            int: The number of documents deleted.
        """
        if query is not None and isinstance(query, dict):
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"An error occurred while deleting data: {e}")
                return 0
        else:
            print("Invalid query. Please provide a dictionary.")
            return 0

# Example usage:
if __name__ == "__main__":
    USER = 'aacuser'
    PASS = 'SNHU1234'
    HOST = 'nv-desktop-services.apporto.com'
    PORT = 31111
    DB = 'AAC'
    COL = 'animals'

    crud = CRUD(USER, PASS, HOST, PORT, DB, COL)
    
    # Example of creating a document
    new_animal = {
        "age_upon_outcome": "1 year",
        "animal_id": "A812345",
        "breed": "Labrador Retriever Mix",
        "color": "Black/White",
        "date_of_birth": "2019-01-01",
        "datetime": "2020-01-10 16:30:00",
        "outcome_type": "Adoption",
        "sex_upon_outcome": "Neutered Male",
        "name": "Max"
    }
    result = crud.create(new_animal)
    print("Insert successful:", result)

    # Example of reading documents
    query = {"animal_id": "A812345"}
    animals = crud.read(query)
    print("Query result:", animals)

    # Example of updating documents
    update_query = {"animal_id": "A812345"}
    new_values = {"age_upon_outcome": "2 years"}
    update_result = crud.update(update_query, new_values)
    print("Update result:", update_result)

    # Example of deleting documents
    delete_query = {"animal_id": "A812345"}
    delete_result = crud.delete(delete_query)
    print("Delete result:", delete_result)
