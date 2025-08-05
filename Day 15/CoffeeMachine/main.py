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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

should_contuie = True
money = 0.0

def turn_off(text):
    return False

def process_coins(p_money):
    quarter=float(input("quarters:")) * 0.25
    dime = float(input("dime:")) * 0.10
    nickles =float(input("nickels")) * 0.05
    pennies = float(input("pennies:")) * 0.01
    p_money = quarter + dime +nickles+pennies
    return p_money

def report():
    print(
        f"water :{resources['water']}ml \nMilk :{resources['milk']}ml \nCoffee :{resources['coffee']}g  \nmoney:${money}")

def change(n1,n2):
    print(f"Here is ${n1-n2}dollars in change.")
    return n1-n2



def deducted(coffee_name1,existing_resources,outgoing_resources):
    if coffee == 'espresso':
        var = existing_resources['water'] - outgoing_resources[coffee_name1]['ingredients']['water']
        # var1 = existing_resources['milk'] - outgoing_resources[coffee_name1]['ingredients']['milk']
        var2 =  existing_resources['coffee'] - outgoing_resources[coffee_name1]['ingredients']['coffee']
        return var,var2
    else:
        var = existing_resources['water'] - outgoing_resources[coffee_name1]['ingredients']['water']
        var1 = existing_resources['milk'] - outgoing_resources[coffee_name1]['ingredients']['milk']
        var2 = existing_resources['coffee'] - outgoing_resources[coffee_name1]['ingredients']['coffee']
        return var,var1,var2






def resources_check(coffe_name,menu_options,resources_left):
    if coffe_name == 'espresso':
        if resources_left['water']+1 > menu_options['espresso']["ingredients"]["water"]:
            if resources_left['coffee'] +1 > menu_options['espresso']["ingredients"]["coffee"]:
                print(f"Here is your {coffe_name}. Enjoy!!")
                return True
            else:
                print("Sorry there is not enough coffe")
                return False
        else:print("Sorry there is not enough water")
        return False
    elif coffe_name == 'latte' or coffe_name =='cappuccino':
        if resources_left['water']+1 > menu_options[coffe_name]["ingredients"]["water"]:
            if resources_left['coffee'] +1> menu_options[coffe_name]["ingredients"]["coffee"]:
                if resources_left['milk']+1 > menu_options[coffe_name]["ingredients"]["milk"]:
                    print(f"Here is your {coffe_name}. Enjoy!!")
                    return True
                else:
                    print("Sorry there is not enough milk")
                    return False
            else:
                print("Sorry there is not enough coffe")
                return False
        else:
            print("Sorry there is not enough water")
            return False


# TOdo prompt to ask user for what coffe he wants

##running the loop till machine is set to off
while should_contuie :
    coffee = input("What would you like? (espresso/latte/cappuccino):").lower()
    if coffee == 'off':
        should_contuie = False
    elif coffee == 'report':
        report()
    elif coffee == "espresso":
        trans_money = process_coins(money)
        if trans_money > (MENU['espresso']['cost']) >=1.0:
            if resources_check(coffee,MENU, resources):
                resources['water'],resources['coffee'] =(deducted(coffee,resources,MENU))
                money +=trans_money- change(trans_money,(MENU['espresso']['cost']))
        elif trans_money > MENU['espresso']['cost']:
            if resources_check(coffee, MENU, resources):
                resources['water'], resources['coffee'] = (deducted(coffee, resources, MENU))
                money += trans_money
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif coffee =='latte' or coffee =='cappuccino' :
        trans_money1 = (process_coins(money))
        if trans_money1 > (MENU[coffee]['cost']) >=1.0:
            if resources_check(coffee,MENU, resources):
                resources['water'], resources['milk'] ,resources['coffee'] = (deducted(coffee, resources, MENU))
                money +=trans_money1- change(trans_money1,(MENU[coffee]['cost']))
        elif trans_money1 > MENU[coffee]['cost']:
            if resources_check(coffee,MENU, resources):
                resources['water'], resources['milk'], resources['coffee'] = (deducted(coffee, resources, MENU))
                money+=trans_money1
        else:
            print("Sorry that's not enough money. Money refunded.")

