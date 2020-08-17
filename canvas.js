window.addEventListener('resize', () => {
	canvas.height = Math.floor(window.innerHeight / 28) * 28;
	canvas.width = canvas.height;
})


window.addEventListener('load', () => {

	// Variables

	const canvas = document.querySelector('#canvas');
	const ctx = canvas.getContext('2d');
	const button = document.querySelector('#predict');
	
	// canvas.style.marginLeft = '60px';
	// canvas.style.marginRight = '60px';
	canvas.height = Math.floor(window.innerHeight / 28) * 28;
	canvas.width = canvas.height;

	let painting = false;

	// Functions

	function startPosition(e){
		painting = true;
		draw(e);
	};

	function finishPosition(){
		painting = false;
		ctx.beginPath();
	};

	function draw(e){
		if(!painting) return;
		ctx.lineWidth = 20;
		ctx.lineCap = 'round';

		ctx.lineTo(e.clientX, e.clientY);
		ctx.stroke();
		ctx.beginPath();
		ctx.moveTo(e.clientX, e.clientY)
	};

	function getData() {
		let ImageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
		let imdata = ImageData.data;
		let data = [];
		
		// cut all color pixels
		for(let i = 3; i < imdata.length; i += 4) {
			data.push(imdata[i])
		}

		console.log(data)
		console.log(data.length)	
		
		// send data to server
		data = JSON.stringify(data);

	};

	// Event listeners

	canvas.addEventListener('mousedown', startPosition);
	document.addEventListener('mouseup', finishPosition);
	canvas.addEventListener('mousemove', draw);
	button.addEventListener('click', getData);
});
