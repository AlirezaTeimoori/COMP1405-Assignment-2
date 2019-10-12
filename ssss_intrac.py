
'''
    ---------------------------------------
    -- Created by:     Alireza Teimoori  --
    -- Created on:     Oct 01 2019       --
    -- Created for:    Assignment 2      --
    -- Course Code:    COMP1405          --
    -- Teacher Name:   Andrew Runka      --
    ---------------------------------------
    -- This program is written for Seb's --
    -- Seb's Savoury Sub Shoppe™, and is --
    -- used as an interactive automatic  --
    -- ordering system.                  --
    ---------------------------------------
    '''

# Define all the requred variables that will help us in 
data_list = [[1, "\"Meat\"-ball sub"            , 7.99],
             [2, "Cold-cut Club sub"            , 8.25],
             [3, "Philly's Cheese Mis-Steak sub", 9.55],
             [4, "Veggie Pile sub"              , 6.75]]
toplist = ["lettuce", "tomatoes", "onions", "peppers", "jalepenos", "pickles", "cucumbers", "olives", "guacamole"]
error = ("\n\t** Invalid input! Please try again! **\n")
class Food:

    def __init__(self, number:int, name:str, price:int, toppings:list = []):
        
        self.number   = number
        self.name     = name
        self.price    = price
        self.toppings = toppings
        self.hst      = 0.13
    
    def get_number(self):

        return self.number
    
    def get_name(self):

        return self.name

    def get_price(self):

        return self.price

    def get_topps(self):

        return self.toppings

    def get_topps_price(self):

        price = 0

        for i in self.toppings: price += 1.50 if i == "guacamole" else 0.00

        return price

    def get_subtotal(self):

        return (self.get_price() + self.get_topps_price())

    def get_tax(self):

        return (self.get_subtotal() * self.hst)
    
    def get_total(self):

        return (self.get_tax() + self.get_subtotal())

    def print(self):

        output = ""
        
        output+= f"*  The food number is:\t{self.number}\n"
        output+= f"*  The food name is:\t{self.name}\n"
        output+= f"*  The food price is:\t{self.price}\n"
        output+=  "*  The food tls is:\t"
        output+=  ' ,'.join(self.toppings) 
        return output

    def show_order(self):

        output = ""

        output+= "\n------------------------------------------\n--          --- Your Order ---          --\n--\t\t\t\t\t--\n"
        output+= f"-- Main:\t{self.name}\t\t--\n"\
            if 18 > len(self.name)\
            else f"-- Main:\t{self.name.split()[0]} {self.name.split()[1]}\t\t--\n"\
            +f"--\t\t{self.name.split()[2]} {self.name.split()[3]}\t\t--\n"\
            if len(self.name.split()) > 3\
            else f"-- Main:\t{self.name.split()[0]} {self.name.split()[1]}\t\t--\n"\
            +f"--\t\t{self.name.split()[2]}\t\n"
        output+= f"--\t\t\t\t\t--\n-- Toppings:\t" + '\t\t--\n--\t\t'.join(self.toppings) + "\t\t--\n"
        output+=  "------------------------------------------"

        return output

    def show_price(self):
        
        self.show_order()

        output = ""

        output+= "\n------------------------------------------\n--          --- Order Bill ---          --\n--\t\t\t\t\t--\n"
        output+= f"-- Subtotal:\t${self.get_subtotal():.2f}\t\t\t--\n"
        output+= f"-- Tax:\t\t${self.get_tax():.2f}\t\t\t--\n--\t\t\t\t\t--\n"
        output+= f"-- Total:\t${self.get_total():.2f}\t\t\t--\n------------------------------------------"

        return output

# Welcoming Message:
print("\n-----------------------------------------\n" +
      "--     Hello and Welcome to Sub's!     --\n" +
      "--     How are you doing today?!       --\n" +
      "-----------------------------------------\n")

# Asking user to order:
while True:
    while True: # Ask for a valid input until we get a number from the user
        try:
            main = int(input("Please choose from one of the following:\n\n" +
                             "1) \"Meat\"-ball sub - $7.99\n" +
                             "2) Cold-cut Club sub - $8.25\n" +
                             "3) Philly's Cheese Mis-Steak sub - $9.55\n" + \
                             "4) Veggie Pile sub - $6.75\n\n\t> My choice is: "))
            break
        except ValueError:
            print("\n\t** Invalid Value! Please enter a number only! **\n")
    
    # If we have a valid number
    if main in range(1,5):

        # Create a new food using the data that we already have and he data we got from the user
        food = Food(data_list[ main - 1 ][0],\
               data_list[ main - 1 ][1],\
               data_list[ main - 1 ][2])

        # Ask the user to enter the toppings they want
        toppings = input("Please enter any toppings you want to add\n\t> ")
        while True: # Do this until we have a valid input

            if toppings != "done":
                food.toppings.append(toppings) if toppings in toplist else print(error) 
            else: break

            toppings = input("\t> ")
        
        for i in range(len(food.toppings)): food.toppings[i] += "  " if len(food.toppings[i]) < 7 else ""

        print(food.show_order())

        # Get confirmation from the user
        confirmation = input("Is this correct? ( y / n )")
        while confirmation != "y" and confirmation != "n": confirmation = input("Is this correct? ( y / n )")
        if confirmation == "n": print("Please Try Again!"); exit()
        
        # Print the calculations prices
        print (food.show_price())

        # Jump out of the loop
        break
    else:
        print(error)
    




