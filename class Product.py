class Product:
    def __init__(self, name, unitprice, gst, quantity):
        self.name = name
        self.unitprice = unitprice
        self.gst = gst
        self.quantity = quantity

    def calculate_total_price(self):
        total_price = (self.unitprice * (1 + self.gst / 100)) * self.quantity

        if self.unitprice >= 500:
            total_price *= 0.95

        return total_price

leather_wallet = Product("Leather Wallet", 1100, 18, 1)
umbrella = Product("Umbrella", 900, 12, 4)
cigarette = Product("Cigarette", 200, 28, 3)
honey = Product("Honey", 100, 0, 2)

basket = [leather_wallet, umbrella, cigarette, honey]


max_gst_product = max(basket, key=lambda product: product.unitprice * product.gst / 100)
print("Product with maximum GST amount:", max_gst_product.name)


total_amount_to_pay = sum(product.calculate_total_price() for product in basket)

print("Total amount to be paid to the shopkeeper:", total_amount_to_pay)