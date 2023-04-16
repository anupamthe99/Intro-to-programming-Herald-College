product={}

def add_item():
    print("Add an item")
    code=input("Enter the code of the item: ")
    name=input("Enter the name of the item: ")
    quantity=int(input("Enter the quantity: "))
    price=float(input("Enter the price: "))
    product[code]={"name":name,"quantity":quantity,"price":price}
    print("Item added successfully")
    print(product)

def remove_item():
    print("Remove an item")
    code=input("Enter the code of the item: ")
    if code in product:
        del product[code]
        print("Item removed successfully")
    else:
        print("Item not found")
    print(product)

def update_item():
    print("Update an item")
    code=input("Enter the code of the item: ")
    if code in product:
        name=input("Enter the name of the item: ")
        quantity=int(input("Enter the quantity: "))
        price=float(input("Enter the price: "))
        product[code]={"name":name,"quantity":quantity,"price":price}
        print("Item updated successfully")
    else:
        print("Item not found")
    print(product)

def display_items():
    print("Display all items")
    print(product)
    
while True:
    print("Welcome to the Inventory Management System")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Update an item")
    print("4. Display all items")
    print("5. Exit")
    
    choice=int(input("Enter your choice: "))

    if choice==1:
        add_item()
    elif choice==2:
        remove_item()
    elif choice==3:
        update_item() 
    elif choice==4:
        display_items()
    elif choice==5:
        break
    else:
        print("Invalid choice")
