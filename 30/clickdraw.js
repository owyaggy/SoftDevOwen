//retrieve node in DOM via ID
let c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2d object
let ctx = c.getContext("2d");

//init global state var
let mode = "rect";

let toggleMode = function (e) {
//let toggleMode = (e) => {
    console.log("toggling...");
    if (e.innerHTML == "rect|circ" || e.innerHTML == "Circle") {
        e.innerHTML = "Rect";
    }
    else {
        e.innerHTML = "Circle";
    }
}

let drawRect = function(e) {
    let mouseX = e.clientX;
    let mouseY = e.clientY;
    console.log("mouseclick registered at ", mouseX, mouseY);
}

//var drawCircle = function(e) {
let drawCircle = (e) => {
    let mouseX = e.clientX;
    let mouseY = e.clientY;
    console.log("mouseclick registered at ", mouseX, mouseY);

}

//var draw = function(e) {
let draw = (e) => {
    console.log("...drawing");
}

//var wipeCanvas = function() {
let wipeCanvas = () => {
    console.log("...wiping");
}

c.addEventListener("click", draw);
let bToggler = document.getElementById('buttonToggle');
bToggler.addEventListener("click", toggleMode);
let clearB = document.getElementById('buttonClear');
clearB.addEventListener("click", wipeCanvas);
