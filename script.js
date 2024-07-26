var checkerBtn = document.querySelector("#button-1")
var guess = document.querySelector("#text")
var message = document.querySelector("#note-1")
var Counter= document.querySelector("#add")
var chanecesSpan = document.querySelector("#chaneces")


var RandomNumber = Math.ceil(Math.random() * 100)
console.log(RandomNumber);
let attempts = 10

checkerBtn.addEventListener("click", function(e) {
    e.preventDefault();

    validationForm();
});

function validationForm(){
    var userGuess = parseInt(guess.value);
    // console.log(userGuess);
    if (userGuess ===""){
        message.textContent = "عددی وارد نشده است" ;
    }
    else if(userGuess === RandomNumber){
        // attempts--;
        message.textContent = " تبریک شما عدد مورد نظر را درست حدس زدید ";
        chanecesSpan -= 1;
    }
    else if(userGuess > RandomNumber){
        // attempts--;
        message.textContent = "عدد شما بزرگتر از عدد مورد تظر است";
        chanecesSpan -= 1;
    }
    else if(userGuess < RandomNumber){
        // attempts--;
        message.textContent= "  عدد شما کوچکتر از عدد مورد نظر است";
        chanecesSpan -= 1;
    }

}
function disableInput(){
    guess.disabled= true;
    checkerBtn.disabled= true;
}
