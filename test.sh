curl --request POST 'http://127.0.0.1:1957/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"sepal_length": 5.2,"sepal_width": 3.6,"petal_length": 1.5,"petal_width": 0.3}'

sleep 2

 curl --request POST 'http://127.0.0.1:1957/predict' \
 --header 'Content-Type: application/json' \
 --data-raw '{"sepal_length": 6.2,"sepal_width": 4.6,"petal_length": 2.5,"petal_width": 6.7}'

sleep 2

 curl --request POST 'http://192.168.205.3:32743/predict' \
 --header 'Content-Type: application/json' \
 --data-raw '{"sepal_length": 6.2,"sepal_width": 4.6,"petal_length": 2.5,"petal_width": 6.7}'

