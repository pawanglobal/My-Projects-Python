finished_sandwitches = {}
sandwitch_order_active = True

while sandwitch_order_active:
    name = input("\nWhat is your name?\n")
    response = input("\nWhich sandwitch would you like to eat?\n")
    
    finished_sandwitches[name.title()] = response.title()
    ask = input('\nWould you like to order any other sandwitch? (yes/no)\n')
    if  ask == 'no':
        print(f'\nThank You for your order. {name.title()} your {response.title()} sandwitch is ready!')
        sandwitch_order_active = False

print("\nToday's orders:")
for name, response in finished_sandwitches.items():
    print(finished_sandwitches)