
from flask import Flask, render_template, redirect, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def reg():
    return render_template('register.html')

@app.route('/register', methods=['GET',"POST"])
def register():
    return render_template('araa.html')

    

@app.route('/araa', methods=['GET',"POST"])
def home():
    
    if request.method == "POST":
        num1 = request.form.get('age')
        num2 = request.form.get('smoke')
        num3 = request.form.get('alcohol')
        num4 = request.form.get('waist')
        num5 = request.form.get('activity')
        num6 = request.form.get('history')
        add = float(num1) + float(num2)+float(num3)+float(num4) + float(num5)+float(num6)
        return render_template('result.html', add=add)
    return render_template('araa.html')



@app.route('/back',methods=['POST','GET'])
def back():
    if request.method=='POST':
        return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)