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

 $(document).ready(function(){
      $("#datatables").DataTable();
    });


    
 function add(ths,sno){


for (var i=1;i<=5;i++){
var cur=document.getElementById("star"+i)
cur.className="fa fa-star"
}

for (var i=1;i<=sno;i++){
var cur=document.getElementById("star"+i)
if(cur.className=="fa fa-star")
{
cur.className="fa fa-star checked"
}
}

}


    
