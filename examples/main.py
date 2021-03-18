import os
import console
import customer_ui
import item_ui
import hey_ui


def print_menu():
    print()
    print("App 0.1")
    print("-"*10)
    print("0. quit")
    print("1. customer ")
    print("2. item ")
    print("3. hey ")
    print("-"*10)
    print()

def menu():
    while True:
        print_menu()
        choice = console.input_str("Option: ")
        os.system("clear")
        if choice == "0":
            break
        if choice == "1":
            customer_ui.menu()
        if choice == "2":
            item_ui.menu()
        if choice == "3":
            hey_ui.menu()
        else:
            print("Command doesn't exist")

if __name__ == "__main__":
    menu()        
