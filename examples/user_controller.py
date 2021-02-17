import os
import product_model

def show_menu():
    print()
    print("-"*10)
    print("product")
    print("0. Go Back")
    print("1. Show all")
    print("2. Add")
    print("3. Remove")
    print("4. Update")
    print("-"*10)
    print()

def clear_screen():
    os.system("clear")

def print_all(product_list):
    print(f"{'id':<15}{'name':<15}")
    print("-"*100)
    for product in product_list:
        print(f"{ product.id:<15}{ product.name:<15}")

def menu():
    while True:
        show_menu()
        choice = input("Option: ")
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
    product_list = product_model.find_all()
    print_all(product_list)

def add():
    
    id = int(input("id: "))
    
    name = input("name: ")
    
    product_object = product_model.product( id, name)
    product_model.save(product_object)

def remove():
    show_all()
    id = int(input("Enter id of product you want to remove: "))
    product_model.remove(id)

def update():
    show_all()
    id = int(input("Enter id of product you want to update: "))
   
    name = input("name: ")
    
    product_object = product_model.product( id, name)
    product_model.update(product_object)




    

if __name__ == "__main__":
    menu()