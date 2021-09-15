import os
import console
import hey_model



def show_menu():
    print()
    print("-"*10)
    print("hey")
    print("0. Go Back")
    print("1. Show all")
    print("2. Add")
    print("3. Remove")
    print("4. Update")
    print("-"*10)
    print()

def clear_screen():
    os.system("clear")

def print_all(hey_list):
    print(f"{'id':<15}{'price':<15}{'asd':<15}{'uff':<15}")
    print("-"*100)
    for hey_object in hey_list:
        print(f"{ hey_object.id:<15}{ hey_object.price:<15}{ hey_object.asd:<15}{ hey_object.uff:<15}")

def menu():
    while True:
        show_menu()
        choice = console.input_str("Option: ")
        clear_screen()
        if choice == "0":
            break
        elif choice == "1":
            show_all()
        elif choice == "2":
            add()
        elif choice == "3":
            remove()
        elif choice == "4":
            update()
        else:
            print("Command doesn't exist.")

def show_all():
    hey_list = hey_model.find_all()
    print_all(hey_list)

def add():
    id = console.input_int("id: ")
    price = console.input_float("price: ")
    asd = console.input_str("asd: ")
    uff = console.input_str("uff: ")
    hey_object = hey_model.Hey( id, price, asd, uff)
    hey_model.save(hey_object)

def remove():
    show_all()
    id = console.input_int("Enter id of hey you want to remove: ")
    hey_model.remove(id)

def update():
    show_all()
    print("Enter id of product you want to update.")
    id = console.input_int("id: ")
    price = console.input_float("price: ")
    asd = console.input_str("asd: ")
    uff = console.input_str("uff: ")
    hey_object = hey_model.Hey( id, price, asd, uff)
    hey_model.update(hey_object)




    

if __name__ == "__main__":
    menu()