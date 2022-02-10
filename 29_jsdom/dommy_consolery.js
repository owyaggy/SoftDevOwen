// Team Hagrio :: Liesel Wong, Owen Yaggy
// SoftDev pd1
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08t
// --------------------------------------------------

//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
// (or command-option-I on Mac)
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

// allows another list item to be added to the end of the list
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
    items[i].classList.replace('blue', 'red'); // adds red to the class for that element, but doesn't necessarily change primary color
      // attempted modifying "add" with "replace"; found somewhat better results
    //console.log(items[i].classList); // for testing
  }
};

// if functioning, alternates colors of list items between red and blue
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
let fib = function fib(n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n -2)
}
// FAC
let fac = function fac(n) {
    if (n > 1) return n * fac(n - 1);
    return n;
}
// GCD
let gcd = function gcd(a, b) {
    a = Math.abs(a);
    b = Math.abs(b);
    if (b == 0) return a;
    return gcd(b, a % b);
}

// function to add fib output to dom
let showFib = function showFib(n) {
    let items = document.body; // assigns the entire document body to a variable
    let element = document.createElement('h1'); // creates a new h1 tag
    element.innerHTML = `Fibonacci number ${n} is ${fib(n)}!` // inserts gcd text in that tag
    items.append(element); // adds that tag to the end of the body (this is what displays it!)
    return element; // returns the tag (this is for debugging in console!)
}

// function to add fac output to dom
let showFac = function showFac(n) {
    let items = document.body; // assigns the entire document body to a variable
    let element = document.createElement('h1'); // creates a new h1 tag
    element.innerHTML = `The factorial of ${n} is ${fac(n)}!` // inserts gcd text in that tag
    items.append(element); // adds that tag to the end of the body (this is what displays it!)
    return element; // returns the tag (this is for debugging in console!)
}

// function to add gcd output to dom
let showGCD = function showGCD(a, b) {
    let items = document.body; // assigns the entire document body to a variable
    let element = document.createElement('h1'); // creates a new h1 tag
    element.innerHTML = `The gcd of ${a} and ${b} is ${gcd(a, b)}!` // inserts gcd text in that tag
    items.append(element); // adds that tag to the end of the body (this is what displays it!)
    return element; // returns the tag (this is for debugging in console!)
}

//showGCD(34, 58); // runs the function to display the gcd

let FIBbut = document.getElementById("b1");
let FACbut = document.getElementById("b2");
let GCDbut = document.getElementById("b3"); // "b" is the html id of the button

//dasbut.addEventListener('dblclick', showGCD(parseInt(Math.random()* 200), parseInt(Math.random()* 200)));
let FIBhelper = function FIBhelper() {
    return showFib(parseInt(Math.random()* 50));
}

let FAChelper = function FAChelper() {
    return showFac(parseInt(Math.random()* 10));
}

let GCDhelper = function GCDhelper() {
    return showGCD(parseInt(Math.random()* 200), parseInt(Math.random()* 200));
}

FIBbut.addEventListener('click', FIBhelper);
FACbut.addEventListener('click', FAChelper);
GCDbut.addEventListener('click', GCDhelper);
