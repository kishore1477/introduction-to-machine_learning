from flask import Flask,  render_template
app = Flask(__name__)

@app.route("/")
def hello_world(request=None):
    return render_template('index.html')
    # return "<p>Hello, World! kishore kumar </p>"
@app.route("/result", methods=['POST'])
def result(request=None):
    data= request.form("exp")
    print("data is:", data)
    return render_template('result.html')

app.run(debug =True)    