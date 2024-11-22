
# A simple stock system (dictionary to hold currency and stock quantities)
stock = {
    "USD": 1000,  # 1000 units of USD available
    "EUR": 500,   # 500 units of EUR available
    "GBP": 300    # 300 units of GBP available
}


def display_main_menu():
    """
    Displays the main menu to the user with options to access the Admin Panel, 
    Customer Panel, or Exit the system.
    """
    print("\n--- TC Go Co. ---")
    print("--- Currency Stock System ---")
    print("1. Admin Panel")
    print("2. Customer Panel")
    print("3. Exit")
    choice = input("Choose an option: ")
    return choice

def customer_panel():
    """
    Displays the Customer Panel where users can view available currency stock 
    or exit the system.

    Returns:
        None: Exits when the customer chooses the option to leave.
    """
    print("\n--- Customer Panel ---")
    print("1. View Currency Stock")
    print("2. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        print("\n--- Currency Stock ---")
        for currency, quantity in stock.items():
            print(f"{currency}: {quantity} units available")
    elif choice == "2":
        return
    else:
        print("Invalid choice.")

def main():
    """
    The main function that controls the flow of the program. It displays the main 
    menu, handles navigation to either the Admin Panel or Customer Panel, and 
    exits the program when the user chooses to do so.

    Loops through the main menu until the user chooses to exit.
    """
    while True:
        choice = display_main_menu()

        if choice == "1":
            print("Coming Soon")
            main()
        elif choice == "2":
            while True:
                customer_choice = customer_panel()
                if customer_choice is None:
                        break
        elif choice == "3":
            print("Exiting the system...")
            sys.exit()
        else:
            print("Invalid option. Please choose again.")
main()