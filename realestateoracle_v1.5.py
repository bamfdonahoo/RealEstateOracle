### RealEstateOracle Version 1.0
## Written in Python 3.9.5
# Blake Donahoo 7-15-2021

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pyodbc

startup_logo =""" 
||\   ||////    ^    ||       ||////   ///// ////////  ^  //////// ||////
|| \  ||       / \   ||       ||      //        ||    / \    ||    ||
||_// ||////  /__ \  ||       ||////  //////    ||   /__ \   ||    ||////
|| \  ||     //    \ ||       ||          //    ||  //    \  ||    ||
||  \ ||//////      \||////   ||//// //////     || //      \ ||    ||////

       
    ///////  ||\       ^     /////// ||      ||//// 
  ///    /// || \     / \   ///      ||      ||
 ///    ///  ||_//   /__ \  ///      ||      ||////
 //    ///   || \   //    \ ///      ||      ||
 ///////     ||  \ //      \ /////// ||///// ||////
-----------------------------------------------------
A primitive data science library for real estate
Creator: Blake Donahoo
Published: 07-15-2021
Version: 1.5
Updated on: 07-18-2021

Data Source: https://www.zillow.com/research/data/

Data & Functionality contained: 
 - Home values in every state since 1996
 - Calculated value changes over time for every state since 1996
 - Forecasting Metrics and predictive algorithms all the way down the the City level
 - Rental Values in every state since 2014
 
Coming in Version 2.0:
  - Mean/Median/Mode, Standard Deviation for every slice of information
  - Python generated visualizations like ScatterPlots, Histograms & BarGraphs
  - "Oracle Prediction" using Proprietary prediction algorithms

"""
# Options and functionality yet to be added to startup menu::: 
#  - Mean/Median/Mode, Standard Deviation for every slice of information
#  - Python generated visualizations like ScatterPlots, Histograms & BarGraphs
#  - "Oracle Prediction" using Proprietary prediction algorithms

# Connection string through pyodbc library to RealEstate Database
cnxn_str = (
    r'DRIVER=SQL Server;'
    r'SERVER=(local)\MSSQLSERVER01;'
    r'Trusted_Connection=yes;'
    r'Database=RealEstate'
)
cnxn = pyodbc.connect(cnxn_str)
print(startup_logo)
# Input number labels:::
input1_op1 = 'Avg Sales price change over time'
input1_op2 = 'Avg Sales price prediction 2022'
input1_op3 = 'Custom SQL Query'
input1_op4 = 'Avg Rental Rates change over time'
input1_op5 = 'Oracle Prediction'
input1_op6 = 'Scatterplots'

def reset():
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
				print("You killed me. (x__x) Restart me to reconnect to database.")
				cnxn.close()

def oraclePredict():
	print('You chose {} \n\n'.format(input1_op5))
	oracleInput_market = input("Type \"rental\" or \"sales\" to pick a market to calculate a prediction for \n\n")
	oracleInput_state = input("Type the two letter abbreviation of the state you want a prediction for (not case sensitive) \n\n")
	oracleInput_date = input("Type the numerical date you want a prediction for in the format: mm-dd-yyyy (with dashes) \n\n")
	print('You chose to predict the {} market in the state of {} around the time of {} \n\n'.format(oracleInput_market,oracleInput_state,oracleInput_date)) 
	mainmenu()

def scatterPlots():
	print('You chose {} \n\n'.format(input1_op6))
	scatinput_market = input("Type \"rental\" or \"sales\" to pick a market to calculate a scatter plot for \n\n")
	scatinput_state = input("Type the two letter abbreviation of the state you want a scatter plot for (not case sensitive) \n\n")
	mainmenu()

def sqlQuery():	
	print('You chose {} \n\n'.format(input1_op3))
	input_3 = input("""
	Type your SQL query from any of the Tables and corresponding schemas shown below \n\n 
	Use normal SQL syntax \n\n 
	Table: AllThreeUnPivSalesPriceMo \n 
	Schema: StateName | State | Date | Bottom Tier | Middle Tier | Top Tier \n\n 
	Table: ForecastSalesAvg2022 \n 
	Schema: Lstate | BottomTierProjection2022 | MiddleTierProjection2022 | TopTierProjection2022 \n\n 
	Table: Window_TMB \n 
	Schema: StateName | Lstate | Date | TopValue | TopPriorMonth | TopDiffPrevMonth | MiddleValue | MidPriorMonth \n| MidDiffPrevMonth | BottomValue | BottomPriorMonth | BottomDiffPrevMonth \n\n
	Table: RentalRatesUnPiv \n
	Schema: Lstate | CityName | Value | Date \n\n
	Table: RentalRates_Window \n
	Schema: Lstate | CityName | Date | Value | PriorMonth | DiffPriorMonth \n\n
	""")
	for i in input_3:
		try:
			print(pd.read_sql("{}".format(input_3),cnxn))
			mainmenu()
		except ProblemExecutingQuery:
			print("Error executing query...Check your syntax and try again \n\n")
			input_3 = input("Type your SQL query from any of the Tables and corresponding schemas shown below \n\n Use normal SQL syntax \n\n Table: AllThreeUnPivSalesPriceMo \n Schema: StateName | State | Date | Bottom Tier | Middle Tier | Top Tier \n\n Table: ForecastSalesAvg2022 \n Schema: Lstate | BottomTierProjection2022 | MiddleTierProjection2022 | TopTierProjection2022 \n\n Table: Window_TMB \n Schema: StateName | Lstate | Date | TopValue | TopPriorMonth | TopDiffPrevMonth | MiddleValue | MidPriorMonth | \n MidDiffPrevMonth | BottomValue | BottomPriorMonth | BottomDiffPrevMonth \n\n")
			for i in input_3:
				try:
					print(pd.read_sql("{}".format(input_3),cnxn))
					mainmenu()
				except ProblemExecutingQuery:
					print("Error executing query...Check your syntax and try again \n\n")
					mainmenu()		
		
# Programming for user input data navigation prompt:
def mainmenu():
	input_1 = input("""What would you like to know? \n\n
	Type the number of the option that best fits your question and press enter.\n\n 
	1 = Avg Sales price change over time  2 = Avg Sales price prediction 2022  3 = Custom SQL Query \n
	4 = Avg Rental Rates change over time  5 = Oracle Prediction  6 = Scatterplots
	""")
	if input_1 == "3":
		sqlQuery()
	elif input_1 == "5":
		oraclePredict()
	elif input_1 == "6":
		scatterPlots()
	input_2 = input("""
	What state would you like to know about? \n\n 
	Type the two letter state abbreviation for state isolated metrics \n\n 
	or \"all\" for national metrics.\n\n 
	example: tx (not case sensitive) \n\n""")
	if input_1 == "1" and input_2.lower() == "all":
		print('You chose {} with a filter of {}\n\n'.format(input1_op1, input_2.upper()))
		print( (pd.read_sql("SELECT * FROM Window_TMB", cnxn)) )
		reset()
	elif input_1 == "1":
		print('You chose {} with a filter of {}\n\n'.format(input1_op1, input_2.upper()))
		print( (pd.read_sql("SELECT * FROM Window_TMB WHERE Lstate LIKE \'{}\'".format(input_2.upper()), cnxn)) )
		reset()
	elif input_1 == "2" and input_2.lower() == "all":
		print('You chose {} with a filter of {}\n\n'.format(input1_op2, input_2.upper()))
		print( (pd.read_sql("SELECT * FROM ForecastSalesAvg2022", cnxn)) )
		reset()
	elif input_1 == "2":
		print('You chose {} with a filter of {}\n\n'.format(input1_op2, input_2.upper()))
		print( (pd.read_sql("SELECT * FROM ForecastSalesAvg2022 WHERE Lstate LIKE \'{}\'".format(input_2.upper()), cnxn)) )
		reset()
	elif input_1 == "4" and input_2.lower() == "all":
		print('You chose {} with a filter of {}\n\n'.format(input1_op4, input_2.upper()))
		print( (pd.read_sql("SELECT * FROM RentalRates_Window", cnxn)) )
		reset()  
	elif input_1 == "4":
		print('You chose {} with a filter of {}\n\n'.format(input1_op4, input_2.upper()))
		print( (pd.read_sql("SELECT * FROM RentalRates_Window WHERE Lstate LIKE \'{}\'".format(input_2.upper()), cnxn)) )
		reset()                                       
mainmenu()  