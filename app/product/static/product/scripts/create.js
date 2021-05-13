
innerWidth = $('.content').css('width').slice(0, -2) - 40;

function startScanner() {
	showModal();
	Quagga.onDetected(function (result) {
		code = result.codeResult.code;
		if (code.length == 13) {
			$('input[name="slug"]').val(code);
			closeModal();
		}
	});
}

function showModal() {
	Quagga.start();
	modal = document.getElementById("app__product-modal");
	modal.style.display = "block";
}

function closeModal() {
	modal = document.getElementById("app__product-modal");
	modal.style.display = "none";
	Quagga.stop();
}