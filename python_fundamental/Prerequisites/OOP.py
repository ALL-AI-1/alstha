class Ecommerce:
    Brand_name = "Alstha"

    def __init__(self):
        print("Welcome")

    def seller(self, seller_name, price):
        self.seller_name = seller_name
        self.price = price
        print(f"Seller set: {self.seller_name}, Price updated to: {self.price}")

    def buyer(self, buyer_name, product_name, quantity):
        self.buyer_name = buyer_name
        self.product_name = product_name
        
        self.quantity = quantity
        print(f"Buyer set: {self.buyer_name}, Product: {self.product_name}, Price: {self.price}, Quantity: {self.quantity}")

    @property
    def total_price(self):
        return self.price * self.quantity

    @classmethod
    def change_brand_name(cls, new_name="Alstha2.0"):
        cls.Brand_name = new_name
        print(f"Brand name changed to: {cls.Brand_name}")

    def __payment(self, payment_method, account_number,amount):
        self.payment_method = payment_method
        self.account_number = account_number
        self.amount = amount
        
    def details(self):
        if self.total_price==self.amount:
            print(f"Payment successful i.e. {self.amount} ")
        else:
            print("Payment failed")
# Example usage:
c1 = Ecommerce()
print(f"Brand: {c1.Brand_name}")
c1.seller("Alice", 48000)
c1.buyer("Bob", "Laptop", 2)
print("Total price:", {c1.total_price})
c1.details()
Ecommerce.change_brand_name("Alstha3.0")
print(f"Updated Brand: {c1.Brand_name}")