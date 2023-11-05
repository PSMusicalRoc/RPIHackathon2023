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
            let values = request.responseText.split(";");
            let redirectcheck = request.responseText.split("......redirect......");

            if (redirectcheck.length == 2 && redirectcheck[0].length == 0)
            {
                document.open();
                document.write(redirectcheck[1]);
                document.close();
                return;
            }
            else {
                currentRepetitionsHTML.value = values[1];
                currentExerciseHTML.value = values[0];
                document.getElementById("exercise-to-do").innerHTML = parseExerciseName(values[0]);
                document.getElementById("number-reps-text").innerHTML = "Do " + currentRepetitionsHTML.value.toString() + " Reps";
                document.getElementById("num-correct").value = "";
            }
        } else if (request.readyState == 4 && request.status != 200) {
            console.log('ERROR: ' + request.responseText)
        }
    }
    request.open("POST", "/getNextExercise", true);
    request.send(formdata);
}

function parseExerciseName(str) {
    let values = str.split(",");
    let output = "";
    for (i = values.length - 1; i >= 0; i--)
    {
        output += values[i];
        if (i != 0) output += " ";
    }
    return output;
}

function triggerDownloadConfig() {
    if (request.readyState == 4 && request.status == 200) {
        let values = request.responseText.split(";");
        currentRepetitionsHTML.value = values[1];
        currentExerciseHTML.value = values[0];
        document.getElementById("exercise-to-do").innerHTML = parseExerciseName(values[0]);
        document.getElementById("number-reps-text").innerHTML = "Do " + currentRepetitionsHTML.value.toString() + " Reps";
        document.getElementById("num-correct").value = "";
    } else if (request.readyState == 4 && request.status != 200) {
        console.log('ERROR: ' + request.responseText)
    }
    request.open("GET", "/downloadExercises", true);
    request.send();
}