import os
import sys
from zipfile import ZipFile
import shutil
from search_engine.exception import CustomException
from search_engine.logger import logging
class DataStore:
    def __init__(self,):
        self.root = os.path.join(os.getcwd(), 'data')
        self.zip = os.path.join(self.root,'archive.zip')
        self.images = os.path.join(self.root, "caltech-101")
        self.list_unwanted = ["BACKGROUND_Google"]

    
    def prepare_data(self,):
        try:
            logging.info('Extracting all')
            with ZipFile(self.zip, 'r') as file:
                file.extractall(path= self.root)
            file.close()
        except Exception as e:
            raise CustomException(e,sys)
        
    def remove_unwanted_classes(self,):
        try:
            logging.info('Removing unwanted classes')
            for lable in self.list_unwanted:
                path = os.path.join(self.images,lable)
                shutil.rmtree(path, ignore_errors=True)
                logging.info(f'Deleted {lable}')
        except Exception as e:
            raise CustomException(e,sys)
        
    def sync_data(self,):
        try:
            logging.info('--------starting data sync-----------')
            os.system(f'aws s3 sync {self.images} s3://data-collection-bucket1/images/')
            logging.info('ending the sync')
        except Exception as e:
            raise CustomException(e,sys)
        
    def run_step(self,):
        try:
            self.prepare_data()
            self.remove_unwanted_classes()
            self.sync_data()
            return True
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=='__main__':
    store = DataStore()
    store.run_step()
    

