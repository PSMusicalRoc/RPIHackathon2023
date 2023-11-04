from flask import Flask, url_for, redirect, render_template, request, send_file, flash
import os
import shutil

this_file = __file__
app = Flask(__name__)


#called on startup
@app.route('/')
def startUp():

    #default values to start
    #print('base page', file=sys.stderr)

    return render_template('index.html') 

#downloads exercise file
#the file we should use should be uner the name Exercises.txt
@app.route('/downloadExercises/')
def downloadExercises():
    #print(f"PATH: {os.path.join(os.path.dirname(this_file), 'logfile.txt')}")
    return send_file(os.path.join(os.path.dirname(this_file), 'Exercises.txt'), as_attachment=True)

#upload new exercises file
@app.route('/uploadExercises/', methods = ['POST'])
def uploadExercises():
    if request.method == 'POST':
        file = request.files['sfile']
        file.save(file.filename)
        
        #delete and replace the file if it exists lol
        if os.path.exists(os.path.join(os.path.dirname(this_file), 'static/Exercises/Exercises.txt')):
            os.remove(os.path.join(os.path.dirname(this_file), 'static/Exercises/Exercises.txt'))
        shutil.copy(file.filename, os.path.join(os.path.dirname(this_file), 'static/Exercises/Exercises.txt'))

        #do stuff with file here...

        return redirect(url_for('/'))



#Starts a exercise session
@app.route('/startSession/', methods = ['POST'])
def startSession():
    if request.method == 'POST':

        #get field this from the form given from the frontend
        a = request.form['this']

        #do something with the given information

        return redirect(url_for('/'))

#adds an exercise
@app.route('/addExercise/', methods = ['POST'])
def addExercise():
    if request.method == 'POST':

        #add the exercise here
        return "String that represents the data structure for the frontend's use"

#removes an exercise
@app.route('/removeExercise/', methods = ['POST'])
def removeExercise():
    if request.method == 'POST':

        #remove the exercise here
        return "String that represents the data structure for the frontend's use"

#updates previous exercise from the tree, gets next exercise from the tree
@app.route('/getNextExercise/', methods = ['POST'])
def getNextExercise():
    if request.method == 'POST':

        #get previous exercise
        a = request.form['this_exercise']

        #update this_exercise's score in the data structure
        #get the next exercise
        return "String representing the next exercise"
