function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


window.addEventListener('load', () => {

	// Variables

	// vars for canvas
	const canvas = document.querySelector('#canvas');
	const ctx = canvas.getContext('2d');
	
	// button for function getData
	const button = document.querySelector('#predict');
	
	// canvas.style.marginLeft = '60px';
	// canvas.style.marginRight = '60px';

	// to pass the validation test number of pixels must be divisible by 784 and canvas must be square
	canvas.height = 784;
	canvas.width = canvas.height;

	let painting = false;

	// Functions

	// start drawing
	function startPosition(e){
		painting = true;
		draw(e);
	};

	// end drawing
	function finishPosition(){
		painting = false;
		ctx.beginPath();
	};

	// draw little stroke
	function draw(e){
		if(!painting) return;
		ctx.lineWidth = 40;
		ctx.lineCap = 'round';

		ctx.lineTo(e.clientX, e.clientY);
		ctx.stroke();
		ctx.beginPath();
		ctx.moveTo(e.clientX, e.clientY)
	};

	// sends data to server and gets response data
	function getData() {
		let ImageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
		let imdata = ImageData.data;
		let data = [];
		
		// cut all color pixels
		for(let i = 3; i < imdata.length; i += 4) {
			data.push(imdata[i])
		}

		
		// send data to server
		const csrftoken = getCookie('csrftoken');
		data = JSON.stringify(data)

		let xhr = new XMLHttpRequest();

		xhr.open('POST', 'http://localhost:8000/canvas', true);

		xhr.responseType = 'json';
		xhr.setRequestHeader('X-CSRFToken', csrftoken);
		xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

		xhr.onreadystatechange = function(){
			if(xhr.readyState === 4 && xhr.status === 200){
				response = xhr.response;
				console.log(response['number']);
				console.log(response['probabilities']);
				result = document.querySelector(".result");
				result.innerHTML = response['number']
			};
		};

		xhr.send('data=' + data);

	};

	// Event listeners

	// finish drawing
	document.addEventListener('mouseup', finishPosition);
	// start drawing
	canvas.addEventListener('mousedown', startPosition);
	// draw when cursor moves
	canvas.addEventListener('mousemove', draw);
	// send data and get enother data
	button.addEventListener('click', getData);
});
