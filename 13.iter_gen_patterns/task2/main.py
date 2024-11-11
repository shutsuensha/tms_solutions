# 1. Pizza class
class Pizza:
    def __init__(self, size=None, cheese=False, pepperoni=False, mushrooms=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        ingredients = []
        if self.cheese:
            ingredients.append("Cheese")
        if self.pepperoni:
            ingredients.append("Pepperoni")
        if self.mushrooms:
            ingredients.append("Mushrooms")
        if self.onions:
            ingredients.append("Onions")
        if self.bacon:
            ingredients.append("Bacon")
        
        return f"Pizza(Size: {self.size}, Ingredients: {', '.join(ingredients)})"


# 2. PizzaBuilder class
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza


# 3. PizzaDirector class
class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_pizza(self, size, with_cheese, with_pepperoni, with_mushrooms, with_onions, with_bacon):
        self.builder.set_size(size)
        
        if with_cheese:
            self.builder.add_cheese()
        if with_pepperoni:
            self.builder.add_pepperoni()
        if with_mushrooms:
            self.builder.add_mushrooms()
        if with_onions:
            self.builder.add_onions()
        if with_bacon:
            self.builder.add_bacon()

        return self.builder.build()


# Usage Example:
if __name__ == "__main__":
    # Create a builder
    builder = PizzaBuilder()
    
    # Create a director
    director = PizzaDirector(builder)
    
    # Build a pizza with specific ingredients
    pizza = director.make_pizza(
        size="Large",
        with_cheese=True,
        with_pepperoni=True,
        with_mushrooms=False,
        with_onions=True,
        with_bacon=True
    )
    
    # Print the pizza
    print(pizza)
