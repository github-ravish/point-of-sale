productSlug = null;
productUrl = null;

function initalizeProduct(productRow) {
	productName = $(productRow).children('.product-name').html();
	productQuantity = $(productRow).children('.product-quantity').html();
	productCostPrice = $(productRow).children('.product-cost-price').html();
	productSellingPrice = $(productRow).children('.product-selling-price').html();
	var product = new Product(productName, productQuantity, productCostPrice, productSellingPrice);
	productSlug = $(productRow).attr('id');
	productUrl = $(productRow).data('url');
	return product;
}

function updateProductList(product) {
	$('#' + productSlug).children('.product-name').html(product.productName);
	$('#' + productSlug).children('.product-quantity').html(product.productQuantity);
	$('#' + productSlug).children('.product-cost-price').html(product.productCostPrice);
	$('#' + productSlug).children('.product-selling-price').html(product.productSellingPrice);
	updateProductBacked(product);
	closeModal();
}


function updateProductBacked(product) {
	$.ajax({
		url: productUrl,
		type: "PUT",
		headers: { 'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val() },
		data: {
			slug: productSlug,
			name: product.productName,
			quantity: product.productQuantity,
			cost_price: product.productCostPrice,
			selling_price: product.productSellingPrice,
		},
		success: function (data) {
			console.log(data);
		},
		error: function (xhr, errmsg, err) {
			console.log(err)
		}
	});
}


$('.app__product-list-row').click(function () {
	var product = initalizeProduct(this);
	showProduct(product);
	// updateProductList(this, product);
});