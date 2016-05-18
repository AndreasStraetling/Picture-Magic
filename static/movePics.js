function moveMyPictures() {
	var terminate = 0;
	var images = document.getElementsByTagName("img");
	var move = setInterval(step,5);
	//var end = document.getEl("container").style.width;
	//console.log(end);
	
	function step(){
		if (terminate == 91) {
			clearInterval(move);
		}
		else {
			terminate ++;
			/* for-of zu neu fuer manche Browser?!
			for (var img of images){
				img.style.margin = '3px 0px 3px ' + terminate + '%';
			}
			*/
			for (var i = 0; i < images.length; i++){
				images[i].style.margin = '3px 0px 3px ' + terminate + '%';
			}
		}
	}
}