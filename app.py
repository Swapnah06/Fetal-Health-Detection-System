import os
from flask import Flask, render_template, url_for, request
import sqlite3
import shutil
from detect import Start
import cv2

from get_rem import get_abnormality_info


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/userlog', methods=['GET', 'POST'])
def userlog():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        query = "SELECT name, password FROM user WHERE name = '"+name+"' AND password= '"+password+"'"
        cursor.execute(query)

        result = cursor.fetchall()

        if len(result) == 0:
            return render_template('index.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')
        else:
            return render_template('userlog.html')

    return render_template('index.html')


@app.route('/userreg', methods=['GET', 'POST'])
def userreg():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        
        print(name, mobile, email, password)

        command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT)"""
        cursor.execute(command)

        cursor.execute("INSERT INTO user VALUES ('"+name+"', '"+password+"', '"+mobile+"', '"+email+"')")
        connection.commit()

        return render_template('index.html', msg='Successfully Registered')
    
    return render_template('index.html')

@app.route('/userlog.html')
def userlogg():
    return render_template('userlog.html')



@app.route('/image', methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
 
        dirPath = "static/images"
        fileList = os.listdir(dirPath)
        for fileName in fileList:
            os.remove(dirPath + "/" + fileName)
        fileName=request.form['filename']
        dst = "static/images"
    
        
            
        shutil.copy("test/"+fileName, dst)
        print(f"readed file {fileName}")
        path='static/images/'+fileName
        print(f"\n\n {path}\n\n")
        image = cv2.imread("test/"+fileName)

        
        Start(path)
        
        lst=[]
        rem=[]
        with open("check.txt", 'r') as file:
            content = file.readline()
        print(content)
        if not content:
            print("File is empty.")
        else:
            info = get_abnormality_info(content)
            cause=info['cause']
            pre=info['prevention']


                
        
        
        return render_template('results.html', content=content,cause=cause,pre=pre,
                               ImageDisplay="http://127.0.0.1:5000/static/images/"+fileName,
                               ImageDisplay4="http://127.0.0.1:5000/static/out.jpg"
                               )
        
    return render_template('userlog.html')

@app.route('/logout')
def logout():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
