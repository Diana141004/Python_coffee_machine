MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}



def give_report (ingredients):
    print(f"Water : {ingredients['water']}ml\nMilk : {ingredients['milk']}ml\nCoffe : {ingredients['coffee']}g\nMoney : {ingredients['money']}")

def check_resources (ingredients, drink_name):
    if MENU[drink_name]['ingredients']['water'] <= ingredients['water']:
        if MENU[drink_name]['ingredients']['milk'] <= ingredients['milk']:
            if MENU[drink_name]['ingredients']['coffee'] <= ingredients['coffee']:
                return True
            else:
                print("Sorry, we are out of coffee! :(((")
        else:
            print("Sorry, we are out of milk! :(((")
    print("Sorry, we are out of water! :(((")
    return False

def money_handler(drink_name):
    print("Please insert coins:")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    total = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    if total < MENU[drink_name]['cost']:
        print("Not enough money. Money refunded.")
        return False
    elif total > MENU[drink_name]['cost']:
        change = total - MENU[drink_name]['cost']
        print(f"Here is ${change} in change.")
    return True

def make_coffee (drink_name, ingredients):
    ingredients['water'] -=  MENU[drink_name]['ingredients']['water']
    ingredients['milk'] -= MENU[drink_name]['ingredients']['milk']
    ingredients['coffee'] -= MENU[drink_name]['ingredients']['coffee']
    ingredients['money'] += MENU[drink_name]['cost']

    print(f"Here is your {drink_name}☕, enjoy!")




########### MAIN CODE ##################

power = "on"
while power == "on":
    prompt = input("What would you like? (espresso/latte/cappuccino):")

    if prompt == "off":
        power = "off"

    elif prompt == "report":
        give_report(resources)

    else:
        if check_resources(resources,prompt):
            if money_handler(prompt):
                make_coffee(prompt,resources)


