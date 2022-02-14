//retrieve node in DOM via ID
let c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2d object
let ctx = c.getContext("2d");

//init global state var
let mode = "rect";

let toggleMode = function (e) {
//let toggleMode = (e) => {
    console.log("toggling...");
    console.log(e);
    if (mode === "rect") {
        mode = "circ";
        e.target.innerHTML = "Circle";
    }
    else {
        mode = "rect";
        e.target.innerHTML = "Rect";
    }
}

let drawRect = function(e) {
    let mouseX = e.clientX;
    let mouseY = e.clientY;
    console.log("rect mouseclick registered at ", mouseX, mouseY);
}

//var drawCircle = function(e) {
let drawCircle = (e) => {
    let mouseX = e.clientX;
    let mouseY = e.clientY;
    console.log("circle mouseclick registered at ", mouseX, mouseY);
}

//var draw = function(e) {
let draw = (e) => {
    console.log("...drawing");
    if (mode === "rect") drawRect(e);
    if (mode === "circ") drawCircle(e);
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
