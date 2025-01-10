class Pizza:
    def __init__(self):
        self.toppings = []
        self.size = None

    def add_topping(self, topping):
        self.toppings.append(topping)

    def set_size(self, size):
        self.size = size

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_cheese(self):
        self.pizza.add_topping("cheese")
        return self

    def add_pepperoni(self):
        self.pizza.add_topping("pepperoni")
        return self

    def set_size(self, size):
        self.pizza.set_size(size)
        return self

    def build(self):
        return self.pizza
