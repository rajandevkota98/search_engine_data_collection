import os
import sys
from search_engine.exception import CustomException
from search_engine.logger import logging
from search_engine.utils.database_handler import MongodbClient


class MetaDataStore:
    def __init__(self,):
        try:
            logging.info('initiating')
            self.root = os.path.join(os.getcwd(), 'data')
            self.images = os.path.join(self.root, 'caltech-101')
            self.labels = os.listdir(self.images)
            self.mongo = MongodbClient()
        except Exception as e:
            raise CustomException(e,sys)

    def register_labels(self,):
        try:
            logging.info('registering')
            records = {}
            existing_labels = set(self.mongo.database['labels'].distinct('label'))  # Get existing labels from the database
            for num, label in enumerate(self.labels):
                if label not in existing_labels:
                    records[f"{num}"] = label
            logging.info(f'lable detail: {records}')
            self.mongo.database['labels'].insert_one(records)
        except Exception as e:
            raise CustomException(e,sys)
    def run_step(self,):
        try:
            self.register_labels()
        except Exception as e:
            raise CustomException(e,sys)

if __name__=='__main__':
    meta = MetaDataStore()
    meta.run_step()