### CHANGE ME IN THE CONFIG.PY FILE

```shell
BUCKET_NAME = "<CHANGE ME>"
ACCESS_KEY = "<CHANGE ME>"
SECRET_KEY = "<CHANGE ME>"
```
### Train Model
```python
python trainer.py
```

### Build Image
````shell
CHANGE DOCKERNAME USER TO YOUR OWN --> worldbosskafka

docker build -t worldbosskafka/iris-model-app:1.0.0 .
docker run -p 1957:1957 worldbosskafka/iris-model-app:1.0.0
docker push worldbosskafka/iris-model-app:1.0.0
````
### Deploy Model
```shell
kubectl -f namespace.yaml
kubectl -f deployment.yaml
kubectl -f service

kubectl get pods -o wide
kubectl get services -o wide
```

### Test API
```shell
curl --request POST 'http://192.168.205.3:32743/predict' \
 --header 'Content-Type: application/json' \
 --data-raw '{"sepal_length": 6.2,"sepal_width": 4.6,"petal_length": 2.5,"petal_width": 6.7}'
```

### RestAPI with Python: python TestAPI.py
```python
import requests
import json

url = "http://192.168.205.3:32743/predict" # http://ec.com.gh/predict
payload = json.dumps({
    "sepal_length": 0.2,
    "sepal_width": 0.6,
    "petal_length": 3.5,
    "petal_width": 1.7
})
headers = {
    'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

if __name__ == '__main__':
    pass
```

