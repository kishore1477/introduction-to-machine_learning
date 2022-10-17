from flask import Flask,  render_template,request,url_for
import joblib 
# from joblib import load
app = Flask(__name__)
# import pickle
@app.route("/")
def home(request=None):
    return render_template('index.html')
    # return "<p>Hello, World! kishore kumar </p>"
@app.route("/result", methods=['POST'])
def result():
    if request.method == 'POST':
        exp = request.form['exp']
        print("Experience",type(exp))
        print(exp)
        numExp = int(exp)
        print("Experience",type(numExp))
        print(numExp)
        # ml = pickle.load(open('pickle_of_MLmodel','rb'))
        # ml = load('/static/pickle_of_MLmodel')
        ml =joblib.load('pickle_of_MLmodel')
        predictedSalary =ml.predict([[numExp]])
        print(predictedSalary)
        # context = {"salary":predictedSalary}
        return render_template('result.html', salary =predictedSalary)



        print("POSt ha method")



    # data= request.form("exp")
    # print("data is:", data)

app.run(debug =True)    