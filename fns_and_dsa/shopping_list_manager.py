#shoppinglist

shopping_list = []

def display_menu():
    print("\n=== Shopping List Menu ===")
    print("1. Add item")
    print("2. Remove item")
    print("3. View shopping list")
    print("4. Exit")

def add_item():
    item = input("Enter the item to add: ").strip()
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")

def remove_item():
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been remove from your shopping list.")

def view_list():
    if shopping_list:
        print("\n Your Shopping List:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}.{item}")
    else:
        print("\nYour shopping list is currently empty")

#mainloop

while True:
    display_menu()
    choice = input("Choose anoption (1-4): ").strip()

    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        view_list()
    elif choice == '4':
        print("Exiting the shopping list app. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
