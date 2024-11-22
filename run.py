import sys



# A simple stock system (dictionary to hold currency and stock quantities)
stock = {
    "USD": 1000,  # 1000 units of USD available
    "EUR": 500,   # 500 units of EUR available
    "GBP": 300,    # 300 units of GBP available
    "JPY": 400,    # 300 units of GBP available
    "AUD": 600,    # 300 units of GBP available
}

# Sample currency exchange rates
exchange_rates = {
    "USD": 1.0,  # Base currency
    "EUR": 0.92,
    "GBP": 0.78,
    "JPY": 148.58,
    "AUD": 1.54
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
    print("3. Log Out")
    choice = input("Choose an option: ")
    return choice

def admin_panel():
    """
    Displays the Admin Panel menu with options to manage exchange rates, 
    currency stock, and view transaction logs.

    Returns:
        str: User's choice from the Admin Panel.
    """
    print("\n--- Admin Panel ---")
    print("1. View/Update Exchange Rates")
    print("2. Manage Currency Stock")
    print("3. View Transaction Logs")
    print("4. Back to Main Menu")
    choice = input("Choose an option: ")
    return choice

def manage_stock():
    """
    Allows the admin to add or remove currency stock from the available 
    currencies.

    The function gives the admin a choice to add or remove stock, input the 
    amount, and updates the stock dictionary accordingly.
    """
    print("\n--- Manage Stock ---")
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. Back to Admin Menu")
    choice = input("Choose an option: ")
    
    if choice == "1":
        currency = input("Enter the currency to add stock (USD, EUR, GBP): ").upper()
        amount = int(input("Enter the amount to add: "))
        if currency in stock:
            stock[currency] += amount
            print(f"Added {amount} units of {currency}.")
        else:
            print("Invalid currency.")
    elif choice == "2":
        currency = input("Enter the currency to remove stock (USD, EUR, GBP): ").upper()
        amount = int(input("Enter the amount to remove: "))
        if currency in stock and stock[currency] >= amount:
            stock[currency] -= amount
            print(f"Removed {amount} units of {currency}.")
        else:
            print("Insufficient stock or invalid currency.")
    elif choice == "3":
        return
    else:
        print("Invalid choice.")

def admin_login():
    """
    Prompts the user to log in to the Admin Panel by entering a password.

    Returns:
        bool: True if login is successful, False if login fails.
    """
    print("\n--- Admin Login ---")
    password = input("Enter admin password: ")
    if password == "admin123":  # Simple password for the admin
        print("Login successful!")
        return True
    else:
        print("Invalid password.")
        return False


def customer_panel():
    """
    Displays the Customer Panel where users can view available currency stock 
    or exit the system.

    Returns:
        None: Exits when the customer chooses the option to leave.
    """
    print("\n--- Customer Panel ---")
    print("1. View Currency Stock")
    print("2. View Exchange Rates")
    print("3. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        print("\n--- Currency Stock ---")
        for currency, quantity in stock.items():
            print(f"{currency}: {quantity} units available")
    
    elif choice == "2":
        view_exchange_rates()
    elif choice == "3":
        return
    else:
        print("Invalid choice.")

def view_exchange_rates():
    """
    Display current exchange rates for all available currencies.
    """
    print("\nCurrent Exchange Rates")
    print("----------------------")
    for currency, rate in exchange_rates.items():
        print(f"{rate} {currency}")


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
            if admin_login():
                while True:
                    admin_choice = admin_panel()
                    if admin_choice == "1":
                        print("\n--- View/Update Exchange Rates ---")
                        print("Feature coming soon!")
                    elif admin_choice == "2":
                        manage_stock()
                    elif admin_choice == "3":
                        print("\n--- Transaction Logs ---")
                        print("Feature coming soon!")
                    elif admin_choice == "4":
                        break
                    else:
                        print("Invalid choice.")
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
# Run the program
if __name__ == "__main__":
    main()