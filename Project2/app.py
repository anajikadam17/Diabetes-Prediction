import pickle
from flask import Flask, render_template, url_for, request
app = Flask(__name__)


filename = 'pipeMinSc_StdSc.pkl'
filename1 = 'RFClr.pkl'

# load the model from disk
pipe= pickle.load(open(filename, 'rb'))
model = pickle.load(open(filename1, 'rb'))

@app.route("/", methods=['GET'])
@app.route("/home")
def home():
    return render_template('home.html', title='Home', show_bar = True)


@app.route("/about")
def about():
    return render_template('about.html', title='About', show_bar = True)

@app.route("/project", methods=['GET','POST'])
def project():
    if request.method == 'POST':
        Pregnancies = float(request.form['Pregnancies'])
        Glucose = float(request.form['Glucose'])
        BloodPressure = float(request.form['BloodPressure'])
        SkinThickness = float(request.form['SkinThickness'])
        Insulin = float(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = float(request.form['Age'])
        data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        #print(data)
        x_test2 = pipe.transform(data)
        output = model.predict(x_test2)
        prediction = output[0]
        if prediction==0:
            text = "Non Diabetes"
        else:
            text = "Diabetes"
        if True:
            return render_template('project.html',Data = data, Text = text)
        else:
            return render_template('project.html',prediction_text="You Can Sell Your Car at {} Lakhs".format(output))
    else:
        return render_template('project.html', title='Project | Home')

if __name__ == '__main__':
    app.run(debug=True)
