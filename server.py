from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import os
import pandas as pd
import shutil
import numpy as np
from main import classsification
import time

UPLOAD_FOLDER = 'data/'
new_data='new_data'
old_data='old_data'
app = Flask(__name__)
app.config.from_object(__name__)
Bootstrap(app)
app.config['UPLOAD_FOLDER_new'] = UPLOAD_FOLDER+new_data+'/'
data={'data1':0,'data2':0,'data3':0}

i=0
c0=0
c1=0
c2=0

@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/upload',methods = ['GET', 'POST'])
def upload():
    
    if request.method == 'POST':
	
        global i
        global data
        global c0
        global c1
        global c2
		
        temp1=c0
        temp2=c1
        temp3=c2
		
		
        file_dir = './'+UPLOAD_FOLDER+old_data+'/'+str(i)+'.csv'
        f = request.files['file_classify']
        f.save(os.path.join(app.config['UPLOAD_FOLDER_new'], f.filename))
        csvfile = os.listdir(UPLOAD_FOLDER+new_data)

        os.rename(UPLOAD_FOLDER+new_data+'/'+csvfile[0],UPLOAD_FOLDER+new_data+'/'+str(i)+'.csv')
		
        shutil.move(UPLOAD_FOLDER+new_data+'/'+str(i)+'.csv',UPLOAD_FOLDER+old_data)
        
        c0,c1,c2 = classsification(file_dir)

        data={'data1':c0+temp1,'data2':c1+temp2,'data3':c2+temp3}
        
        
        i+=1
        return render_template('dashboard.html',data=data)
		
@app.route('/dashboard')
def dashboard():
    global data
    return render_template('dashboard.html',data=data)
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug = False)
	 
    # c0= classsification(UPLOAD_FOLDER+new_data+'/test_data_2.csv')
     #print(c0)
   # file_dir = UPLOAD_FOLDER+old_data+'/'+str(i)+'.csv'
   # c1,c2,c3=m.classsification(file_dir)
    #print(UPLOAD_FOLDER+old_data+'/'+str(i)+'.csv')
    #c0,c1,c2=m.classsification(UPLOAD_FOLDER+old_data+'/'+str(i)+'.csv')
   # print(c0,c1,c2