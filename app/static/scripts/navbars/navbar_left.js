function navbarLeftHeightWidth() {
	var headerHeight = $('#navbar').outerHeight(true);
	headerHeight = headerHeight ? headerHeight : 0;
	var height = window.innerHeight - headerHeight + 'px';
	$("#app__navbar-left").css("min-height", height);
}

function navbarLeftToggle() {
	var navbarLeftWidth = $('#app__navbar-left').outerWidth(true);
	if (navbarLeftWidth > 0) {
		$("#app__navbar-left").css("width", "0px");
		$(".app__top-nav-trigger", 0).html("view_headline");
		setBodyWidth('close');
	}
	else {
		$("#app__navbar-left").css("width", "250px");
		$(".app__top-nav-trigger", 0).html("close");
		setBodyWidth('open');
	}
}

function setBodyWidth(navbarState) {
	if (window.innerWidth >= 800 && navbarState == 'open') {
		$(".content").css("margin-left", '250px');
	}
	else {
		$(".content").css("margin-left", '0px');
	}
}

function navbarLeftDropdownToggle(element) {
	var dropdownDisplay = $("." + element).css("display");
	if (dropdownDisplay == "block") {
		$("." + element).css("display", "none");
	}
	else {
		$("." + element).css("display", "block");
	}
	console.log(dropdownDisplay);
}

$('#container-fluid, #footer').click(function (e) {
	var width = $("#app__navbar-left").outerWidth(true);
	if (width > 0) {
		navbarLeftToggle();
	}
})

$(document).onload = navbarLeftHeightWidth();