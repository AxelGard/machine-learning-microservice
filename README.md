# machine-learning-microservice

<img src="https://raw.githubusercontent.com/AxelGard/machine-learning-microservice/master/doc/icon.png" alt="drawing" style="width:300px;"/>

My template for how to make a simple micro service for machine learning models. (in python)


Most likley you will want to change the predicted resturn to be json and not html. 
As well as chage the data to be sent in a json format. 
This is justa way of very easliy intract with the service and test it. 

## setup


### install 

```
python3 -m venv env
```

```
source ./env/bin/activate
```

```
pip install -r requirements.txt
```

### run

```
python3 service/server.py
```

### train

In `machine-learning-microservice/service/train.ipynb` you can re-train the model or change the problem, models etc. 

If you add a new model, it also need to be in the server. 

## UI

![example](./doc/ex.png)