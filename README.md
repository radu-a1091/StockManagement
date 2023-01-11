# Simple Stock Management Tool

## Intro
The tool was built using OOP allows user to read stock data, create new stock entry, view all products information, re-order low stock products, search specific SKU and get its details (i.e. product name, cost, quantity, country where it is sold), check stock value and check overstocked item.

## Installation
Download the inventory.py and inventory.txt to your local machine (preferably in a new empty folder) and open the folder where they've been downloaded in your IDE:

    PyCharm: File -> Open

    VS Code: File -> Open Folder

Before running the program, install tabulate on your machine. Instructions here:
https://pypi.org/project/tabulate/

_Note_: It is important that both, the .py and .txt files, are saved into the __same folder__.

## inventory.py
The file with the magic.

### Classes and methods
The program uses one class - Shoe - which has 3 methods:
* __get_cost()__ - pulls the cost price for the Shoe object referenced
* __get_quantity__ - pulls the quantity in stock for the shoe object referenced
* __\_\_str\_\___ - converts the Shoe object's attributes into a string (used to add a new Shoe object to inventory.txt)

### Functions
* __capture_shoes()__ - captures the shoes details from user inputs, does error checking on the user inputs, creates a new shoe object and adds the object to inventory.txt
* __view_all()__ - displays all the products and their information 
* __update_inventory(modified_list)__ - updates the inventory.txt database. Takes one argument: modified_list (the new and modified list of objects)
* __re_stock()__ - allows the user to re-stock the lowest quantity product to a desired quantity; if there are more products with the same low quantity, the user is asked if should 1 or all be updated; if there are any products with missing/incorrect quantity information in inventory.txt, these will be temporarily removed from calculation but added to the same position once the calculation has been done.
* __search_shoe()__ - requests the user to input a desired code and displays the product details linked to the code. Displays an error message if the code is not linked to any product
* __value_per_item()__ - displays all the products, adds an extra column "Stock value" where the value per product it is calculated and displayed
* __highest_qty()__ - reads the shoes' data from "inventory.txt" and displays the item/items with the highest quantity in stock

### User menu
```
1 - view inventory
2 - add shoe to inventory
3 - re-stock lowest
4 - search for a product by code
5 - check inventory value per item
6 - Sale list
e - exit
```

## inventory.txt
Feel free to add/alter/remove information on this text file once it's been downloaded on your machine.

The column headers are in the first row, separated by comma:

__Country__ - the country where the product is sold

__Code__ = the SKU of the product

__Product__ - product name

__Cost__ - the cost of the product

__Quantity__ - the quantity in stock

## Screenshots
![add shoe to inventory](https://github.com/radu-a1091/finalCapstone/blob/156a12c03c7d9bb3e78c59c8781dce3ddb14eccc/add.jpg "add")

![inventory value](https://github.com/radu-a1091/finalCapstone/blob/156a12c03c7d9bb3e78c59c8781dce3ddb14eccc/inv_value.jpg "inventory value")

![current inventory](https://github.com/radu-a1091/finalCapstone/blob/156a12c03c7d9bb3e78c59c8781dce3ddb14eccc/view_all.jpg "current inventory")

![search by code](https://github.com/radu-a1091/finalCapstone/blob/156a12c03c7d9bb3e78c59c8781dce3ddb14eccc/search.jpg "search by code")

![low quantity stock - 1 item](https://github.com/radu-a1091/finalCapstone/blob/156a12c03c7d9bb3e78c59c8781dce3ddb14eccc/restock_low.jpg "low quantity stock1")

![low quantity stock - multiple](https://github.com/radu-a1091/finalCapstone/blob/156a12c03c7d9bb3e78c59c8781dce3ddb14eccc/double_low_stock.jpg "low quantity2")

![overstock](https://github.com/radu-a1091/finalCapstone/blob/156a12c03c7d9bb3e78c59c8781dce3ddb14eccc/sale.jpg "overstock")

## To-do list
* [ ] - change the class 'Shoe' to adapt any product type

* [ ] - update README.md to reflect class change

* [ ] - add option to do inventory adjustment and record such adjustments

* [ ] - build GUI (Tkinter / Kivy / PySimpleGUI - TBC)  




