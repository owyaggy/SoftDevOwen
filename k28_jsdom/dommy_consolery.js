/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-J in Firefox to reveal console)
console.log("AYO");

let i = "hello";
let j = 20;


//assign an anonymous fxn to a let
// can enter f(x) in console to return 30 + x
let f = function(x) {
  let j=30;
  return j+x;
};


//instantiate an object
let o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) { // can be accessed using o['func'](x) to return 30 + x
            return x+30;
          }
        };


let addItem = function(text) {
  let list = document.getElementById("thelist");
  let newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

// removes list item n in the dom and live html page
let removeItem = function(n) {
  let listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


let red = function() {
  let items = document.getElementsByTagName("li");
  for(let i = 0; i < items.length; i++) { // loops through all items in list
    items[i].classList.add('red'); // adds red to the class for that element
    console.log(items[i].classList);
  }
};


let stripe = function() {
  let items = document.getElementsByTagName("li");
  for(let i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
// FAC
// GCD
