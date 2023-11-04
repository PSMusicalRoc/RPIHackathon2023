let global_exercises = [];

let delimiter = ".......";

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

