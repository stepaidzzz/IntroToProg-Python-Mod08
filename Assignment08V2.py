# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# SYong,9.7.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    # TODO: Add Code to the Product class
    # -- Constructor --
    # SY: Not sure why we need constructor. Thought we could just dive right into getter and setter?
    # SY: Maybe it is the "Attributes" that are not necessary?
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    # -- Properties --
    @property
    def product_name(self):  # getter or accessor
        return str(self.__product_name_str).title() #this command is "returning" something.

    @product_name.setter
    def product_name(self, value):
        self.__product_name_str = value #this is "setting" a value.

    @property
    def product_price(self):
        return float(self.__product_price_float)

    @product_price.setter
    def product_price(self, value):
        self.__product_price_float = value

    # -- Methods --
    def __str__(self):
        return self.product_name + " " + str(self.product_price)
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):


        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        SYong,9.7.2022,Modified code to complete assignment 8
    """

    # TODO: Add Code to process data from a file
    @staticmethod
    def write_data_to_file(file_name, lstOfProductObjects):
        """ Writes data from a list of dictionary rows to a File

        :param strFileName: (string) with name of file:
        :param lstOfProductObjects: (list) you want filled with file data:
        :return: (list) of rows
        """
        file_obj = open(file_name, "w")
        for row in lstOfProductObjects:
            file_obj.write(row.__str__() + "\n")
        file_obj.close()
        return lstOfProductObjects


    # TODO: Add Code to process data to a file
    @staticmethod
    def read_data_from_file(file_name, lstOfProductObjects):
        """ Reads data from a file into a list of dictionary rows

        :param strFileName: (string) with name of file:
        :param lstOfProductObjects: (list) you want filled with file data:
        :return: (list) of rows
        """
        #list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            product, price = line.split(",") #SY: Not quite sure about the rationale behind this line.
            row = Product(data[0], data[1]) #SY: Not quite sure about the syntax for this line.
            lstOfProductObjects.append(row)
        file.close()
        return lstOfProductObjects
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring

    # TODO: Add code to show menu to user
    @staticmethod
    def output_menu_tasks():
        print('''
                Menu of Options
                1) Show current data
                2) Add Data to File        
                3) Save and Exit Program
                ''')

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def output_current_tasks_in_list(lstOfProductObjects):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("** The current products and prices are: **")
        for row in lstOfProductObjects:
            print(row.product_name + " " + str(row.product_price))
        print("******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_product_and_price():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        # TODO: Add Code Here!
        product = str(input("Please input a product: "))
        price = input("Please indicate price: ")
        lstProduct = Product(product_name = product, product_price = price)
        return lstProduct
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
while (True):
    IO.output_menu_tasks()

# Get user's menu option choice
    try:
        choice_str = IO.input_menu_choice()

        # Show user current data in the list of product objects
        if choice_str.strip() == '1':  # Add a new Task
            IO.output_current_tasks_in_list(lstOfProductObjects)
            continue  # to show the menu

        # Let user add data to the list of product objects
        if choice_str == '2':
            lstOfProductObjects.append(IO.input_new_product_and_price())
            print("Data Saved!")
            continue  # to show the menu

        # let user save current data to file and exit program
        if choice_str == '3':
            FileProcessor.write_data_to_file(strFileName, lstOfProductObjects)
            print("Goodbye!")
            break  # by exiting loop

        elif choice_str != "1" or "2" or "3":
            raise Exception("Please limit your input to 1, 2 or 3!")
    except Exception as e:
        print("There was a non-specific error!")
        print(e)
# Main Body of Script  ---------------------------------------------------- #
