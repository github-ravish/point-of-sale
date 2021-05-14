$('.app__order-list-row').click(function () {
	id = $(this).data('trigger');
	orderProduct = $('#' + id)
	if (orderProduct.css('display') == 'none') {
		$('.app_order-list-product-row').css('display', 'none');
		orderProduct.css('display', 'table-row');
	}
	else {
		orderProduct.css('display', 'none');
	}
});