document.getElementById('novi-izl').addEventListener("click", function() {

	document.querySelector('.overlay').style.display = "flex";
	document.querySelector('.bg-modal').style.display = "flex";
	document.querySelector('#CarouselTest').style.display = "none";


});

document.querySelector('.zatvori').addEventListener("click", function() {
	document.querySelector('.overlay').style.display = "none";
	document.querySelector('.bg-modal').style.display = "none";
	document.querySelector('#CarouselTest').style.display = "flex";

});


document.getElementById('recenz').addEventListener("click", function() {

	

	document.querySelector('.overlay').style.display = "flex";
	document.querySelector('.bg-modal2').style.display = "flex";
	document.querySelector('#CarouselTest').style.display = "none";


});

document.querySelector('.zatvori2').addEventListener("click", function() {
	
	
	document.querySelector('.overlay').style.display = "none";
	document.querySelector('.bg-modal2').style.display = "none";
	document.querySelector('#CarouselTest').style.display = "flex";

});
