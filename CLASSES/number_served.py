class NumberServed:
    def __init__(self):
        self.number_served = 0
    
    def set_number_served(self, update):
        self.number_served = update
        return self.number_served
    
    def increment_number_served(self, incre):
        self.number_served += incre
        return self.number_served


restaurant = NumberServed()
print(f"The restaurant has served {restaurant.number_served}.")

restaurant.set_number_served(34)
print(f"The restaurant has served {restaurant.number_served}.")

restaurant.increment_number_served(4)
print(f"The restaurant has served {restaurant.number_served}.")