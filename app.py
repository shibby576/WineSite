from flask import Flask, request, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb')) #model object

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    #get values from form and input into model
    sulfate = float(request.form["sulfate"])
    alcohol = float(request.form["alcohol"])
    prediction = model.predict([[sulfate, alcohol]])  
    output = round(prediction[0], 2) #prediction is a list, so select and round first value
    modified_output=''
    output_measure=0.0
    if output <.4 :
        output_measure = round(3+(output*5.013),0)
        modified_output = 'low'
    elif output < .6:
        output_measure = round(3+(output*5.025),0)
        modified_output='moderate'
    elif output < .8:
        output_measure = round(3+(output*5.013),0)
        modified_output='high'
    elif output < 1:
        output_measure = round(3+(output*5.013),0)
        modified_output='great'
    else:
        output_measure = round(3+(output*5.013),0)
        modified_output='superb'


    return render_template('index.html', prediction_text=f'Your wine has a predicted quality of {output_measure} and a rating of {modified_output}!')

if __name__ == "__main__":
    app.run()