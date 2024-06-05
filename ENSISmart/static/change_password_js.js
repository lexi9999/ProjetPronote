const myInput = document.querySelector("#psw");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");
const validation = document.querySelector("#validation");
const change_form = document.querySelector(".change")

// When the user clicks on the password field, show the message box
myInput.addEventListener('focus', function() {
    validation.classList.add("upped");
    validation.classList.remove("notupped");
    change_form.classList.add("upped");
});

// When the user clicks outside of the password field, hide the message box
myInput.addEventListener('blur', function() {
    validation.classList.remove("upped");
    validation.classList.add("notupped");
    change_form.classList.remove("upped");
});


// When the user starts to type something inside the password field
myInput.addEventListener ('keyup', function() {
    // Validate lowercase letters
  var lowerCaseLetters = /[a-z]/g;
  if(myInput.value.match(lowerCaseLetters)) {
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
}

  // Validate capital letters
  var upperCaseLetters = /[A-Z]/g;
  if(myInput.value.match(upperCaseLetters)) {
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  // Validate numbers
  var numbers = /[0-9]/g;
  if(myInput.value.match(numbers)) {
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }

  // Validate length
  if(myInput.value.length >= 12) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }
});