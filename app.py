import pickle
import numpy as np
from flask import Flask, render_template
from flask import Flask, flash, request, redirect, url_for, render_template
app=Flask(__name__)
sc=pickle.load(open('sc.pkl','rb'))
model=pickle.load(open('classi.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/next',methods=['POST','GET'])
def next():
    if request.method=='POST':
         name=request.form.get('nam')
         nap=float(request.form['pregnets'])
         glucose=float(request.form['glucose'])
         BP=float(request.form['BP'])
         insu=float(request.form['Insulin'])
         bmi=float(request.form['Bmi'])
         pf=float(request.form['Pedigree'])
         age=float(request.form['age'])
         st=float(request.form['st'])
         print(np.array([nap,glucose,BP,st,insu,bmi,pf,age]).reshape(1,-1))
         pred=model.predict(np.array([nap,glucose,BP,st,insu,bmi,pf,age]).reshape(1,-1))
         return render_template('next.html',nal=name,r=pred,age=age)
    return render_template('next.html')
@app.route('/diet',methods=['POST'])
def diet():
    if request.method=="POST":
        age=float(request.form['Diet'])
        if(age>0 and age<26):
            return render_template('25.html')
        elif(age>50):
            return render_template('50.html')
        else:
            return render_template('30.html')

   

if __name__=="__main__":
    app.run(debug=True)


