import json
import werkzeug
from flask import Flask
from flask import request
from services.model_service import predict_apartment_value


app = Flask(__name__)


@app.route('/predict')
def predict():
    test_data = request.data.decode('utf-8')
    prediction = predict_apartment_value(test_data)
    return json.dumps(prediction)


@app.errorhandler(werkzeug.exceptions.HTTPException)
def handle_error(e):
    response = e.get_response()
    response.data = json.dumps({"errMessage": "Error. Check data format!"})
    response.content_type = "application/json"
    return response
