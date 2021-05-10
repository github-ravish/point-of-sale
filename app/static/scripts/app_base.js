function bodyHeight() {
	var headerHeight = $('#navbar').outerHeight(true);
	headerHeight = headerHeight ? headerHeight : 0;
	var footerHeight = $('#footer').outerHeight(true);
	footerHeight = footerHeight ? footerHeight : 0;
	height = (window.innerHeight - (headerHeight + footerHeight)) + 'px';
	$("#container-fluid").css("min-height", height);
	$("#container-fluid").css("margin-top", headerHeight + 'px');
}

function passwordTypeToggle(event) {
	var inpType = $('#toggle-password-type')[0].type;
	if (inpType == 'password') {
		$('#toggle-password-type')[0].type = 'text';
		$('.password-toggle').html('visibility')
	} else {
		$('#toggle-password-type')[0].type = 'password';
		$('.password-toggle').html('visibility_off')
	}
}

$(document).onload = bodyHeight();