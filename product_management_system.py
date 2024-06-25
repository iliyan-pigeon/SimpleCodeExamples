class BaseDrink:
    def __init__(self, product: str, price: float, amount=1, comment=None):
        self.product_name = product
        self.price = price
        self.amount = amount
        self.comment = comment

    def total_price(self):
        result = self.price * self.amount

        return result


class Water250ml(BaseDrink):
    pass


class Coffee(BaseDrink):
    pass


class Lemonade(BaseDrink):
    pass


class BaseFood:
    def __init__(self, product, price, amount=1, comment=None):
        self.product_name = product
        self.price = price
        self.amount = amount
        self.comment = comment

    def total_price(self):
        result = self.price * self.amount

        return result


class Pasta(BaseFood):
    pass


class Burger(BaseFood):
    pass


class Pizza(BaseFood):
    pass


class OpenBill:
    def __init__(self, *products):
        self.products = products

    def total_price(self):
        result = 0

        for product in self.products:
            result += product.total_price()

        return result

    def list_the_products(self):
        result_list = []

        for product in self.products:
            result_list.append(f"Product: {product.product_name}, Amount: {product.amount}, "
                               f"Price: {product.total_price()} lv.")

        result = "\n".join(result_list)

        return result


water = Water250ml("Devin", 2.00, 2)
coffee = Coffee("Dabov", 3.00, 4)
lemonade = Lemonade("Lemonade", 5.00, 1)
pasta = Pasta("Carbonara", 15.00, 2)
pizza = Pizza("Margherita", 12.00, 1)
burger = Burger("Burger", 17.00, 3)

bill = OpenBill(water, coffee, lemonade, pasta, pizza, burger)

print(bill.list_the_products())
print("Total:")
print(bill.total_price())
