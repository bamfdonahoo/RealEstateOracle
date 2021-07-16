### RealEstateOracle Version 1.0
## Written in Python 3.9.5
# Blake Donahoo 7-15-2021

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pyodbc

cnxn_str = (
    r'DRIVER=SQL Server;'
    r'SERVER=(local)\MSSQLSERVER01;'
    r'Trusted_Connection=yes;'
    r'Database=RealEstate'
)
cnxn = pyodbc.connect(cnxn_str)
startup_logo =""" 
||\   ||////    ^    ||       ||////   ///// ////////  ^  //////// ||////
|| \  ||       / \   ||       ||      //        ||    / \    ||    ||
||_// ||////  /__ \  ||       ||////  //////    ||   /__ \   ||    ||////
|| \  ||     //    \ ||       ||          //    ||  //    \  ||    ||
||  \ ||//////      \||////   ||//// //////     || //      \ ||    ||////

       
    ///////  ||\       ^     /////// ||      ||//// 
  ///    /// || \     / \   ///      ||      ||
 ///    ///  ||_//   /__ \  ///      ||      ||////
 ///   ///   || \   //    \ ///      ||      ||
 ///////     ||  \ //      \ /////// ||///// ||////
-----------------------------------------------------
A primitive data science library for real estate
Creator: Blake Donahoo
Published: 07-15-2021
Version: 1.0

"""
print(startup_logo)
def mainmenu():
    input_1 = input("What would you like to know? Type the number of the option that best fits your question and press enter.\n\n 1 = Avg Sales price change over time  2 = Avg Sales price prediction 2022 \n\n")
    input_2 = input("What state would you like to know about? \n\n Type the two letter state abbreviation for state isolated metrics \n\n or \"all\" for national metrics.\n\n example: tx (not case sensitive) \n\n")
    if input_1 == "1" and input_2.lower() == "all":
        print( (pd.read_sql("SELECT * FROM Window_TMB", cnxn)) )
        input_0 = input("Type the number 0 and press enter to return to the main menu \n")
        if input_0 == "0":
            mainmenu()
        elif input_0 != "0":
            input("Invalid Input Error: Type the number 0 and press enter to return to the main menu \n")
            if input_0 == "0":
                mainmenu()
            elif input_0 != "0": 
                input("You're killing me. Type the number 0 and press enter to return to the main menu \n")
                if input_0 == "0":
                    mainmenu()
                elif input_0 != "0":
                    print("You killed me. (x__x) Just restart me already then.")
    elif input_1 == "1":
        print( (pd.read_sql("SELECT * FROM Window_TMB WHERE Lstate LIKE \'{}\'".format(input_2.upper()), cnxn)) )
        input_0 = input("Type the number 0 and press enter to return to the main menu \n")
        if input_0 == "0":
            mainmenu()   
        elif input_0 != "0":
            input("Invalid Input Error: Type the number 0 and press enter to return to the main menu \n")   
            if input_0 == "0":
                mainmenu()
            elif input_0 != "0": 
                input("You're killing me. Type the number 0 and press enter to return to the main menu \n")
                if input_0 == "0":
                    mainmenu()
                elif input_0 != "0":
                    print("You killed me. (x__x) Just restart me already then.")
    elif input_1 == "2" and input_2.lower() == "all":
        print( (pd.read_sql("SELECT * FROM ForecastSalesAvg2022", cnxn)) )
        input_0 = input("Type the number 0 and press enter to return to the main menu \n")
        if input_0 == "0":
            mainmenu()
        elif input_0 != "0":
            input("Invalid Input Error: Type the number 0 and press enter to return to the main menu \n")
            if input_0 == "0":
                mainmenu()
            elif input_0 != "0": 
                input("You're killing me. Type the number 0 and press enter to return to the main menu \n")
                if input_0 == "0":
                    mainmenu()
                elif input_0 != "0":
                    print("You killed me. (x__x) Just restart me already then.")
    elif input_1 == "2":
        print( (pd.read_sql("SELECT * FROM ForecastSalesAvg2022 WHERE Lstate LIKE \'{}\'".format(input_2.upper()), cnxn)) )
        input_0 = input("Type the number 0 and press enter to return to the main menu \n")
        if input_0 == "0":
            mainmenu()   
        elif input_0 != "0":
            input("Invalid Input Error: Type the number 0 and press enter to return to the main menu \n")   
            if input_0 == "0":
                mainmenu()
            elif input_0 != "0": 
                input("You're killing me. Type the number 0 and press enter to return to the main menu \n")
                if input_0 == "0":
                    mainmenu()
                elif input_0 != "0":
                    print("You killed me. (x__x) Just restart me already then.")					            
mainmenu()