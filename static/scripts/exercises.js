let global_exercises = [];

const default_score = 0.2;

let layer_delim = ":";
let name_delim = ";";
let action_delim = "......";

class ExerciseDataStruct {
    constructor(name, layers) {
        this.name = name;

        // This is an array of arrays of strings
        this.layers = layers;
    }
}

class ExerciseNode {
    constructor(name, score)
    {
        this.name = name;
        this.score = score;
    }
}

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
                    global_exercises = parseBackendString(request.responseText);
                    populateExercises(request.responseText);
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

function addExercise()
{
    let ename = document.getElementById("add-new-exercise").value;
    let ename_nows = ename.replace(/\s/g,'');

    if (ename_nows == "") return;
    if (global_exercises.includes(ename)) return;

    global_exercises = global_exercises.concat(ename, "0.2");
    populateExercises(generateExerciseString(global_exercises));

    document.getElementById("add-new-exercise").value = "";
}

function toggleDropdown(index) {
    let exercise = document.getElementsByClassName("exercise")[index];
    if (exercise.getElementsByClassName("dropdown-menu").length == 0)
    {
        // dropdown menu does not exist at the moment, swap
        let menu = exercise.getElementsByClassName("dropdown-hidden")[0];
        menu.classList = "dropdown-menu";

        exercise.getElementsByClassName("dropdown")[0].setAttribute("style", "display:none;");
        exercise.getElementsByClassName("pullup")[0].setAttribute("style", "");

        exercise.classList = "exercise no-height-limit";
    }
    else
    {
        // dropdown exists, swap
        let menu = exercise.getElementsByClassName("dropdown-menu")[0];
        menu.classList = "dropdown-hidden";

        exercise.getElementsByClassName("dropdown")[0].setAttribute("style", "");
        exercise.getElementsByClassName("pullup")[0].setAttribute("style", "display:none;");

        exercise.classList = "exercise";
    }
}

function parseBackendString(str) {
    let output = [];
    let actions = str.split(action_delim);
    if (actions[actions.length - 1].length == 0)
    {
        actions.pop();
    }

    for (i = 0; i < actions.length; i++)
    {
        let layers = actions[i].split(layer_delim);
        if (layers[layers.length - 1].length == 0)
        {
            layers.pop();
        }

        let inlayers = [];
        
        for (j = 1; j < layers.length; j++)
        {
            let names = layers[j].split(name_delim);
            if (names[names.length - 1].length == 0)
            {
                names.pop();
            }
            let temp = [];
            for (k = 0; k < names.length; k+=2)
            {
                temp.push(new ExerciseNode(names[k], names[k+1]));
            }
            inlayers.push(temp);
        }
        let toplevel = layers[0].split(name_delim);

        let exercise = new ExerciseDataStruct(new ExerciseNode(toplevel[0], toplevel[1]), inlayers);
        output.push(exercise);
    }

    return output;
}

function generateBackendString(exercises)
{
    // reverse of parseBackendString()
    // make sure to test that each layer has something
    // in it, otherwise remove it
}

function populateExercises(input_str)
{
    if (global_exercises.length == 0)
    {
        global_exercises = parseBackendString(input_str);
    }

    let exerciseColumn = document.getElementsByClassName("exercise-col").item(0);
    let elementsToBeRemoved = document.getElementsByClassName("exercise");
    while (elementsToBeRemoved[0])
        elementsToBeRemoved[0].parentNode.removeChild(elementsToBeRemoved[0]);

    for (e = 0; e < global_exercises.length; e++)
    {
        let data = global_exercises[e];

        let exercise = document.createElement("div");
        exercise.setAttribute("class", "exercise");

        let standardvis = document.createElement("div");
        standardvis.setAttribute("class", "standard");

        let dropdownvis = document.createElement("div");
        dropdownvis.setAttribute("class", "dropdown-hidden");

        for (i = 0; i < data.layers.length; i++) {
            let label = document.createElement("p");
            label.setAttribute("style", "font-size: 20px");
            label.innerHTML = "Layer " + (i + 1).toString();
            dropdownvis.appendChild(label);

            let text = "";
            for (j = 0; j < data.layers[i].length; j++)
            {
                if (j != 0) text += ", ";
                text += data.layers[i][j].name + " (" + data.layers[i][j].score + ")";
            }
            let radio = document.createElement("p");
            radio.innerHTML = text;
            dropdownvis.appendChild(radio);
        }

        let ename = document.createElement("p");
        ename.innerHTML = data.name.name + " (" + data.name.score + ")";
        ename.setAttribute("class", "name");
        standardvis.appendChild(ename);

        let dropdownbutton = document.createElement("button");
        dropdownbutton.setAttribute("class", "dropdown");
        dropdownbutton.setAttribute("onclick", "toggleDropdown(" + e.toString() + ");");
        standardvis.appendChild(dropdownbutton);

        let pullupbutton = document.createElement("button");
        pullupbutton.setAttribute("class", "pullup");
        pullupbutton.setAttribute("style", "display:none;");
        pullupbutton.setAttribute("onclick", "toggleDropdown(" + e.toString() + ");");
        standardvis.appendChild(pullupbutton);

        let deletebutton = document.createElement("button");
        deletebutton.setAttribute("class", "delete");
        standardvis.appendChild(deletebutton);

        exercise.appendChild(standardvis);
        exercise.appendChild(dropdownvis);

        exerciseColumn.appendChild(exercise);
    }
}

function beginTraining() {
    let number_iterations = document.getElementById("number-iterations").value;
    let number_exercises = document.getElementById("number-exercises").value;

    let formdata = new FormData();
    formdata.set("number-iterations", number_iterations);
    formdata.set("number-exercises", number_exercises);

    const request = new XMLHttpRequest();
    request.onreadystatechange = async function() {
        if (request.readyState == 4 && request.status == 200) {
            console.log(request.responseText);
        } else if (request.readyState == 4 && request.status != 200) {
            console.log('ERROR: ' + request.responseText)
        }
    }
    request.open("POST", "/startSession", true);
    request.send(formdata);
}
