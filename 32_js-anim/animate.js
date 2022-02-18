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
  //console.log("clear invoked...");
  // YOUR CODE HERE
};

let xspeed;
let yspeed;
let xpos;
let ypos;

let dvdPlayer = new Image();
dvdPlayer.src = 'logo_dvd.jpg';

var screenHelper = (e) => {
  xpos = 50 + Math.random() * 350;
  ypos = 50 + Math.random() * 350;
  xspeed = 0.5 + Math.random();
  yspeed = 0.5 + Math.random();
  screenSaver();
}

//var drawDot = function() {
var screenSaver = (e) => {

  //console.log("drawDot invoked...");
  clear();
  //console.log(`xpos: ${xpos}`)
  //console.log(`ypos: ${ypos}`)
  xpos += xspeed;
  ypos += yspeed;
  if (xpos >= c.width-92 || xpos <= -5) xspeed *= -1;
  if (ypos >= c.height-80 || ypos <= -20) yspeed *= -1;
  /*ctx.beginPath();
    ctx.moveTo(xpos, ypos);
    ctx.lineTo(xpos + 50, ypos);
    ctx.lineTo(xpos + 50, ypos - 50);
    ctx.lineTo(xpos, ypos - 50);
    ctx.closePath();
    ctx.stroke();*/
  ctx.drawImage(dvdPlayer, xpos, ypos, 100, 100);
  //ctx.rect(xpos+5, ypos+20, 87, 60);
  //ctx.stroke();
  window.cancelAnimationFrame(requestID);
  requestID = window.requestAnimationFrame(screenSaver);

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
  //console.log("stopIt invoked...")
  //console.log( requestID );
  window.cancelAnimationFrame(requestID);

  // YOUR CODE HERE
  /*
    ...to
    Stop the animation

    You will need
    window.cancelAnimationFrame()
  */
};

dotButton.addEventListener( "click", screenHelper );
stopButton.addEventListener( "click",  stopIt );
