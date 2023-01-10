# learnt about tabulate:
#   https://pypi.org/project/tabulate/
# text formatting in the terminal:
#   https://towardsdatascience.com/coloured-text-terminal-python-dc5692ee6319
#   https://appdividend.com/2022/07/27/how-to-print-bold-python-text/
# from Logan's lecture on I/O used some fancy symbols throughout the project
#   https://fsymbols.com/keyboard/windows/alt-codes/list/


from tabulate import tabulate


# if you have not got the tabulate module installed, please install it
# instructions here: https://pypi.org/project/tabulate/
# ========The beginning of the class==========
class Shoe:
    """A class for creating shoe objects
    """

    def __init__(self, country, code, product, cost, quantity):
        """Initializing the shoe object

        Args:
            country (string): the country where the shoe is sold
            code (string): the stock keeping unit code
            product (string): the product name
            cost (integer): the cost of 1 quantity of the product
            quantity (integer): the quantity in stock
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """A function that returns the cost of the object

        Returns:
            int: the cost of 1 quantity of the product
        """
        return self.cost

    def get_quantity(self):
        """A function that returns the quantity in stock for the object.

        Returns:
            int: the quantity in stock for the object
        """
        return self.quantity

    def __str__(self):
        """Converts the object into formatted string

        Returns:
            str: combines all the parameters of the Class object into one string
        """
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    """A function that reads the inventory.txt file and
    returns a 2D list of items.

    Returns:
        list: each parameter of the products are list items and 
              are nested inside a bigger list
    """
    with open("inventory.txt", "r") as f:
        data = f.readlines()[1:]
        for i in range(len(data)):
            data[i] = data[i].strip("\n").split(",")
    f.close()
    return data
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''


def capture_shoes():
    """A function that capture's the Shoe object details from the user,
    creates a new object and is adding it to the inventory.txt
    """
    shoe_list = read_shoes_data()
    # requesting user inputs
    country = input("Enter the country where the product is sold: ")
    code = input("Enter the code of the product: ")
    product = input("Enter the product name: ")
    while True:
        # checking if user cost input is valid
        cost = input("Enter the cost of the product: ")
        try:
            float(cost)
            break
        except:
            print("Incorrect value entered. Try again (should be a number).")
    ask = True
    display = []
    # Checking if the product exists in the database
    # includes and displays the duplicated product info
    for row in shoe_list:
        if row[2] == product and row[0] == country and row[1] == code and row[3] == cost:
            print("Product already exists. Consider updating the quantity.")
            display.append(row)
            ask = False
    if len(display) != 0:
        print(tabulate(display, headers=["Country", "Code", "Product", "Cost", "Quantity"], tablefmt="rounded_grid",
                       numalign="left"))
    # if product doesn't exist, ask for the quantity on hand
    # and create and add the product to inventory
    # then update the "shoe_list" with the updated inventory
    else:
        while ask == True:
            quantity = input("Enter the quantity in stock: ")
            try:
                int(quantity)
                ask = False
                shoe = f"\n{Shoe(country, code, product, cost, quantity).__str__()}"
                with open("inventory.txt", "a") as f:
                    f.write(shoe)
                f.close()
                shoe_list = read_shoes_data()
                print("Product added to inventory.")
            except:
                print("Incorrect value entered. Try again (should be a whole number).")


def view_all():
    """A function that allows the user to view all products and
    their current stored information
    """
    shoe_data = read_shoes_data()
    data = tabulate(shoe_data, headers=["Country", "Code", "Product", "Cost", "Quantity"], tablefmt="rounded_grid",
                    numalign="left")
    print("""
                    ╔════════════════════════════╗
                      \033[1m\033[92mCurrent Inventory on Hand\033[0m
                    ╚════════════════════════════╝
""")
    print(data)
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''


def update_inventory(modified_list):
    """A function that updates the inventory.txt database.

    Args:
        modified_list (list): the new and modified list of objects
    """
    new_inventory = Shoe("Country", "Code", "Product", "Cost", "Quantity").__str__()
    for list in modified_list:
        new_inventory += f"\n{Shoe(list[0], list[1], list[2], list[3], list[4]).__str__()}"
    with open("inventory.txt", "r") as f:
        pass
    f.close()
    with open("inventory.txt", "w") as f:
        f.write(new_inventory)
    f.close()


def re_stock():
    """A function that allows the user to re-stock the lowest quantity product
    to a desired quantity.
    If there are more products with the same low quantity, the user is asked if
    should 1 or all be updated.
    If there are any products with missing/incorrect quantity information in inventory.txt,
    these will be temporarily removed from calculation but added to the same position once 
    the calculation has been done.    
    """
    shoe_list = read_shoes_data()
    try:
        low = int(shoe_list[0][-1])
    except:
        print("The first item doesn't have any quantity recorded")
    low_rows = []
    # getting the lowest quantity and
    # checking for errors for the quantity value (i.e. chars entered instead of numbers)
    for index, _ in enumerate(shoe_list):
        try:
            if int(_[-1]) < low:
                low = int(_[-1])
        except:
            print(f"Item at row {index + 2} doesn't have correct value as quantity or it is empty.")
            to_remove = (index, _)
            to_remove_str = Shoe(_[0], _[1], _[2], _[3], _[4]).__str__()
            print(f"{to_remove_str} will be removed from calculation until rectified.")
            shoe_list.remove(_)
    # getting all the rows with min value stock
    for index, _ in enumerate(shoe_list):
        if int(_[-1]) == low:
            low_rows.append(index)
    # checking if there is only one item with the lowest quantity
    display = []
    titles = ["ID", "Country", "Code", "Product", "Cost", "Quantity"]
    if len(low_rows) < 2:
        for index, row in enumerate(shoe_list):
            if row == shoe_list[low_rows[0]]:
                row.insert(0, str(index))
                display.append(row)
        print(tabulate(display, headers=titles, tablefmt="rounded_grid", numalign="left"))
        # asking the user if quantity should be updated
        user_choice = input("Would you like to update re-stock the item? (y/n) ").lower()
        while True:
            if user_choice == "y":
                # getting the quantity to update to from user
                while True:
                    user_quantity = input("Please enter the quantity to re-stock to: ")
                    try:
                        # checking that the user input is a valid number
                        user_quantity = int(user_quantity)

                    except ValueError:
                        user_quantity = input("Please enter the quantity to re-stock to: ")
                    # updating the quantity in "shoe_list" and removing the preceding index
                    shoe_list[low_rows[0]][-1] = user_quantity
                    shoe_list[low_rows[0]].pop(0)
                    try:
                        # checking if there was any item removed and
                        # if so, adding it back to the list
                        shoe_list.insert(to_remove[0], to_remove[1])
                    except:
                        pass
                    # updating the "inventory.txt" and displaying an appropriate message
                    update_inventory(shoe_list)
                    print("Product updated")
                    break
                break
            elif user_choice == "n":
                break
            else:
                print("You have not entered a valid option")
                user_choice = input("Would you like to re-stock the item? (y/n)").lower()
    else:
        # the calculation for more products with the same low quantity
        # displaying all the products that match criteria as well as their index
        for index, row in enumerate(shoe_list):
            for i in low_rows:
                if row == shoe_list[int(i)]:
                    row.insert(0, str(index))
                    display.append(row)
        print(tabulate(display, headers=titles, tablefmt="rounded_grid", numalign="left"))
        user_choice = ''
        # getting user input on update type and
        # giving an option for exiting the loop
        while user_choice != "3":
            user_choice = input("""Please select from below:
1 - re-stock 1 item
2 - re-stock all items
3 - no update
""")
            if user_choice in ["1", "2", "3"]:
                while True:
                    # updating 1 item from the list
                    if user_choice == "1":
                        user_quantity = input("Please enter the quantity to update to: ")
                        # user input error checking
                        try:
                            user_quantity = int(user_quantity)
                        except ValueError:
                            print("Please enter a valid number.")

                        user_id_choice = input("Please type in the ID of the product to update: ")
                        try:
                            user_id_choice = int(user_id_choice)
                        except ValueError:
                            print("Please enter a valid ID from the list provided.")
                        if user_id_choice not in low_rows:
                            print("The ID entered is not on the list provided")
                        else:
                            # updating the product selected with the input quantity
                            for i, row in enumerate(shoe_list):
                                if i == user_id_choice:
                                    shoe_list[user_id_choice][-1] = user_quantity
                                    # removing the leading index number from the updated number
                                    shoe_list[user_id_choice].pop(0)
                                    # removing the updated item from the list of low stock products
                                    low_rows.pop(low_rows.index(user_id_choice))
                                    row.insert(0, str(i))
                                    display.pop(display.index(row))
                            # removing the leading index number from the rest of the products
                            for row in shoe_list:
                                if row[0].isdigit():
                                    shoe_list[shoe_list.index(row)].pop(0)
                            try:
                                # checking if there was any item temporarily removed from the list and,
                                # if so, adding it back to the list in the same row
                                shoe_list.insert(to_remove(0), to_remove(1))
                            except:
                                pass
                            # updating the "inventory.txt" database with the newest information
                            update_inventory(shoe_list)
                            # printing an appropriate message and,
                            # if there are any other items with lowest quantity, their summary
                            print("Product re-stocked")
                            if len(low_rows) != 0:
                                print(tabulate(display, headers=titles, tablefmt="rounded_grid", numalign="left"))
                            break
                    elif user_choice == "2":
                        # calculation to update all items with the same lowest quantity at once
                        user_quantity = input("Please enter the quantity to update to: ")
                        try:
                            user_quantity = int(user_quantity)
                        except ValueError:
                            print("Please enter a valid number.")
                        for i, row in enumerate(shoe_list):
                            for item in low_rows:
                                if i == int(item):
                                    shoe_list[i][-1] = user_quantity
                                if shoe_list[i][0].isdigit():
                                    shoe_list[i].pop(0)
                        try:
                            shoe_list.insert(to_remove(0), to_remove(1))
                        except:
                            pass
                        update_inventory(shoe_list)
                        print("Products re-stocked.")
                        break
                    # exiting the loop
                    elif user_choice == "3":
                        break
                    else:
                        print("You have not entered a valid choice. Please try again.")


def search_shoe():
    """A function that requests the user to input a desired code and
    displays the product details linked to the code.
    Displays an error message if the code is not linked to any product.
    """
    shoe_list = read_shoes_data()
    sku = input("What is the product code? ")
    display = [["Country", "Code", "Product", "Cost", "Quantity"]]
    count = 0
    for _ in shoe_list:
        if _[1] == sku:
            display.append(_)
            count += 1
    if count > 0:
        print(tabulate(display, headers="firstrow", tablefmt="rounded_grid", numalign="left"))
    else:
        print("Product code is not in the database.")


def value_per_item():
    """A function that displays all the products, it calculates the value per product and
    it adds an extra column "Stock value" where it is displayed
    """
    shoe_list = read_shoes_data()
    display = [["Country", "Code", "Product", "Cost", "Quantity", "Stock value"]]
    for _ in shoe_list:
        _.append(int(_[-1]) * int(_[-2]))
        display.append(_)
    print(tabulate(display, headers="firstrow", tablefmt="rounded_grid", numalign="left"))


def highest_qty():
    """A function that reads the shoes' data from "inventory.txt" and
    displays the item/items with the highest quantity in stock.
    """
    shoe_list = read_shoes_data()
    high_stock = []
    try:
        high = int(shoe_list[0][-1])
    except:
        print("The first item doesn't have a correct quantity")
    for index, line in enumerate(shoe_list):
        try:
            if int(line[-1]) > high:
                high = int(line[-1])
        except:
            print(f"The item at row {index + 2} does not contain a valid quantity.")
            to_remove = (index, _)
            to_remove_str = Shoe(_[0], _[1], _[2], _[3], _[4]).__str__()
            print(f"{to_remove_str} will be removed from calculation until rectified.")
            shoe_list.remove(_)
    for index, _ in enumerate(shoe_list):
        if int(_[-1]) == high:
            high_stock.append(index)
    display = []
    titles = ["ID", "Country", "Code", "Product", "Cost", "Quantity"]
    if len(high_stock) < 2:
        for index, row in enumerate(shoe_list):
            if int(row[-1]) == high:
                row.insert(0, str(index))
                display.append(row)
        print("""
                    ╔════════════════════════════╗
                              \033[4m\033[1m\033[91mSale Stock\033[0m
                    ╚════════════════════════════╝
""")
        print(tabulate(display, headers=titles, tablefmt="rounded_grid", numalign="left"))
        for row in shoe_list:
            try:
                if row[0].isdigit():
                    row.pop(0)
            except:
                pass
        try:
            shoe_list.insert(to_remove(0), to_remove(1))
        except:
            pass
    else:
        for index, row in enumerate(shoe_list):
            for i in high_stock:
                if index == i:
                    row.insert(0, str(index))
                    display.append(row)

        print("""
                    ╔════════════════════════════╗
                              \033[4m\033[1m\033[91mSale Stock\033[0m
                    ╚════════════════════════════╝
""")
        print(tabulate(display, headers=titles, tablefmt="rounded_grid", numalign="left"))
        for row in shoe_list:
            try:
                if row[0].isdigit():
                    row.pop(0)
            except:
                pass
        try:
            shoe_list.insert(to_remove(0), to_remove(1))
        except:
            pass


# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
user_choice = ''
while user_choice != "e":
    # displaying to the user the available options
    user_choice = input("""Chose from the options below:
1 - view inventory
2 - add shoe to inventory
3 - re-stock lowest
4 - search for a product by code
5 - check inventory value per item
6 - Sale list
e - exit
""")
    # checking which option was selected and 
    # calling the appropriate function or
    # if user selected "3" - will exit the program
    if user_choice == "1":
        view_all()
    elif user_choice == "2":
        capture_shoes()
    elif user_choice == "3":
        re_stock()
    elif user_choice == "4":
        search_shoe()
    elif user_choice == "5":
        value_per_item()
    elif user_choice == "6":
        highest_qty()
    elif user_choice == "e":
        print("Good Bye!")
        exit()
    else:
        print("Incorrect choice. Try again")
