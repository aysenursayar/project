import datetime
import csv

# to create a superclass for pizzas
class Pizza():
    # to assign new objects in pizza class
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # to get description of the corresponding pizza
    def get_description(self):
        return f"{self.name} has a price of {self.price}"

    # to get cost of the corresponding pizza
    def get_cost(self):
        return self.price


# creating subclasses of all pizzas and instances of the subclasses
class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza", 50)


class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita Pizza", 56)


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Turk Pizza", 60)


class DominosPizza(Pizza):
    def __init__(self):
        super().__init__("Dominos Pizza", 68)


# creating a superclass for all sauces
class Decorator():
    # to assing new objects in decorator class
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # to get description of the corresponding sauce
    def get_description(self):
        return f"{self.name} has a price of {self.price}"

    # to get cost of the corresponding pizza
    def get_cost(self):
        return self.price


# creating subclasses of all sauces and instances of the subclasses
class Olives(Decorator):
    def __init__(self):
        super().__init__("Olives", 2)


class Mushrooms(Decorator):
    def __init__(self):
        super().__init__("Mushrooms", 3)


class GoatCheese(Decorator):
    def __init__(self):
        super().__init__("Goat Cheese", 5)


class Meat(Decorator):
    def __init__(self):
        super().__init__("Meat", 6)


class Onions(Decorator):
    def __init__(self):
        super().__init__("Onions", 2)


class Corn(Decorator):
    def __init__(self):
        super().__init__("Corn", 3)


# main function to get information about the order
def main():
    # using the text file that the menu written in
    m = open("menu.txt", "r")
    menu = m.read()

    print(menu)
    m.close()

    # to match the input from user and the number to the related pizza
    pizza_dict = {
        1: ClassicPizza(),
        2: MargheritaPizza(),
        3: TurkPizza(),
        4: DominosPizza()
    }
    # to match the input from user and the number to the related sauce
    sauce_dict = {
        11: Olives(),
        12: Mushrooms(),
        13: GoatCheese(),
        14: Meat(),
        15: Onions(),
        16: Corn()
    }

    # taking order of the pizza
    p = "null value"
    while p == "null value":
        pizza_choice = int(input("What is your pizza choice? [1-4]"))
        if pizza_choice > 4:
            print("Please write a valid number")
        elif pizza_choice > 0:
            p = "valid value"
        else:
            print("Please write a valid number")

    # taking order of the sauce
    s = "null value"
    while s == "null value":
        sauce_choice = int(input("What is your sauce choice? [11-16]"))
        if sauce_choice > 16:
            print("Please write a valid number")
        elif sauce_choice > 10:
            s = "valid value"
        else:
            print("Please write a valid number")

    # taking order of the extra sauce
    more = "Yes"
    mult_sauce_choice = 0
    while more == "Yes":
        more = input("Do you want more sauces? (Yes or No)")
        if more == "Yes":
            mult_sauce_choice = int(
                input("What is your sauce choice? [11-16]"))
        elif more == "No":
            break
        else:
            "Please write Yes or No"

    # calculating the costs and printing to the screen
    pizza_cost = pizza_dict[pizza_choice].get_cost()
    sauce_cost = sauce_dict[sauce_choice].get_cost()
    total_cost = pizza_cost + sauce_cost
    if mult_sauce_choice == 0:
        total_cost = total_cost
    else:
        total_cost += sauce_dict[mult_sauce_choice].get_cost()
    print(f"Your total payment is {total_cost} .")

    # taking the user information
    user_id = input("ID = ")
    user_name = input("Name = ")
    credit_card_no = input("Credit Card No = ")
    credit_card_password = input("Credit Card Password = ")
    order_description = "The order of {} with a sauce of {}. The total cost is {}".format(
        pizza_dict[pizza_choice], sauce_dict[sauce_choice], total_cost)
    order_time = datetime.datetime.now()

    # inserting new order to the database
    with open('Order_Database.csv', 'w', newline='') as orders:
        writer = csv.writer(orders)
        writer.writerows([user_id], [user_name], [credit_card_no], [credit_card_password],
                           [order_description], [order_time])


main()
