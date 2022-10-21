
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/fail/<string:s>')
def fail(s):
     return s

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score > 4:
        res = " screening needed"
    else:
        res = "no screening needed"

    return render_template('result.html', result=res)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    count = 0
    if request.method == 'POST':
        
        age = int(request.form["age"])
        if (age >= 30 and age <= 39):
            count += 0
            
        elif (age >= 40 and age <= 49):
            count = count+1
            
        elif (age >= 50 and age <= 59):
            count += 2
            
        elif(age>=60):
            count += 3
        else:
            return redirect(url_for('fail',s="invalid"))    
     
         
        print("count 1", count)
        smoke = (request.form["smoke"])
        if (smoke.lower() == "never"):
            count += 0
            
        elif ((smoke.lower() == "used to consume in past") or (smoke.lower() == "sometime now")):
            count += 1
            
        elif (smoke.lower() == "daily"):
            count += 2
            
        else:
            return redirect(url_for('fail',s="invalid"))
            
    
        print("count 2", count)
        alcohol = (request.form["alcohol"])
        
        if (alcohol.lower() == "yes"):
            count = count+0
            
        elif (alcohol.lower() == "no"):
            count = count+1
            
        else:
            return redirect(url_for('fail',s="invalid"))
            
    
        print("count 3", count)
        
        gender = (request.form["gender"])
        waist_measurement = int(request.form["waist"])

        
        if (gender.lower() == "male"):
            if (waist_measurement <= 90):
                count = count+0
                
            elif (waist_measurement > 90 and waist_measurement <= 100):
                count = count+1
                
            elif (waist_measurement > 100):
                count += 2
                

        elif (gender.lower() == "female"):
            if (waist_measurement <= 80):
                count = count+0
                
            elif (waist_measurement > 80 and waist_measurement <= 90):
                count = count+1
                
            elif (waist_measurement > 90):
                count += 2
                
        else:
            return redirect(url_for('fail',s="invalid"))
            
        print("count 4", count)
        physical_activity = int(request.form["activity"])
       
        if (physical_activity >= 150):
            count = count+0
            
        elif (physical_activity < 150):
            count = count+1
            
        else:
            return redirect(url_for('fail',s="invalid"))
            
    
        print("count 5", count)
        history = (request.form["history"])
       
        if (history.lower() == "no"):
            count = count+0
            
        elif (history.lower() == "yes"):
            count = count+2
            
        else:
            return redirect(url_for('fail',s="invalid"))
            
        

        print("count 6", count)

        # ADDITION OF TOTAL SCORE

        # tot_score1 = (age1+waist1+activity1)
     
    res = " "
    return redirect(url_for('success', score=count))


if __name__ == '__main__':
    app.run(debug=True, port=8080)
