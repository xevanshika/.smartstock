import json
import os

# ==========================
# FILE SETUP
# ==========================

DATA_FILE = "inventory.json"


# ==========================
# LOAD DATA
# ==========================

def load_data():

    if os.path.exists(DATA_FILE):

        with open(DATA_FILE, "r") as file:
            return json.load(file)

    return {
        "products": {},
        "sales": []
    }


# ==========================
# SAVE DATA
# ==========================

def save_data(data):

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ==========================
# ADD PRODUCT
# ==========================

def add_product(data):

    print("\n========== ADD PRODUCT ==========")

    product_id = input("Enter Product ID: ").upper()

    if product_id in data["products"]:
        print("❌ Product already exists!")
        return


    name = input("Enter Product Name: ").title()


    while True:
        try:
            price = float(input("Enter Price: "))

            if price <= 0:
                print("Price should be greater than 0")
                continue

            break

        except:
            print("Enter valid price")


    while True:
        try:
            quantity = int(input("Enter Quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative")
                continue

            break

        except:
            print("Enter valid quantity")


    data["products"][product_id] = {

        "name": name,
        "price": price,
        "quantity": quantity
    }


    save_data(data)

    print("✅ Product Added Successfully")


# ==========================
# VIEW PRODUCTS
# ==========================

def view_products(data):

    print("\n========== PRODUCT LIST ==========")


    if not data["products"]:
        print("No products available")
        return


    for product_id, product in data["products"].items():

        print("-------------------------")
        print("ID:", product_id)
        print("Name:", product["name"])
        print("Price: ₹", product["price"])
        print("Quantity:", product["quantity"])



# ==========================
# SEARCH PRODUCT
# ==========================

def search_product(data):

    print("\n========== SEARCH PRODUCT ==========")

    search = input("Enter Product ID: ").upper()


    if search in data["products"]:

        product = data["products"][search]

        print("\nProduct Found")
        print("----------------")
        print("Name:", product["name"])
        print("Price: ₹", product["price"])
        print("Quantity:", product["quantity"])


    else:

        print("❌ Product not found")
# ==========================
# UPDATE STOCK
# ==========================

def update_stock(data):

    print("\n========== UPDATE STOCK ==========")

    product_id = input("Enter Product ID: ").upper()


    if product_id not in data["products"]:
        print("❌ Product not found")
        return


    try:
        add_quantity = int(input("Enter quantity to add: "))

        data["products"][product_id]["quantity"] += add_quantity

        save_data(data)

        print("✅ Stock Updated")

    except:
        print("❌ Enter valid quantity")



# ==========================
# DELETE PRODUCT
# ==========================

def delete_product(data):

    print("\n========== DELETE PRODUCT ==========")

    product_id = input("Enter Product ID: ").upper()


    if product_id in data["products"]:

        del data["products"][product_id]

        save_data(data)

        print("✅ Product Deleted")


    else:

        print("❌ Product not found")



# ==========================
# SELL PRODUCT
# ==========================

def sell_product(data):

    print("\n========== SELL PRODUCT ==========")

    product_id = input("Enter Product ID: ").upper()


    if product_id not in data["products"]:

        print("❌ Product not found")
        return



    try:

        quantity = int(input("Enter Quantity: "))


        available = data["products"][product_id]["quantity"]


        if quantity > available:

            print("❌ Not enough stock available")

            return



        data["products"][product_id]["quantity"] -= quantity



        bill = quantity * data["products"][product_id]["price"]



        sale = {

            "product": data["products"][product_id]["name"],
            "quantity": quantity,
            "amount": bill
        }



        data["sales"].append(sale)


        save_data(data)


        print("✅ Sale Successful")
        print("Total Bill: ₹", bill)



    except:

        print("❌ Invalid quantity")




# ==========================
# SALES REPORT
# ==========================

def sales_report(data):

    print("\n========== SALES REPORT ==========")


    if not data["sales"]:

        print("No sales yet")

        return



    total = 0


    for sale in data["sales"]:

        print("----------------")
        print("Product:", sale["product"])
        print("Quantity:", sale["quantity"])
        print("Amount: ₹", sale["amount"])


        total += sale["amount"]



    print("----------------")
    print("Total Revenue: ₹", total)




# ==========================
# LOW STOCK ALERT
# ==========================

def low_stock(data):

    print("\n========== LOW STOCK ==========")


    found = False


    for pid, product in data["products"].items():


        if product["quantity"] <= 5:


            found = True

            print("----------------")
            print("ID:", pid)
            print("Name:", product["name"])
            print("Stock:", product["quantity"])



    if found == False:

        print("No low stock products")




# ==========================
# MAIN MENU
# ==========================

def main():

    data = load_data()


    while True:


        print("\n==============================")
        print("       SMART STOCK PRO")
        print("==============================")

        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. Delete Product")
        print("6. Sell Product")
        print("7. Sales Report")
        print("8. Low Stock Alert")
        print("9. Exit")


        choice = input("\nEnter Choice: ")



        if choice == "1":

            add_product(data)



        elif choice == "2":

            view_products(data)



        elif choice == "3":

            search_product(data)



        elif choice == "4":

            update_stock(data)



        elif choice == "5":

            delete_product(data)



        elif choice == "6":

            sell_product(data)



        elif choice == "7":

            sales_report(data)



        elif choice == "8":

            low_stock(data)



        elif choice == "9":

            save_data(data)

            print("Thank you for using SmartStock Pro!")

            break



        else:

            print("❌ Invalid Choice")




# ==========================
# START PROGRAM
# ==========================

if __name__ == "__main__":

    main()