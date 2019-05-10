document.getElementById('login').addEventListener("click", function() {
	document.querySelector('.bg-modal').style.display = "flex";
});

document.querySelector('.close').addEventListener("click", function() {
	document.querySelector('.bg-modal').style.display = "none";
});

document.getElementById('reg').addEventListener("click", function() {
	document.querySelector('.bg-modal2').style.display = "flex";
});

document.querySelector('.zatvori').addEventListener("click", function() {
	document.querySelector('.bg-modal2').style.display = "none";
});
