import sys
import os
import datetime
import time


stock = {
    "USD": 10000,
    "EUR": 5000,
    "GBP": 3000,
    "JPY": 4000,
    "AUD": 6000,
}


exchange_rates = {
    "USD": 1.21,
    "EUR": 1.15,
    "GBP": 1.0,
    "JPY": 0.52,
    "AUD": 1.85
}


def display_main_menu():
    """
    Displays the main menu to the user with options to access the
    Admin Panel, Customer Panel, or Exit the system.
    """
    clear_screen()
    print("\n--- TC Go Co. ---")
    print("--- Currency System ---")
    print("\n")
    print("1. Admin Panel")
    print("2. Customer Panel")
    print("3. Log Out")
    print("\nPress the corresponding number key to choose an option.")

    while True:
        choice = input("\nPlease choose an option: ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid option. Please select 1, 2, or 3.")


def clear_screen():
    """
    Clears the console output based on the operating system.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def admin_panel():
    """
    Displays the Admin Panel menu with options to manage exchange rates,
    currency stock, and view transaction logs.
    """
    clear_screen()
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
    clear_screen()
    print("\n--- Manage Stock ---")
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. Back to Admin Menu")
    choice = input("Choose an option: ")
    if choice == "1":
        clear_screen()
        currency_message = "Enter the currency to add stock (USD, EUR, GBP):"
        currency = input(f"{currency_message}").upper()
        amount = int(input("Enter the amount to add: "))
        if currency in stock:
            stock[currency] += amount
            print(f"Added {amount} units of {currency}.")
            time.sleep(2)
            manage_stock()
        else:
            print("Invalid currency.")
            time.sleep(3)
            manage_stock()

    elif choice == "2":
        clear_screen()
        rc_message = "Enter the currency to remove stock (USD, EUR, GBP):"
        currency = input(f"{rc_message}").upper()
        amount = int(input("Enter the amount to remove: "))
        if currency in stock and stock[currency] >= amount:
            stock[currency] -= amount
            print(f"Removed {amount} units of {currency}.")
            time.sleep(2)
            manage_stock()
        else:
            print("Insufficient stock or invalid currency.")
            time.sleep(3)
            manage_stock()
    elif choice == "3":
        return
    else:
        print("Invalid choice.")


def admin_login():
    """
    Prompts the user to log in to the Admin Panel by entering a password.
    """

    clear_screen()
    print("\n--- Admin Login ---")
    password = input("Enter admin password: ")
    if password == "admin123":
        print("Login successful!")
        time.sleep(1)
        return True        
    else:
        print("Invalid password.")
        time.sleep(3)
        return False


def print_receipt(currency, amount, cost_in_gbp):
    """
    Prints a receipt after a successful transaction.
    It includes the currency purchased, amount, cost in GBP, 
    and the current date/time.
    """
    transaction_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
    input("\nPress Enter to return to the previous menu...")
    customer_panel()


def sell_currency():
    """
    Allows customers to buy foreign currency from the shop.
    """
    clear_screen()
    print("\nSell Currency")
    print("Available Stock:")
    for currency, units in stock.items():
        print(f"{currency}: {units} units available")

    sc_message = "please enter currency code e.g USD, EUR, JPY..."
    selected_currency = input(f"{sc_message}").strip().upper()

    if selected_currency not in stock:
        print("Invalid currency selection. Please try again.")
        time.sleep(2)
        return

    sc_a_message = f"Enter the amount of {selected_currency} you want to buy:"
    try:
        amount = float(input(f"{sc_a_message}"))
        print("\n")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        time.sleep(2)
        return

    if amount > stock[selected_currency]:
        s_message = f"\nSorry, we only have{stock[selected_currency]} left."
        print(f"{s_message}")
        return

    exchange_rate = exchange_rates[selected_currency]
    cost_in_gbp = amount / exchange_rate

    print(f"{amount:.2f} {selected_currency} is {cost_in_gbp:.2f} GBP.")
    confirm = input("Do you wish to proceed? (Y/N): ").strip().lower()

    if confirm == "y":

        stock[selected_currency] -= amount
        print(f"You have purchased {amount:.2f} "
              f"{selected_currency} for {cost_in_gbp:.2f} GBP.")

        print("\n")
        print(f"Remaining stock{selected_currency}:"
              f"{stock[selected_currency]:.2f} units.")

        print("\n")
        receipt_message = "Do you want to print a receipt? (y/n):"
        receipt_choice = input(f"{receipt_message}").strip().lower()
        if receipt_choice == 'y':

            print_receipt(selected_currency, amount, cost_in_gbp)
        else:
            print("No receipt will be printed.")
            time.sleep(2)
            customer_panel()
    else:
        print("Transaction cancelled.")
        input("\nPress Enter to return to the previous menu...")
        customer_panel()


def customer_panel():
    """
    Displays the Customer Panel where users can view available 
    currency stock or exit the system.

    Returns:
        None: Exits when the customer chooses the option to leave.
    """
    clear_screen()
    print("---- TC Go Co. ----")
    print("--- Customer Panel ---")
    print("\n1. View Currency Stock")
    print("2. View Exchange Rates")
    print("3. Sell Currency (Till)")
    print("4. Exit")
    print("\n")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        clear_screen()
        print("\n--- Currency Stock ---")
        for currency, quantity in stock.items():
            print(f"{currency}: {quantity} units available")
        input("\nPress Enter to return to the previous menu...")
        customer_panel()

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
    print("\n---- TC Go Co. ----")
    print("\nCurrent Exchange Rates")
    print("----------------------")
    for currency, rate in exchange_rates.items():
        print(f"1 GBP = {rate} {currency}")
    input("\nPress Enter to return to the previous menu...")
    customer_panel()


def main():
    """
    The main function that controls the flow of the program. 
    It displays the main menu, handles navigation to either 
    the Admin Panel or Customer Panel, and exits the program 
    when the user chooses to do so.

    Loops through the main menu until the user chooses to exit.
    """

    clear_screen()
    while True:
        choice = display_main_menu()
        if choice == "1":
            if admin_login():
                while True:
                    admin_choice = admin_panel()
                    if admin_choice == "1":
                        print("\n--- View/Update Exchange Rates ---")
                        print("Feature coming soon!")
                        time.sleep(2)
                        admin_panel()
                    elif admin_choice == "2":
                        manage_stock()
                    elif admin_choice == "3":
                        print("\n--- Transaction Logs ---")
                        print("Feature coming soon!")
                        time.sleep(2)
                        admin_panel()
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
            time.sleep(2)
            clear_screen()
            sys.exit()

        else:
            print("Invalid option. Please choose again.")
            time.sleep(2)


if __name__ == "__main__":
    main()
    print("\n")
