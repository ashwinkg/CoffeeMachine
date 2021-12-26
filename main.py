from Menu import MENU
from Resource import resources

vending_money = 0
VALUE_OF_QUARTERS = 0.25
VALUE_OF_DIMES = 0.10
VALUE_OF_NICKEL = 0.05
VALUE_OF_PENNIES = 0.01


def get_coffee_profile(input_coffee):
    """Returns the coffee profile of the input parameter"""
    return MENU[input_coffee]


def check_price_match(actual_cost, num_of_quarters, num_of_dimes, num_of_nickle, num_of_pennies):
    total_quarters = num_of_quarters * VALUE_OF_QUARTERS
    total_dimes = num_of_dimes * VALUE_OF_DIMES
    total_nickel = num_of_nickle * VALUE_OF_NICKEL
    total_pennies = num_of_pennies * VALUE_OF_PENNIES
    input_sum = (total_quarters + total_dimes + total_nickel + total_pennies)
    if actual_cost > input_sum:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(float(input_sum - actual_cost), 2)
        global vending_money
        vending_money += actual_cost
        print(f"Here is ${change} in change")
        return True


def calculate_resource(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def update_resource(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]


def dispense_coffee():
    print("Please insert coins.")
    user_quarters = int(input("how many quarters?: "))
    user_dimes = int(input("how many dimes?: "))
    user_nickle = int(input("how many nickles?: "))
    user_pennies = int(input("how many pennies?: "))
    coffee_profile = get_coffee_profile(user_input)
    enough_resource = calculate_resource(coffee_profile["ingredients"])
    if enough_resource:
        transaction_complete = check_price_match(coffee_profile["cost"], user_quarters, user_dimes, user_nickle,
                                                 user_pennies)
        if transaction_complete:
            print(f"Here is your {user_input}. Enjoy! ☕")
            update_resource(coffee_profile["ingredients"])


def display_resources(profit):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


vending_machine_on = True
while vending_machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input == 'off':
        vending_machine_on = False
    elif user_input == "report":
        display_resources(vending_money)
    else:
        dispense_coffee()

# TODO: 1 Prompt user by asking "What would you like?"
# TODO: 2 Turn off the Coffee Machine by entering “off” to the prompt
# TODO: 3 Print report.
# TODO: 4 Check resources sufficient?
# TODO: 5 Process coins.
# TODO: 6 Check transaction successful?
# TODO: 7 Make Coffee
