import random

# Global sets to track orders
name_tea = set()
name_coffee = set()
name_soda = set()
name_smoothie = set()
recept = set()

def mainmenu():
    print("\n[CHOOSE THE MENU]")
    print("1. TEA")
    print("2. COFFEE")
    print("3. SODA")
    print("4. SMOOTHIE")
    print("5. GAME")
    print("6. CHECK DISCOUNT")
    print("0. TOTAL")

def show_menu(menu):
    """Displays a menu with items and their prices."""
    for i, (item, price) in enumerate(menu.items(), 1):
        print(f"{i}. {item} - {price} Baht")

def order_drinks(menu, order_set):
    """Handles ordering drinks from a specific menu."""
    total_cost = 0
    while True:
        print("\nType 'end' to stop ordering.")
        choice = input("Choose menu item (type name): ").strip().lower()
        if choice == "end":
            break
        elif choice in menu:
            order_set.add(choice)
            total_cost += menu[choice]
            recept.add(choice)
            print(f"Added {choice}. Current total: {total_cost} Baht")
        else:
            print(f"Invalid choice: {choice}. Please try again.")
    return total_cost

def tea():
    menu_tea = {
        "thai tea": 40, "taiwan tea": 40, "brown sugar tea": 30,
        "lemon tea": 45, "green tea": 50, "iced black tea": 30,
        "jasmine tea": 45, "rose tea": 35
    }
    print("\nTEA MENU")
    show_menu(menu_tea)
    return order_drinks(menu_tea, name_tea)

def coffee():
    menu_coffee = {
        "americano": 40, "latte": 55, "cappuccino": 50,
        "mocca": 45, "espresso": 40, "macchiato": 60
    }
    print("\nCOFFEE MENU")
    show_menu(menu_coffee)
    return order_drinks(menu_coffee, name_coffee)

def soda():
    menu_soda = {
        "peppsi": 25, "red soda": 30, "lemon soda": 30,
        "yusu soda": 40, "strawberry soda": 40,
        "lychee soda": 45, "melon soda": 45, "ume soda": 45
    }
    print("\nSODA MENU")
    show_menu(menu_soda)
    return order_drinks(menu_soda, name_soda)

def smoothie():
    menu_smoothie = {
        "oreo smoothie": 55, "ovaltine smoothie": 55, "chocolate smoothie": 60,
        "strawberry milk smoothie": 65, "melon milk smoothie": 65,
        "yusu milk smoothie": 65, "lychee milk smoothie": 65
    }
    print("\nSMOOTHIE MENU")
    show_menu(menu_smoothie)
    return order_drinks(menu_smoothie, name_smoothie)

def ran(total):
    """Random game for discounts."""
    chances = total // 100
    discount = 0
    print(f"\nYou have {chances} chance(s) to play the game.")
    for i in range(chances):
        print(f"\nRound {i + 1}")
        random_number = random.randint(1, 11)
        print(f"You got {random_number}.")
        if random_number % 11 == 0:
            print("---> YOU WIN!")
            discount += 10
        else:
            print("YOU LOSE.")
    if discount > 0:
        print(f"\nCongratulations! You won a total discount of {discount} Baht.")
    else:
        print("\nThank you for playing!")
    return discount

def discount(total):
    """Calculates discount based on total amount spent."""
    if total >= 400:
        rate = 20
    elif total >= 300:
        rate = 15
    elif total >= 200:
        rate = 10
    elif total >= 100:
        rate = 5
    else:
        rate = 0
    discount_amount = total * rate // 100
    if discount_amount > 0:
        print(f"\nYou received a {rate}% discount: {discount_amount} Baht.")
    else:
        print("\nNo discount applicable.")
    return discount_amount

def farewell(total):
    """Prints a summary and farewell message."""
    print("\n--------------")
    print(f"Your total orders: {recept}")
    print(f"Total price: {total} Baht")
    print("Thank you for using our service!")
    print("--------------")

def main():
    total = 0
    while True:
        mainmenu()
        try:
            choice = int(input("Select menu (type number): "))
        except ValueError:
            print("\nPlease enter a valid number.")
            continue

        if choice == 0:
            farewell(total)
            break
        elif choice == 1:
            total += tea()
        elif choice == 2:
            total += coffee()
        elif choice == 3:
            total += soda()
        elif choice == 4:
            total += smoothie()
        elif choice == 5:
            total -= ran(total)
        elif choice == 6:
            total -= discount(total)
        else:
            print("\nInvalid option. Please choose again.")

if __name__ == "__main__":
    main()
