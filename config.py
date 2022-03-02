MODEL_NAME = "model.pkl"
BUCKET_NAME = "<CHANGE ME>"
ACCESS_KEY = "<CHANGE ME>"
SECRET_KEY = "<CHANGE ME>"
S3_LOCATION = "http://{0}.s3.amazonaws.com/{1}".format(BUCKET_NAME, MODEL_NAME)
MODEL_LOCAL_STORAGE_PATH = "/tmp/model.pkl"
