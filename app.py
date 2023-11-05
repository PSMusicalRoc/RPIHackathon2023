from flask import Flask, url_for, redirect, render_template, request, send_file, flash
import os
import shutil
import Exercise


this_file = __file__
app = Flask(__name__)
main_list = []

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
        file = request.files['input']
        file.save(file.filename)
        
        #delete and replace the file if it exists lol
        if os.path.exists(os.path.join(os.path.dirname(this_file), 'static/Exercises/Exercises.txt')):
            os.remove(os.path.join(os.path.dirname(this_file), 'static/Exercises/Exercises.txt'))
        shutil.copy(file.filename, os.path.join(os.path.dirname(this_file), 'static/Exercises/Exercises.txt'))

        outfile = open(file.filename)
        main_list = Exercise.parse(file.filename)
        for e in main_list:
            print(''.join(e.toSendStringCaller()))
        #do stuff with file here...

        #sending back - should be "excercise:score;exercise:score;exercise:score......"

        'Jump: Full Hop Fast Fall Fair Forward 1:0.5;'


        return "obama"



#Starts a exercise session
@app.route('/startSession/', methods = ['POST'])
def startSession():
    if request.method == 'POST':

        #get field this from the form given from the frontend
        a = request.form['this']

        #do something with the given information

        return redirect(url_for('/'))



#get prev exercise with score, update the tree (?), get the next exercise and send it to the frontend
#probably called from js to keep updating page
@app.route('/getNextExercise/', methods = ['POST'])
def getNextExercise():
    if request.method == 'POST':

        #get previous exercise
        a = request.form['this_exercise']

        #update this_exercise's score in the data structure
        #get the next exercise
        return "String representing the next exercise"

#called when session finishes
@app.route('/resultsRedirect')
def resultsRedirect():
    return redirect(url_for('/showResults'))

#returns results information
@app.route('/showResults/')
def showResults():

    return 'results string'



#######################################################################################################################################
########################################################   DO LATER   #################################################################
#######################################################################################################################################


#fuck you use our input file
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