from fastapi import FastAPI
import pickle
from package.utils import from_number_to_flower
from package.iris import my_prediction_function

# FastAPI instance
app = FastAPI()

# Root endpoint
@app.get("/")
def root():
    return {'greeting':"hello"}

# Prediction endpoint
@app.get("/predict")
def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    # Use the function in our package to run the prediction
    prediction = my_prediction_function(sepal_length, sepal_width, petal_length, petal_width)
    flower_name = from_number_to_flower(int(prediction[0]))
    return {"prediction": flower_name}

    # Return prediction
    return from_number_to_flower({"prediction": int(prediction[0])})
