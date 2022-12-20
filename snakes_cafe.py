intro = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""
print(intro)
order = {
    "wings": 0,
    "cookies": 0,
    "spring rolls": 0,
    "salmon": 0,
    "steak": 0,
    "meat tornado": 0,
    "a literal garden": 0,
    "ice cream": 0,
    "cake": 0,
    "pie": 0,
    "coffee": 0,
    "tea": 0,
    "unicorn tears": 0
}
ask_again = True
while ask_again:
    user_input = input("> ").lower()
    if user_input == "quit":
        ask_again = False
        break
    if user_input.lower() in order.keys():
        order[user_input] += 1
        if order[user_input] == 1:
            orders_text = "order"
        else:
            orders_text = "orders"
        print(f"** {order[user_input]} {orders_text} of {user_input} have been added to your meal **")
    else:
        print("That item is not on our menu. Please try again.")

if __name__ == "__snake-cafe__":
    print(__name__)
