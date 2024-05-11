from flask import Flask, request, jsonify
import numpy as np
from final import model
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')


# Function to process input and return result
def get_result(lang_vocab, memory, speed, visual, audio, survey):
    # 2D numpy array created with the values input by the user
    array = np.array([[lang_vocab, memory, speed, visual, audio, survey]])
    # The output given by model is converted into an int and stored in label
    label = int(model.predict(array))
    # Giving final output to user depending upon the model prediction
    if label == 0:
        output = "There is a high chance of the applicant to have dyslexia."
    elif label == 1:
        output = "There is a moderate chance of the applicant to have dyslexia."
    else:
        output = "There is a low chance of the applicant to have dyslexia."
    return output

# Route to handle user input
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print(data)
    lang_vocab = float(data['lang_vocab'])
    memory = float(data['memory'])
    speed = float(data['speed'])
    visual = float(data['visual'])
    audio = float(data['audio'])
    survey = float(data['survey'])
    result = get_result(lang_vocab, memory, speed, visual, audio, survey)
    return jsonify({'result': result})

@app.route("/")
def index():
    return {"status":200,"message":"Dyslexia"}

if __name__=="__main__":
    app.run(debug=True) 