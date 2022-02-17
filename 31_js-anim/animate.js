// Team Hagrio :: Liesel Wong (King Hagrid), Owen Yaggy (Rio)
// SoftDev pd0
// K31 -- canvas based JS animation
// 2022-02-15

// model for HTML5 canvas-based animation


//access canvas and buttons via DOM
var c = document.getElementById("playground");// GET CANVAS
var dotButton = document.getElementById("buttonCircle");// GET DOT BUTTON
var stopButton = document.getElementById("buttonStop");// GET STOP BUTTON

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d")// YOUR CODE HERE

//set fill color to team color
ctx.fillStyle = 'cyan';// YOUR CODE HERE

var requestID;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
  ctx.clearRect(0, 0, c.width, c.height);
  console.log("clear invoked...");
  // YOUR CODE HERE
};

var radius = 0;
var growing = true;

//var drawDot = function() {
var drawDot = (e) => {
  console.log("drawDot invoked...");
  clear();
  if (growing && radius >= 250) {
    growing = false;
  }
  if (!growing && radius <= 0) {
    growing = true;
  }
  ctx.beginPath(); // d-man = genius
  ctx.arc(250, 250, radius, 0, 2 * Math.PI);
  ctx.fill();
  ctx.closePath();
  if (growing) { 
    radius += 1;
  }
  else {
    radius -= 1; 
  }
  requestID = window.requestAnimationFrame(drawDot);

  // YOUR CODE HERE

  /*
    ...to
    Wipe the canvas,
    Repaint the circle,

    ...and somewhere (where/when is the right time?)
    Update requestID to propagate the animation.
    You will need
    window.cancelAnimationFrame()
    window.requestAnimationFrame()

   */
};


//var stopIt = function() {
var stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );
  window.cancelAnimationFrame(requestID);

  // YOUR CODE HERE
  /*
    ...to
    Stop the animation

    You will need
    window.cancelAnimationFrame()
  */
};


dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
