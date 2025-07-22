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

```
mkdir data
```

Download a data set, as en example I have used https://gist.github.com/slopp/ce3b90b9168f2f921784de84fa445651
```
cp ../Downlaods/penguin.csv ./data/penguin.csv
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



### ex input

```csv
bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g
39.5,16.7,178.0,3250.0
50.9,17.9,196.0,3675.0
42.1,19.1,195.0,4000.0
46.6,14.2,210.0,4850.0
41.1,18.2,192.0,4050.0
54.2,20.8,201.0,4300.0
```