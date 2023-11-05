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
global temp_list
temp_list = []
global index

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
        global temp_list
        global main_list
        global index
        no_iterations = int(request.form['number-iterations'])
        no_exercises = int(request.form['number-exercises'])
        print(no_iterations)
        print(no_exercises)
        temp_list = Exercise.getExercises(main_list,no_exercises)
        index = 0
        #do something with the given information


        return redirect(url_for('render_session'))

@app.route('/render-session/')
def render_session():
    return render_template('doExercise.html')

#get prev exercise with score, update the tree (?), get the next exercise and send it to the frontend
#probably called from js to keep updating page
@app.route('/getNextExercise/', methods = ['POST'])
def getNextExercise():
    if request.method == 'POST':

        global no_exercises
        global no_iterations
        global index
        #get previous exercise
        exercise_name = request.form['this_exercise']
        exercise_score = request.form['this_score']
        if exercise_score != '':
            score = exercise_score/no_iterations
            #update this_exercise's score in the data structure
            Exercise.scoring(main_list, exercise_name, score)
        #send back string representation of exercise
        send = temp_list[index] + ';' + str(no_iterations)
        index += 1
        print('send', send)
        return send

        #get the next exercise



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

        global main_list
        new_exercise = request.form['new_exercise']

        #Jump:Hello;World;: is the format


        #add the exercise here
        Exercise.addExercise(main_list, new_exercise)

        return "String that represents the data structure for the frontend's use"

#removes an exercise
@app.route('/removeExercise/', methods = ['POST'])
def removeExercise():
    if request.method == 'POST':

        #remove the exercise here
        return "String that represents the data structure for the frontend's use"