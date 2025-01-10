class AbstractProductA:
    def method(self):
        pass

class ConcreteProductA1(AbstractProductA):
    def method(self):
        return "Product A1"

class ConcreteProductA2(AbstractProductA):
    def method(self):
        return "Product A2"

class AbstractFactory:
    def create_product_a(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()
