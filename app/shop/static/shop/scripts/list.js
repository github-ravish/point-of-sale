$(".app__shop-list-row").click(function () {
	console.log("here");
	window.document.location = $(this).data("url");
});