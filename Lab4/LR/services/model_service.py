from ml.model import ValuePredictModel
import numpy
import pandas as pd

MODEL = ValuePredictModel()


def predict_apartment_value(test_data_json_str):
    pd_test_data = pd.read_json(test_data_json_str)
    prediction: numpy.ndarray = MODEL.predict(pd_test_data)
    return prediction.flatten().tolist()
