if (quaggaInitialize == true) {
	Quagga.start();
}

var products = [
	new Product('890400440006', 'Nestea Icetea', '180.00', '10'),
	new Product('890400440377', 'Nestle Maggie', '18.00', '5'),
	new Product('923541256358', 'Britania Rusk', '70.00', '6'),
]


function updateCart() {
	if (products.length <= 0) {
		$('.cart').html("");
		return;
	}

	var table = '<table class="table">'
	table += '<thead class="thead-dark">'
	table += '<tr>'
	table += '<th scope="col">#</th>'
	table += '<th scope="col">Name</th>'
	table += '<th scope="col">Price</th>'
	table += '<th scope="col">Quantity</th>'
	table += '<th scope="col"></th>'
	table += '</tr>'
	table += '</thead>'
	table += '<tbody>'
	for (i = 0; i < products.length; i++) {
		table += '<tr>'
		table += '<th scope="row">' + (i + 1).toString() + '</th>'
		table += '<td>' + products[i].productName + '</td>'
		table += '<td>' + products[i].productSellingPrice + '</td>'
		table += '<td>' + products[i].productQuantity + '</td>'
		table += '<td class="action-button-col">'

		table += '<a onclick=' + 'removeProductFromCart(' + i + ')>'
		table += '<span style="margin-right: 10px;" class="product-cart-action-button material-icons material-icons-outlined">delete_outline</span>'
		table += '</a>'
		table += '<a onclick=' + 'editProduct(' + i + ')>'
		table += '<span class="product-cart-action-button material-icons material-icons-outlined">edit</span>'
		table += '</a>'

		table += '</td>'
		table += '</tr>'
	}
	table += '<tr><td colspan="5" class="text-right"><button class="btn btn-primary" onclick="addOrderBackend()">Create Order</button></td></tr>'
	table += '<tbody>'
	table += '</table>'

	$('.cart').html(table);
}

function addOrderBackend() {
	orderAddUrl = $('.cart-card').data('url');
	data = []
	for (i = 0; i < products.length; i++) {
		data.push({
			"product": products[i].productSlug,
			"quantity": products[i].productQuantity
		})
	}
	finalData = {
		"items": data
	}
	$.ajax({
		url: orderAddUrl,
		type: "POST",
		headers: { 'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val() },
		data: JSON.stringify(finalData),
		dataType: "json",
		contentType: "application/json; charset=utf-8",
		success: function (data) {
			console.log(data);
		},
		error: function (xhr, errmsg, err) {
			console.log(xhr, errmsg, err)
		},
		beforeSend: function (xhr) {
			console.log(this.data)
		}
	});
}


$(document).onload = updateCart();