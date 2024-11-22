def display_main_menu():
    """
    Displays the main menu to the user with options to access the Admin Panel, 
    Customer Panel, or Exit the system.

    Returns:
        str: User's choice from the main menu.
    """
    print("\n--- Currency Stock System ---")
    print("1. Admin Panel")
    print("2. Customer Panel")
    print("3. Exit")
    choice = input("Choose an option: ")
    return choice

display_main_menu()