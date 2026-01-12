
from flask import Flask, render_template, jsonify, request, send_file
from src.exception import CustomException
from src.logger import logging as lg
import os,sys


from src.pipeline.train_pipeline import TrainingPipeline
from src.pipeline.predict_pipeline import PredictionPipeline


app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to my App"




@app.route("/train") # when we hit this route, training should start.
def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()


        return "Training completed successfully."
    except Exception as e:
        raise CustomException(e, sys)
    

@app.route("/predict", methods=['POST', 'GET'])
def upload():

    try:

        if request.method == 'POST':
            # it is a object of prediction pipeline.
            predict_pipeline = PredictionPipeline(request)

            # now we are running this run pipeline method
            prediction_file_detail = predict_pipeline.run_pipeline()
            # calling the run_pipeline method of prediction pipeline.
            

            lg.info("prediction completed. Downloading prediction file")
            return send_file(prediction_file_detail.prediction_file_path,
                             download_name= prediction_file_detail.prediction_file_name,
                             as_attachment=True)
        # all the files will be saved and new "prediction file" will be created.


        else:
            return render_template('upload_file.html')
    except Exception as e:
        raise CustomException(e, sys)
    




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)