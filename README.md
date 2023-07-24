# Embedding Based Image Search Engine
## Data Collection Endpoint

This repository containts code for data collection which is required to train our embeding based image search engine.

# Architecture
The CI-CD pipeline is implemented while devpoling this project.
![CICD](https://github.com/rajandevkota98/search_engine_data_collection/raw/main/images/CICD.png)


![outline](https://github.com/rajandevkota98/search_engine_data_collection/blob/main/images/Screenshot%20from%202023-07-24%2010-23-06.png)

# Action Workflow
1. On push checkout the code and create docker container on git-hub server.
2. Push the image to Ecr with production tag
3. Once action push is completed pull and run the image on Ec2 instance.




# Route Details
Here is the screenshot of the route.
![ss](https://github.com/rajandevkota98/search_engine_data_collection/blob/main/images/server.png)

- /fetch : To get labels currently present in the database. Important to call as it updates in memory database.
- /Single_upload : This Api Should be used to upload single image to s3 bucket
- /bulk_upload : This Api should be used to upload bulk images to s3 bucket
- /add_label : This api should be ued to add new label in s3 bucket.



# Infrastructure Details

- *S3 Bucket*
- *Mongo Database*
- *Elastic Container Registry*
- *Elastic Compute Cloud*


# Steps
1. Download dataset: Dataset link(https://www.kaggle.com/datasets/imbikramsaha/caltech-101)
2. Put archive.zip in data folder.
3. run s3_setup.py
4. run mongo_setup.py

# Env Variable
```bash
export ATLAS_CLUSTER_USERNAME=<username>
export ATLAS_CLUSTER_PASSWORD=<password>

export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
export AWS_REGION=<region>

export AWS_BUCKET_NAME=<AWS_BUCKET_NAME>
export AWS_ECR_LOGIN_URI=<AWS_ECR_LOGIN_URI>
export ECR_REPOSITORY_NAME=<name>

export DATABASE_NAME=<name>
```

# To run locally

1. Clone the code
2. Create a virtual environment
```
conda create -n new_env python=3.9 -y
```
3. Activate the environment

```
conda activate new_env
```

4. run the s3_setup, mongo_setup.py

5. run app.py

