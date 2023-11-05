let global_exercises = [];

let delimiter = ".......";

function fileChanged()
{
    let file = document.getElementById("file-upload").files[0];
    file.text().then(
        (str) => {
            let formdata = new FormData;
            formdata.append("input", file);

            const request = new XMLHttpRequest();
            request.onreadystatechange = async function() {
                if (request.readyState == 4 && request.status == 200) {
                    console.log(request.responseText)
                } else if (request.readyState == 4 && request.status != 200) {
                    console.log('ERROR: ' + request.responseText)
                }
            }
            request.open("POST", "/uploadExercises",true);
            request.send(formdata);
        },
        (str) => {console.log("There was an error: " + str);}
    );
}

function populateExercises(exercises)
{
    global_exercises = exercises;

    let exerciseColumn = document.getElementsByClassName("exercise-col").item(0);
    for (e in exercises)
    {
        let exercise = document.createElement("div");
        exercise.setAttribute("class", "exercise");

        let standardvis = document.createElement("div");
        standardvis.setAttribute("class", "standard");


        let ename = document.createElement("p");
        ename.innerHTML = exercises[e];
        ename.setAttribute("class", "name");
        standardvis.appendChild(ename);

        let editbutton = document.createElement("button");
        editbutton.setAttribute("class", "edit");
        standardvis.appendChild(editbutton);

        let excludebutton = document.createElement("button");
        excludebutton.setAttribute("class", "exclude");
        standardvis.appendChild(excludebutton);

        let deletebutton = document.createElement("button");
        deletebutton.setAttribute("class", "delete");
        standardvis.appendChild(deletebutton);

        exercise.appendChild(standardvis);

        exerciseColumn.appendChild(exercise);
    }
}

