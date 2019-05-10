document.getElementById('novi-izl').addEventListener("click", function() {

	document.querySelector('.overlay').style.display = "flex";
	document.querySelector('.bg-modal').style.display = "flex";
	document.querySelector('#slides').style.display = "none";


});

document.querySelector('.zatvori').addEventListener("click", function() {
	document.querySelector('.overlay').style.display = "none";
	document.querySelector('.bg-modal').style.display = "none";
	document.querySelector('#slides').style.display = "flex";

});

