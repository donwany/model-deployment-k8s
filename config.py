MODEL_NAME = "model.pkl"
BUCKET_NAME = "att-buc"
ACCESS_KEY = "AKIAJQBYHBOJUQ5EWRMA"
SECRET_KEY = "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"
S3_LOCATION = "http://{0}.s3.amazonaws.com/{1}".format(BUCKET_NAME, MODEL_NAME)
MODEL_LOCAL_STORAGE_PATH = "/tmp/model.pkl"
