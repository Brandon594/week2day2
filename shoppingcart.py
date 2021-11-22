"""
1) Build a Shopping Cart

Should have the following capabilities:

1) Takes in input
2) Stores user input into a list
3) User can add or delete items
4) User can see current shopping list
5) Loops until user 'quits'
6) Upon quiting the program, print out all items in the user's list
"""

shopping_cart = []

def run():
    done = False
    command = input("(a)dd, (r)emove, or (v)iew shopping cart, or (q)uit:")
    while done == False:
        if command == "a":
            added_item = input("add which item?")
            shopping_cart.append(str(added_item))
            command2 = input("(a)dd another or (b)ack?")
            if command2 == "b":
                run()
        elif command == "r":
            #removed_item == input("Remove which item?")
            #shopping_cart.remove(str(removed_item))
            shopping_cart.pop(-1)
            command2 = input("(a)nother or (b)ack?")
            if command2 == "b":
                run()
        elif command == "v":
            print(shopping_cart)
            run()
        elif command == "q":
            done = True
    if done == True:
        print("Your final shopping cart is:",shopping_cart)
        return

run()

#Module should have the following capabilities:
#1) Has a function to calculate the square footage of a room
#2) Has a function to calculate the circumference of a circle

def square_footage(x,y):
    ft2 = (x * y)
    print(ft2)
    return (ft2)

def circumference(r):
    cir = (2 * 3.14 * r)
    print(cir)
    return(cir)


