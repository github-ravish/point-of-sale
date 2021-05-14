innerWidth = $('.content').css('width').slice(0, -2) - 20;

function editProduct(index) {
	modal = document.getElementById("cart-add-product-modal");
	modal.style.display = "block";
	product = products[index]
	modal_content = 'Product Name:';
	modal_content += '<input style="margin-bottom: 10px;" type="text" class="form-control"' + 'value="' + product.productName + '"' + 'disabled>';
	modal_content += 'Quantity:';
	modal_content += '<input id="product-quantity" style="margin-bottom: 10px;" type="text" class="form-control"' + 'value="' + product.productQuantity + '"' + '>';
	modal_content += 'Price:';
	modal_content += '<input id="product-price" style="margin-bottom: 10px;" type="text" class="form-control"' + 'value="' + product.productSellingPrice + '"' + '>';
	modal_content += '<button onclick="updateProduct(' + index + ')" style="margin-top: 10px; float: right;" type="button" class="btn btn-outline-primary">';
	modal_content += 'Update';
	modal_content += '</button>';
	$('.cart-add-modal-content').html(modal_content);
	showModal();
}

function addProductInCart(product) {
	for (i = 0; i < products.length; i++) {
		if (products[i].productSlug == product.productSlug) return;
	}
	products.push(product);
	editProduct(products.length - 1);
	updateCart();
}

function removeProductFromCart(index) {
	products.pop(index);
	updateCart();
}

function updateProduct(index) {
	products[index].productQuantity = $('#product-quantity').val();
	products[index].productPrice = $('#product-price').val() * products[index].productQuantity;
	updateCart();
	closeModal();
}

function intializeObject(data) {
	product = new Product(data.slug, data.name, data.selling_price, data.quantitiy);
	return product;
}