class Pizza(object):
    def __init__(self):
        self.toppings = []

    def __call__(self, topping):
        self.toppings.append(topping())

    def __repr__(self):
        return str(self.toppings)


pizza = Pizza()


@pizza
def cheese():
    return "chee2se"


@pizza
def tomato():
    return "tomato"


print(pizza)
