class Product {
	productSlug;
	productName;
	productSellingPrice;
	productQuantity;

	constructor(productSlug, productName, productSellingPrice, productQuantity) {
		this.productSlug = productSlug;
		this.productName = productName;
		this.productQuantity = productQuantity;
		this.productSellingPrice = productSellingPrice;
	}
}