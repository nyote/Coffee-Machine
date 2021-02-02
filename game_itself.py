from main import resources
from main import MENU
from main import coins

#def check_report():

def pay():
    p = int(input("How many pennies would you like to pay with? "))
    p1 = p*0.01
    n = int(input("How many nickels would you like to pay with? "))
    n1 = n*0.05
    d = int(input("How many dimes would you like to pay with? "))
    d1 = d*0.10
    q = int(input("How many quarters would you like to pay with? "))
    q1 = q*0.25
    totalpay = p1+n1+d1+q1
    return totalpay

report = {
    "water left": 0,
    "milk left": 0,
    "coffee left": 0,
    "profit": 0,
}

def order(word):  #ordering function
    milk = 0
    esp = MENU[word]
    water = esp["ingredients"]["water"]
    coffee = esp["ingredients"]["coffee"]
    cost = esp["cost"]
    if word == "espresso":
        esp["ingredients"]["coffee"] = 0
        milk = esp["ingredients"]["coffee"]
    return water, milk, coffee, cost

def play_game():
    finished = False
    total_profit = 0
    total_water = resources["water"]
    total_milk = resources["milk"]
    total_coffee = resources["coffee"]
    while not finished:
        pick_coffee = input("What would you like? (espresso/latte/cappuccino): ")
        if pick_coffee == 'off':
            print("The machine is turning off")
            return
        elif pick_coffee == 'report':
            print(report)
        if pick_coffee == "espresso" or pick_coffee == "latte" or pick_coffee == "cappuccino":
            order_ingredients = order(pick_coffee)
            print(order_ingredients)
            water = order_ingredients[0] #calling water from new_function
            cost = order_ingredients[3]
            coffee = order_ingredients[2]
            print(coffee)
            milk = order_ingredients[1]
            print(f"{water} , this costs: ${cost}")

            if water > total_water:
                print("Sorry, there isn't enough water for the drink")
                return
            elif milk > total_milk:
                print("Sorry, there isn't enough milk for the drink")
                return
            elif coffee > total_coffee:
                print("Sorry, there isn't enough coffee for the drink")
                return

            profit = pay()
            print(profit)

            if profit < cost:
                print("The payment is not enough. Money refunded")
                profit = 0
                play_game()
            elif profit == cost:
                total_water = total_water - water
                report["water left"] = total_water
                total_milk = total_milk - milk
                report["milk left"] = total_milk
                total_coffee = total_coffee - coffee
                report["coffee left"] = total_coffee
                report["profit"] += profit
                print(f"Here is your {pick_coffee}, enjoy! :) ")
                play_game()
            elif profit > cost:
                refund = profit - cost
                total_water = total_water - water
                report["water left"] = total_water
                total_milk = total_milk - milk
                report["milk left"] = total_milk
                total_coffee = total_coffee - coffee
                report["coffee left"] = total_coffee
                print(f"${profit} is more than ${cost}. You get ${refund} back.")
                report["profit"] += cost
                print(f"Here is your {pick_coffee}, enjoy! :) ")
                play_game()



play_game()