#creating a localhost 
#working 
'''
create a directory named "Webapp"\
Webapp
    app.py
    cnn.py
    templates
        index.html
        result.html
    static 
        main.css
'''
from flask import Flask, render_template, request,redirect, url_for
from flask import send_from_directory
from werkzeug import secure_filename
import os,shutil

global result


app= Flask(__name__)


@app.route("/") #GET information
def index():
	return render_template("index.html")


@app.route("/result", methods=['POST','GET'])
def result():
    if request.method == 'POST' :
        f=request.files['file']
        f.save(secure_filename(f.filename))
        shutil.move(f.filename, "os.getcwd/static"+f.filename) # as the file we save will be in directory we need to move to static 
        #make sure that cnn.py is in the same directory created
        import cnn
        result =cnn.test(f.filename)
        print(result)
        return render_template('result.html',value =result, filename = str("../static/"+f.filename))
        



if __name__=='__main__':
	app.run(debug =True)

