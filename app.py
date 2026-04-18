from flask import Flask,render_template,request
from src.pipeline.predict_pipeline import CustomData

application = Flask(__name__)
app = application 

@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/predictdata',methods = ['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        customData = CustomData(
            request.form['Select_Gender'],
            request.form['Race_or_Ethnicity'],
            request.form['Parental_Level_of_Education'],
            request.form['Lunch_Type'],
            request.form['Test_preparation_Course'],
            float(request.form['writing_name']),
            float(request.form['reading_name'])
        )
        result = customData.data()
        return render_template('home.html',results = result[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)