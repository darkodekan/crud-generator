import os
import console
import item_model
import customer_ui



def show_menu():
    print()
    print("-"*10)
    print("item")
    print("0. Go Back")
    print("1. Show all")
    print("2. Add")
    print("3. Remove")
    print("4. Update")
    print("-"*10)
    print()

def clear_screen():
    os.system("clear")

def print_all(item_list):
    print(f"{'id':<15}{'name':<15}{'price':<15}{'customer_id':<15}{'asd':<15}")
    print("-"*100)
    for item_object in item_list:
        print(f"{ item_object.id:<15}{ item_object.name:<15}{ item_object.price:<15}{ item_object.customer_id:<15}{ item_object.asd:<15}")

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
    item_list = item_model.find_all()
    print_all(item_list)

def add():
    id = console.input_int("id: ")
    name = console.input_str("name: ")
    price = console.input_float("price: ")
    customer_ui.show_all()
    print("--Pick one--")
    customer_id = console.input_int("customer_id: ")
    asd = console.input_str("asd: ")
    item_object = item_model.Item( id, name, price, customer_id, asd)
    item_model.save(item_object)

def remove():
    show_all()
    id = console.input_int("Enter id of item you want to remove: ")
    item_model.remove(id)

def update():
    show_all()
    print("Enter id of product you want to update.")
    id = console.input_int("id: ")
    name = console.input_str("name: ")
    price = console.input_float("price: ")
    customer_id = console.input_int("customer_id: ")
    asd = console.input_str("asd: ")
    item_object = item_model.Item( id, name, price, customer_id, asd)
    item_model.update(item_object)




    

if __name__ == "__main__":
    menu()