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