from flask import Flask, url_for, redirect, render_template, request, send_file, flash
import os
import shutil
import Exercise


this_file = __file__
app = Flask(__name__)
global main_list
global no_iterations 
global no_exercises
main_list = []

#called on startup
@app.route('/')
def startUp():
    global main_list
    #default values to start
    #print('base page', file=sys.stderr)
    print(main_list)

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


        #get main list of data from frontend (from file)
        global main_list
        main_list = Exercise.parse(file.filename)
        s = ''
        for e in main_list:
            s += e.toSendString(e) + '......'

        #sending back - should be "excercise;score;exercise;score;:exercise;score......"

        print(s)

        return s



#Starts a exercise session
@app.route('/startSession/', methods = ['POST'])
def startSession():
    if request.method == 'POST':

        #get field this from the form given from the frontend
        global no_iterations
        global no_exercises
        no_iterations = int(request.form['number-iterations'])
        no_exercises = int(request.form['number-exercises'])
        print(no_iterations)
        print(no_exercises)
        #do something with the given information


        return redirect(url_for('/render-session'))

@app.route('/render-session/')
def render_session():
    return render_template('doExercise.html')

#get prev exercise with score, update the tree (?), get the next exercise and send it to the frontend
#probably called from js to keep updating page
@app.route('/getNextExercise/', methods = ['POST'])
def getNextExercise():
    if request.method == 'POST':

        #get previous exercise
        exercise_name = request.form['this_exercise']
        exercise_score = float(request.form[''])
        #update this_exercise's score in the data structure
        #get the next exercise
        return "String representing the next exercise"

#called when session finishes
@app.route('/resultsRedirect/')
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

        #Jump:Hello;World;: is the format
        #add the exercise here
        return "String that represents the data structure for the frontend's use"

#removes an exercise
@app.route('/removeExercise/', methods = ['POST'])
def removeExercise():
    if request.method == 'POST':

        #remove the exercise here
        return "String that represents the data structure for the frontend's use"