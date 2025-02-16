from IPython.display import clear_output


cart = []

def addItem(item):
    clear_output()
    cart.append(item)
    print(f"{item} has been added.")
    
def removeItem(item):
    clear_output()
    try:
        cart.remove(item)
        print(f"{item} has been removed.")
    except:
        print(f"Sorry we could not remove the item! {item}")

def showCart():
    clear_output()
    if cart:
        print("Here is your cart:")
        for item in cart:
            print(f"- {item}")
    else:
        print("Cart is empty.")

def clearCart():
    clear_output()
    cart.clear()
    print("Your cart is empty.")

def main():
    done = False
    while not done:
        ans = input("Quit/Add/Remove/Show/Clear: ").capitalize()
        if ans == "Quit":
            print("Thanks for using our program.")
            showCart()
            done = True
        elif ans == "Add":
            item = input("What would you like to add? ").capitalize()
            addItem(item)
        elif ans == "Remove":
            showCart()
            item = input("What item would you like to remove? ").capitalize()
            removeItem(item)
        elif ans == "Show":
            showCart()
        elif ans == "Clear":
            clearCart()
        else:
            print("Invalid input, try again!")

if __name__ == "__main__":
    main()