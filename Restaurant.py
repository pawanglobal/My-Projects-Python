"""A car that can be used to represent a car"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"My restaurant's name is {self.restaurant_name}, and it has a {self.cuisine_type} food to serve.")
    
    def restaurant_open(self):
        print(f"My {self.restaurant_name} restaurant opens everyday for 24*7.")
    
    def customers(self):
        print(f"The customers have been served: {self.number_served}.")
        
    def set_the_number_served(self, new_value):
        if new_value > self.number_served:
            self.number_served = new_value
        else:
            print("Discount...")
    
    def increment_number_served(self,customers):
        self.number_served += customers

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
    
        self.flavours = 'vanilla, chocolaty, extra_creamy'
    
    def list_of_flavours(self):
        print(f"This Ice Cream Stand has {self.flavours} Ice Cream Flavours.")
        
        
        
        
   
restaurant_is = Restaurant('Radigaston', 'Traditional')
restaurant_is.describe_restaurant()
restaurant_is.restaurant_open()

restaurant = Restaurant('IMPERIAL HOTEL', 'FAST FOOD')
restaurant.describe_restaurant()
restaurant.customers()

restaurant.set_the_number_served(25)
restaurant.customers()

restaurant.increment_number_served(10)
restaurant.customers()

my_stand = IceCreamStand('Dream Ice Cream', 'Every Ice Cream')
my_stand.describe_restaurant()
my_stand.list_of_flavours()