import os
import console
import customer_model
import item_ui



def show_menu():
    print()
    print("-"*10)
    print("customer")
    print("0. Go Back")
    print("1. Show all")
    print("2. Add")
    print("3. Remove")
    print("4. Update")
    print("-"*10)
    print()

def clear_screen():
    os.system("clear")

def print_all(customer_list):
    print(f"{'id':<15}{'name_pers':<15}{'ages_all':<15}{'hobby':<15}{'heh':<15}")
    print("-"*100)
    for customer_object in customer_list:
        print(f"{ customer_object.id:<15}{ customer_object.name_pers:<15}{ customer_object.ages_all:<15}{ customer_object.hobby:<15}{ customer_object.heh:<15}")

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
    customer_list = customer_model.find_all()
    print_all(customer_list)

def add():
    id = console.input_int("id: ")
    name_pers = console.input_str("name_pers: ")
    item_ui.show_all()
    print("--Pick one--")
    ages_all = console.input_int("ages_all: ")
    hobby = console.input_bool("hobby: ")
    heh = console.input_bool("heh: ")
    customer_object = customer_model.Customer( id, name_pers, ages_all, hobby, heh)
    customer_model.save(customer_object)

def remove():
    show_all()
    id = console.input_int("Enter id of customer you want to remove: ")
    customer_model.remove(id)

def update():
    show_all()
    print("Enter id of product you want to update.")
    id = console.input_int("id: ")
    name_pers = console.input_str("name_pers: ")
    AgesAll = console.input_int("ages_all: ")
    hobby = console.input_bool("hobby: ")
    heh = console.input_bool("heh: ")
    customer_object = customer_model.Customer( id, name_pers, AgesAll, hobby, heh)
    customer_model.update(customer_object)




    

if __name__ == "__main__":
    menu()