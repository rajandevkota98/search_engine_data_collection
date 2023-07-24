import pymongo
import os,sys
from search_engine.logger import logging
from search_engine.exception import CustomException


class MongodbClient:
    client = None

    def __init__(self, database_name=os.environ['DATABASE_NAME']):
        if MongodbClient.client is None:
            MongodbClient.client = pymongo.MongoClient(
                f"mongodb+srv://{os.environ['ATLAS_CLUSTER_USERNAME']}:{os.environ['ATLAS_CLUSTER_PASSWORD']}@reverseimagesearch.9ibunre.mongodb.net/?retryWrites=true&w=majority"
            )
        self.client = MongodbClient.client
        self.database = self.client[database_name]
        self.database_name = database_name

    def fetch_data(self, collection_name):
        try:
            logging.info(f'Fetching data from collection: {collection_name}')
            collection = self.database[collection_name]
            result = collection.find({})  # Fetch all documents in the collection
            return list(result)  # Convert the result cursor to a list of documents
        except Exception as e:
            raise CustomException(e, sys)
        
    def empty_collection(self, collection_name):
        try:
            logging.info(f'Emptying collection: {collection_name}')
            collection = self.database[collection_name]
            collection.delete_many({})  # Delete all documents in the collection
            logging.info(f'Collection {collection_name} is now empty.')
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == '__main__':
    # Assuming you have already set up the environment variables for Atlas cluster and database
    database_name = os.environ['DATABASE_NAME']
    collection_name = 'labels'  # Replace with the name of the collection you want to fetch data from

    # Create an instance of the MongodbClient class
    mongodb_client = MongodbClient(database_name)

    # Fetch data from the specified collection
    data = mongodb_client.fetch_data(collection_name)

    mongodb_client.empty_collection(collection_name)


    # Print the fetched data
    for document in data:
        print(document)
