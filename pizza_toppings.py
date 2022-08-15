layers = "Enter the name of your favaurite topping."
layers += "\nWe will put toppings from base to the top level according to your order of input."
layers += "\nEnter 'quit' if you are done.\nEnter topping: "
while True:
    topping = input(layers)
    if topping == 'quit':
        print("Thanks for your order")
        break