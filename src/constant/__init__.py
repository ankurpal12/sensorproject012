import os # it helps to interact with the operating system. reading or writing to the file system.

AWS_S3_BUCKET_NAME = "wafer-fault3"
MONGO_DATABASE_NAME = "sensor"
MONGO_COLLECTION_NAME = "faultdetect"


TARGET_COLUMN = "quality"
MONGO_DB_URL="mongodb+srv://pwskills1:nFYBDuO3sA6xzbPh@cluster01.tucy0.mongodb.net/?appName=Cluster01"
# this url is taken from the upload_data.py file. and instructions are given in that file as well.
# this is the connection string to connect to the MongoDB database.
# it contains the username, password, cluster address and other parameters.

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder =  "artifacts"