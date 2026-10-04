//Setting up variables

var question=1;
var userAnswer;


var questionList = ["Which planet is closest to the Sun?", "What is 40% of 60?",
  "How many continents are on Earth?","How do plants make food?","H2O is the formula for what?",
  "What is a group of birds called?", "What is the largest ocean in the World?"];

var correctAnswers = ["Mercury", "24", "7", 
  "Photosynthesis", "Water", "Flock","Pacific"];

//Event Handlers

onEvent("nextButton", "click", function( ) {
  setProperty("button1", "hidden", false);
  setProperty("button2", "hidden", false);
  setProperty("button3", "hidden", false);
  setProperty("button4", "hidden", false);
  question=question+1;
  getQuestion(question);
  setQuestion();
  
});

onEvent("button1", "click", function( ) {
  updateScreen("button1");
  setProperty("button2", "hidden", true);
  setProperty("button3", "hidden", true);
  setProperty("button4", "hidden", true);

});

onEvent("button2","click", function( ) {
  updateScreen("button2");
  setProperty("button1", "hidden", true);
  setProperty("button3", "hidden", true);
  setProperty("button4", "hidden", true);
});

onEvent("button3","click", function( ) {
  updateScreen("button3");
  setProperty("button1", "hidden", true);
  setProperty("button2", "hidden", true);
  setProperty("button4", "hidden", true);
});

onEvent("button4","click", function( ) {
  updateScreen("button4");
  setProperty("button1", "hidden", true);
  setProperty("button2", "hidden", true);
  setProperty("button3", "hidden", true);
});
onEvent("restartButton1", "click", function( ) {
  question = 1;
  setScreen("screen1");
  setProperty("button1", "hidden", false);
  setProperty("button2", "hidden", false);
  setProperty("button3", "hidden", false);
  setProperty("button4", "hidden", false);
  getQuestion(question);
  setQuestion();
});

onEvent("restartButton2", "click", function( ) {
  question = 1;
  setScreen("screen1");
  setProperty("button1", "hidden", false);
  setProperty("button2", "hidden", false);
  setProperty("button3", "hidden", false);
  setProperty("button4", "hidden", false);
  getQuestion(question);
  setQuestion();
});


//Checks if the user's answer is corrects and than updates the screen
//correctAnswers{list} - A list of all the correct answers
//buttonID{string} - The ID of the button the user clicks
//question{number} - Question number the user is on
//userAnser{string} - The answer chosen by the user
function updateScreen(buttonID) {
 userAnswer = getText(buttonID);
 for (var i = 0; i < correctAnswers.length; i++) {
    if (userAnswer == correctAnswers[i]) {
      if (question >= correctAnswers.length) {
        setScreen("screen3");
      } else {
        setText("resultBox", "You are Correct!");
      }
      return;
    }
  }
 setScreen("screen2");
}

// Gets a question from the list and displays it depending on what question the user is on
// questionlist{list} - A list of all of the questions
// number{number} - The current question number
function getQuestion(number) {
  if (number >= 1 && number <= questionList.length) {
  setText("questionInput", questionList[number - 1]);
  }
}

//Sets the text for all four answer buttons based on the question number
//question{number} - The current question the user is on
//resultBox{string} - Resets the result text to default
function setQuestion() {
    if(question == 1)
  {
    setText("resultBox","Result:");
    setText("button1", "Mercury");
    setText("button2", "Mars");
    setText("button3", "Earth");
    setText("button4", "Jupiter");
  }
  if(question==2)
  {
     setText("resultBox","Result:");
     setText("button1", "14");
     setText("button2", "24");
     setText("button3", "12");
     setText("button4", "16");
  }
  if(question==3)
  {
     setText("resultBox","Result:");
     setText("button1", "7");
     setText("button2", "5");
     setText("button3", "9");
     setText("button4", "3");
  }
  if(question==4)
  {
     setText("resultBox","Result:");
     setText("button1", "Evaporation");
     setText("button2", "Condensation");
     setText("button3", "Precipitation");
     setText("button4", "Photosynthesis");
  }
  if(question==5)
  {
     setText("resultBox","Result:");
     setText("button1", "Gold");
     setText("button2", "Water");
     setText("button3", "Hydrogen");
     setText("button4", "Oxygen");
  }
  if(question==6)
  {
     setText("resultBox","Result:");
     setText("button1", "Group");
     setText("button2", "Pack");
     setText("button3", "Flock");
     setText("button4", "Herd");
  }
  if(question==7)
  {
     setText("resultBox","Result:");
     setText("button1", "Atlantic");
     setText("button2", "Indian");
     setText("button3", "Artic");
     setText("button4", "Pacific");
  }
}

//All buttons and icons are from code.orgs library
