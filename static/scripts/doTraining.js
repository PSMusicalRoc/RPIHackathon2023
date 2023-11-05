function getNextExercise(firsttime) {
    let numInput = document.getElementById("num-correct").value;
    let currentExerciseHTML = document.getElementById("exercise-path");
    let currentRepetitionsHTML = document.getElementById("exercise-reps");

    let formdata = new FormData();

    if (firsttime)
    {
        formdata.set("this_exercise", "");
        formdata.set("this_score", "");
    }
    else
    {
        formdata.set("this_exercise", currentExerciseHTML.value);
        formdata.set("this_score", numInput);
    }

    const request = new XMLHttpRequest();
    request.onreadystatechange = async function() {
        if (request.readyState == 4 && request.status == 200) {
            document.getElementById("exercise-to-do").innerHTML = "Shit and Fuck";
            document.getElementById("number-reps-text").innerHTML = "Do " + currentRepetitionsHTML.value.toString() + " Reps";
            document.getElementById("num-correct").value = "";
        } else if (request.readyState == 4 && request.status != 200) {
            console.log('ERROR: ' + request.responseText)
        }
    }
    request.open("POST", "/getNextExercise", true);
    request.send(formdata);
}