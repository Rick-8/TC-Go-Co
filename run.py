import sys
import os
import datetime


# A simple stock system (dictionary to hold currency and stock quantities)
stock = {
    "USD": 10000,
    "EUR": 5000,
    "GBP": 3000,
    "JPY": 4000,
    "AUD": 6000,
}

# Sample currency exchange rates
exchange_rates = {
    "USD": 1.21,  
    "EUR": 1.15,
    "GBP": 1.0, # Base currency
    "JPY": 0.52,
    "AUD": 1.85
}

# Function for the main menu
def display_main_menu():
    """
    Displays the main menu to the user with options to access the Admin Panel, 
    Customer Panel, or Exit the system.
    """
    clear_screen()  # Clear the console before displaying the menu
    print("\n--- TC Go Co. ---")
    print("--- Currency System ---")
    print("1. Admin Panel")
    print("2. Customer Panel")
    print("3. Log Out")
    choice = input("Choose an option: ")
    return choice

# Function to clear the console
def clear_screen():
    """
    Clears the console output based on the operating system.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

# Function for the admin panel
def admin_panel():
    """
    Displays the Admin Panel menu with options to manage exchange rates, 
    currency stock, and view transaction logs.

    Returns:
        str: User's choice from the Admin Panel.
    """
    clear_screen()
    print("\n--- Admin Panel ---")
    print("1. View/Update Exchange Rates")
    print("2. Manage Currency Stock")
    print("3. View Transaction Logs")
    print("4. Back to Main Menu")
    choice = input("Choose an option: ")
    return choice

# Function to manage stock
def manage_stock():
    """
    Allows the admin to add or remove currency stock from the available 
    currencies.

    The function gives the admin a choice to add or remove stock, input the 
    amount, and updates the stock dictionary accordingly.
    """
    clear_screen()
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

# Function for the admin password login
def admin_login():
    """
    Prompts the user to log in to the Admin Panel by entering a password.
    """

    clear_screen()  # Clear the console before displaying the menu
    print("\n--- Admin Login ---")
    password = input("Enter admin password: ")
    if password == "admin123":  # Simple password for the admin
        print("Login successful!")
        return True
    else:
        print("Invalid password.")
        return False

# Function for the print receipt
def print_receipt(currency, amount, cost_in_gbp):
    """
    Prints a receipt after a successful transaction. It includes the currency purchased,
    amount, cost in GBP, and the current date/time.
    """
    # Get the current date and time
    transaction_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Print receipt
    print("\n---- RECEIPT ----")
    print("---- TC Go Co. ----")
    print("Stand 56, T4 Gatwick Airport")
    print(f"Transaction Date/Time: \n{transaction_time}")
    print("\n")
    print(f"Currency Purchased: {currency}")
    print(f"Amount: {amount:.2f} {currency}")
    print("\n")
    print(f"Total Cost: £{cost_in_gbp:.2f} GBP")
    print("\nThank you for your purchase!")
    print("----------------------")
    print("\n")
    input("Press Enter to return to the previous menu...")
    customer_panel()


# Sell currency (Till)
def sell_currency():
    """
    Allows customers to buy foreign currency from the shop.
    """
    clear_screen()
    print("\nSell Currency")
    print("Available Stock:")
    for currency, units in stock.items():
        print(f"{currency}: {units} units available")
        
    selected_currency = input("Enter the currency you want to buy (e.g., EUR, GBP): ").strip().upper()
    
    if selected_currency not in stock:
        print("Invalid currency selection. Please try again.")
        return
    
    try:
        amount = float(input(f"Enter the amount of {selected_currency} you want to buy: "))
        print("\n")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    # Check if sufficient stock is available
    if amount > stock[selected_currency]:
        print(f"Sorry, we only have {stock[selected_currency]} units of {selected_currency} available.")
        return
    
    # Calculate cost in GBP
    exchange_rate = exchange_rates[selected_currency]
    cost_in_gbp = amount / exchange_rate
    
    # Confirm transaction
    print(f"The cost for {amount:.2f} {selected_currency} is {cost_in_gbp:.2f} GBP.")
    confirm = input("Do you want to proceed with the transaction? (Y/N): ").strip().lower()
        
    if confirm == "y":
        # Deduct from stock
        stock[selected_currency] -= amount
        print(f"Transaction successful! You have purchased {amount:.2f} {selected_currency} for {cost_in_gbp:.2f} GBP.")
        print("\n")
        print(f"Remaining stock for {selected_currency}: {stock[selected_currency]:.2f} units.")
        
        # Ask if the customer wants a receipt
        receipt_choice = input("Do you want to print a receipt? (y/n): ").strip().lower()
        if receipt_choice == 'y':
            # Print receipt after the transaction
            print_receipt(selected_currency, amount, cost_in_gbp)
        else:
            print("No receipt will be printed.")
    else:
        print("Transaction cancelled.")
        input("\nPress Enter to return to the previous menu...")
        customer_panel()


# Function for the customer section
def customer_panel():
    """
    Displays the Customer Panel where users can view available currency stock 
    or exit the system.

    Returns:
        None: Exits when the customer chooses the option to leave.
    """
    clear_screen()
    print("\n--- Customer Panel ---")
    print("1. View Currency Stock")
    print("2. View Exchange Rates")
    print("3. Sell Currency (Till)")
    print("4. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        print("\n--- Currency Stock ---")
        for currency, quantity in stock.items():
           print(f"{currency}: {quantity} units available")
        input("\nPress Enter to return to the previous menu...")
    
    elif choice == "2":
        view_exchange_rates()
    elif choice == "3":
        sell_currency()        
    elif choice == "4":
        return
    else:
        print("Invalid choice.")

def view_exchange_rates():
    """
    Display current exchange rates for all available currencies.
    """
    clear_screen()
    print("\nCurrent Exchange Rates")
    print("----------------------")
    for currency, rate in exchange_rates.items():
        print(f"1 GBP = {rate} {currency}")
    input("\nPress Enter to return to the previous menu...")


def main():
    """
    The main function that controls the flow of the program. It displays the main 
    menu, handles navigation to either the Admin Panel or Customer Panel, and 
    exits the program when the user chooses to do so.

    Loops through the main menu until the user chooses to exit.
    """
    clear_screen()  # Clear the console before displaying the menu
    while True:
        choice = display_main_menu()
        if choice == "1":
            if admin_login():
                while True:
                    admin_choice = admin_panel()
                    if admin_choice == "1":
                        print("\n--- View/Update Exchange Rates ---")
                        print("Feature coming soon!")
                        input("Press Enter to return to the previous menu...")
                    elif admin_choice == "2":
                        manage_stock()
                    elif admin_choice == "3":
                        print("\n--- Transaction Logs ---")
                        print("Feature coming soon!")
                        input("Press Enter to return to the previous menu...")
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