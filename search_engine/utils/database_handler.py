import pymongo
import os

class MongodbClient:
    client = None

    def __init__(self, database_name = os.environ['DATABASE_NAME']):
        if MongodbClient.client is None:
            MongodbClient.client=pymongo.MongoClient(
            "mongodb+srv://rdevkota98:rajan98@reverseimagesearch.9ibunre.mongodb.net/?retryWrites=true&w=majority"
            )
        self.client = MongodbClient.client
        self.database = self.client[database_name]
        self.database_name = database_name