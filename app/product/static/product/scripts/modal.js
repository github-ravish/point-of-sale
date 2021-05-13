function showModal() {
	modal = document.getElementById("app__product-modal");
	modal.style.display = "block";
}

function closeModal() {
	modal = document.getElementById("app__product-modal");
	modal.style.display = "none";
}


function showProduct(product) {
	modal = document.getElementById("app__product-modal");
	console.log(product);
	modal_content = '<h1>Update Product</h1><br>';
	modal_content += 'Product Name:';
	modal_content += '<input id="product-name" style="margin-bottom: 10px;" type="text" class="form-control"' + 'value="' + product.productName + '"' + '>';
	modal_content += 'Quantity:';
	modal_content += '<input id="product-quantity" style="margin-bottom: 10px;" type="text" class="form-control"' + 'value="' + product.productQuantity + '"' + '>';
	modal_content += 'Cost Price:';
	modal_content += '<input id="product-cost-price" style="margin-bottom: 10px;" type="text" class="form-control"' + 'value="' + product.productCostPrice + '"' + '>';
	modal_content += 'Selling Price:';
	modal_content += '<input id="product-selling-price" style="margin-bottom: 10px;" type="text" class="form-control"' + 'value="' + product.productSellingPrice + '"' + '>';
	modal_content += '<button onclick="updateProduct()" style="margin-top: 10px;" type="button" class="btn btn-outline-primary ml-auto">';
	modal_content += 'Update';
	modal_content += '</button>';
	$('.app__product-modal-body').html(modal_content);
	showModal();
}

function updateProduct() {
	productName = $(".app__product-modal-body > #product-name").val();
	productQuantity = $(".app__product-modal-body > #product-quantity").val();
	productCostPrice = $(".app__product-modal-body > #product-cost-price").val();
	productSellingPrice = $(".app__product-modal-body > #product-selling-price").val();
	product = new Product(productName, productQuantity, productCostPrice, productSellingPrice);
	updateProductList(product);
}

// onclick="updateProduct(' + 'index' + ')"