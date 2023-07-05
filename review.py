class Order:

    def __init__(self, customer, products, total_price, status):
        self.customer = customer
        self.products = products
        self.total_price = total_price
        self.status = status

    def __repr__(self):
        print(f"Order({self.customer}, {self.products}, {self.total_price}, {self.status})")