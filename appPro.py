from flask import Flask,jsonify,request
from prediction import get_prediction

app = Flask(__name__)
@app.route('/alpha_predict', methods = ['POST'])
def alpha_predict():
    image_file = request.files.get('alpha_img') #digit_img : upload img file
    prediction = get_prediction(image_file)
    return jsonify({'prediction_result':prediction }, 200)

    


if __name__ == "__main__":
    app.run(debug=True)

