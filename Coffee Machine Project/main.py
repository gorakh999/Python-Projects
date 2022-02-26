import replit
import art

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0
resources = {
    "water": 500,
    "milk": 200,
    "coffee": 50,
}



def is_transaction_successfull(payment, drink_cost):
    """Returns True if Payment is accepted, or False if money is insufficient"""
    if (payment > drink_cost):
        change = round(total_coin - order['cost'], 2)
        global profit
        profit += drink_cost
        print(f"Here is Your Change ${change}")
        return True

    else:
        print("Sorry, Money is Insufficient. Money refunded")
        return False


def process_coin():
    print("Please Insert Coins")
    total = int(input("How many Quarters ? : ")) * 0.25
    total += int(input("How many Dimes ? : ")) * 0.1
    total += int(input("How many Nickles ? : ")) * 0.05
    total += int(input("How many Penny ? : ")) * 0.01
    return total


def is_resource_sufficient(order_ingradient):
    for item in order_ingradient:
        if (order_ingradient[item] > resources[item]):
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_drink(order, ingredients):
    """Deduct the required Ingredient from the resource"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"here is your {order}")

if __name__ == '__main__':
    running = True
    replit.clear()
    print(art.logo)
    while running:
        choice = input("​What would you like? (espresso/latte/cappuccino): ")
        
        if (choice == 'off'):
            running = False
        elif (choice == 'report'):
            print(f"Water : {resources['water']}ml")
            print(f"Milk : {resources['milk']}ml")
            print(f"Coffee : {resources['coffee']}ml")
            print(f"Money : ${profit}")
        else:
            order = MENU[choice]
            if (is_resource_sufficient(order['ingredients'])):
                total_coin = process_coin()
                if (is_transaction_successfull(total_coin, order["cost"])):
                    make_drink(choice, order["ingredients"])            
