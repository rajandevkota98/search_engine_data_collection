import os,sys
import boto3
from typing import Dict, List
from search_engine.utils.unique_id import image_unique_name
from search_engine.exception import CustomException
from search_engine.logger import logging

class S3Connection:
    def __init__(self):
        session = boto3.Session(
            aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        )
        self.s3 = session.resource("s3")
        self.bucket = self.s3.Bucket(os.environ["AWS_BUCKET_NAME"])

    def add_label(self, label: str) -> Dict:
 
        try:
            key = f"images/{label}/"
            response = self.bucket.put_object(Body="", Key=key)
            return {"Created": True, "Path": response.key}
        except Exception as e:
            message = CustomException(e, sys)
            return {"Created": False, "Reason": message.error_message}

    def upload_to_s3(self, image_path, label: str):

        try:
            self.bucket.upload_fileobj(
                image_path,
                f"images/{label}/{image_unique_name()}.jpeg",
                ExtraArgs={"ACL": "public-read"},
            )
            return {"Created": True}
        except Exception as e:
            message = CustomException(e, sys)
            return {"Created": False, "Reason": message.error_message}