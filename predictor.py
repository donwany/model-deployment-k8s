import datetime
import pickle
import uuid
import boto3
import botocore
from flask import Flask, request, jsonify
from config import ACCESS_KEY, SECRET_KEY, BUCKET_NAME, MODEL_LOCAL_STORAGE_PATH

app = Flask(__name__)

# Model Labels
labels = ["setosa", "versicolor", "virginica"]


class PythonPredictor:
    def __init__(self):

        s3 = boto3.client(
            "s3",
            aws_access_key_id=str(ACCESS_KEY),
            aws_secret_access_key=str(SECRET_KEY),
        )
        try:
            with open(MODEL_LOCAL_STORAGE_PATH, "wb") as f:
                s3.download_fileobj(BUCKET_NAME, "model.pkl", f)

        except botocore.exceptions.ClientError as e:
            if e.response["Error"]["Code"] == "404":
                print("============ The Model Object Does Not Exist ================")
            else:
                raise

        self.model = pickle.load(open(MODEL_LOCAL_STORAGE_PATH, "rb"))

    def predict(self, payload):
        measurements = [
            payload["sepal_length"],
            payload["sepal_width"],
            payload["petal_length"],
            payload["petal_width"],
        ]
        label_id = self.model.predict([measurements])[0]
        return labels[label_id]


@app.route("/predict", methods=["POST"])
def predict():
    """Direct API Call"""
    if request.method == "POST":
        model = PythonPredictor()
        payload = request.get_json(force=True)
        # make predictions
        prediction = model.predict(payload)

        response = {
            "status": 200,
            "modelID": uuid.uuid1(),
            "prediction": prediction,
            "modelType": "LogisticRegression",
            "created_at": datetime.datetime.now(),
            "message": "Success"
        }
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=1957)
