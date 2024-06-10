# CS-340-Module-5-CSA
Client-Side Authentication Assignment


# CS-340 MongoDB Authentication Dashboard

## Overview

This project is part of the CS-340 course at Southern New Hampshire University. The goal of this assignment is to create a dashboard using the Dash framework that authenticates users with a MongoDB database. The dashboard prompts the user to enter their username and password, then uses these credentials to query the database and return specific results.

## Prerequisites

- Python 3.x
- Jupyter Notebook
- Dash
- MongoDB
- Your CRUD module from Project One

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages using pip:
   ```bash
   pip install dash jupyter-dash pymongo
   ```
3. Ensure you have a MongoDB instance running and accessible.
4. Make sure your CRUD module from Project One is available and correctly implemented.

## Setup

1. Open the `Module Five Assignment.ipynb` file in Jupyter Notebook.
2. Ensure your `crud_operations.py` file is correctly implemented as shown below:

    ```python
    from pymongo import MongoClient, errors

    class CRUD:
        """CRUD operations for a specified MongoDB collection."""

        def __init__(self, user, password, host, port, db_name, collection_name):
            """Initialize the MongoClient and access the MongoDB databases and collections."""
            try:
                self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}')
                self.database = self.client[db_name]
                self.collection = self.database[collection_name]
                print("MongoDB connection established.")
            except errors.ConnectionFailure as e:
                print(f"Could not connect to MongoDB: {e}")

        def create(self, document):
            """Insert a document into the specified MongoDB collection."""
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
            """Update documents in the specified MongoDB collection."""
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
            """Delete documents from the specified MongoDB collection."""
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
    ```

3. Update the import statement for your CRUD module in the notebook:

    ```python
    from crud_operations import CRUD
    ```

## Running the Dashboard

1. Launch Jupyter Notebook and open the `Module Five Assignment.ipynb` file.
2. Execute the cells in the notebook to start the Dash server.
3. Open the provided URL (usually `http://127.0.0.1:31111/`) in your web browser to access the dashboard.

## Usage

1. Enter your MongoDB username and password in the provided input fields.
2. Click the `Submit` button.
3. The dashboard will authenticate the user and execute a test query on the MongoDB database:
   ```json
   {"animal_type": "Dog", "name": "Lucy"}
   ```
4. The results of the query will be displayed on the dashboard.

## Screenshot
## Screenshots

![Dashboard showing user login and MongoDB query results - 1](CS%20340%20Module%205%20(1).png)
![Dashboard showing user login and MongoDB query results - 2](CS%20340%20Module%205%20(2).png)
![Dashboard showing user login and MongoDB query results - 3](CS%20340%20Module%205%20(3).png)
![Dashboard showing user login and MongoDB query results - 4](CS%20340%20Module%205%20(4).png)
![Dashboard showing user login and MongoDB query results](CS%20340%20Module%205.png)


Include screenshots of your running dashboard here. The screenshots should show the username/password input fields, the submit button, and the query result. Ensure your unique identifier (name) is visible.

## Important Notes

- This assignment requires the use of the "aacuser" account and password set up in the Module Three milestone. If you did not complete the milestone, follow the steps in Part II of the milestone to set up the "aacuser" account before beginning this assignment.
- The authentication built in this assignment passes the username and password directly to the MongoDB database. The Dash framework's authentication component is not used in this assignment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
