### RealEstateOracle Version 1.7
## Written in Python 3.9.5
# Blake Donahoo 7-15-2021

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pyodbc
import joblib
import re

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
Version: 2
Updated on: 08-23-2021

Data Source: https://www.zillow.com/research/data/

Data & Functionality contained: 
 - Home values in every state since 1996
 - Forecasting Metrics and predictive algorithms for future market prices in every state
 - Rental Values in every state since 2014
 
Coming in Version 2.5:
  - Python generated visualizations like ScatterPlots, Histograms & BarGraphs

"""
# Options and functionality yet to be added to startup menu::: 
#  - Mean/Median/Mode, Standard Deviation for every slice of information
#  - Python generated visualizations like ScatterPlots, Histograms & BarGraphs
#  - "Oracle Prediction" using Proprietary prediction algorithms
rental = pd.read_csv('realestate_data/Rental_FullEDA_fillNaN.csv', parse_dates = ['Date'])
sales = pd.read_csv('realestate_data/Combined_RealEstateData_Cleaned.csv', parse_dates = ['Date'])
predict_sales = joblib.load('knr_sales.mdl')
predict_rental = joblib.load('knr_rental.mdl')
print(startup_logo)
# Input number labels:::
input1_op1 = 'Avg Sales price table data'
input1_op2 = 'Avg Rental Rates table data'
input1_op3 = 'Oracle Prediction'

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
    print('You chose {} \n\n'.format(input1_op3))
    
    oracleInput_market = input("Type \"rental\" or \"sales\" to pick a market to calculate a prediction for \n\n")
    oracleInput_state = input("Type the two letter abbreviation of the state you want a prediction for (not case sensitive) \n\n")
    oracleInput_date = input("Type the numerical date you want a prediction for in the format: mm-dd-yyyy (with dashes) \n\n")
    print('You chose to predict the {} market in the state of {} around the time of {} \n\n'\
          .format(oracleInput_market,oracleInput_state,oracleInput_date)) 
    
    if oracleInput_state:
        if oracleInput_state.lower() == 'al':
            oracleInput_state = 1 
        elif oracleInput_state.lower() == 'ak':
            oracleInput_state = 2 
        elif oracleInput_state.lower() == 'ar':
            oracleInput_state = 3 
        elif oracleInput_state.lower() == 'az':
            oracleInput_state = 4 
        elif oracleInput_state.lower() == 'ca':
            oracleInput_state = 5 
        elif oracleInput_state.lower() == 'co':
            oracleInput_state = 6 
        elif oracleInput_state.lower() == 'ct':
            oracleInput_state = 7 
        elif oracleInput_state.lower() == 'de':
            oracleInput_state = 8 
        elif oracleInput_state.lower() == 'fl':
            oracleInput_state = 9 
        elif oracleInput_state.lower() == 'ga':
            oracleInput_state = 10 
        elif oracleInput_state.lower() == 'hi':
            oracleInput_state = 11 
        elif oracleInput_state.lower() == 'ia':
            oracleInput_state = 12 
        elif oracleInput_state.lower() == 'id':
            oracleInput_state = 13 
        elif oracleInput_state.lower() == 'il':
            oracleInput_state = 14 
        elif oracleInput_state.lower() == 'in':
            oracleInput_state = 15 
        elif oracleInput_state.lower() == 'ks':
            oracleInput_state = 16 
        elif oracleInput_state.lower() == 'ky':
            oracleInput_state = 17 
        elif oracleInput_state.lower() == 'la':
            oracleInput_state = 18 
        elif oracleInput_state.lower() == 'ma':
            oracleInput_state = 19 
        elif oracleInput_state.lower() == 'md':
            oracleInput_state = 20 
        elif oracleInput_state.lower() == 'me':
            oracleInput_state = 21 
        elif oracleInput_state.lower() == 'mi':
            oracleInput_state = 22 
        elif oracleInput_state.lower() == 'mn':
            oracleInput_state = 23 
        elif oracleInput_state.lower() == 'mo':
            oracleInput_state = 24 
        elif oracleInput_state.lower() == 'ms':
            oracleInput_state = 25 
        elif oracleInput_state.lower() == 'mt':
            oracleInput_state = 26 
        elif oracleInput_state.lower() == 'nc':
            oracleInput_state = 27 
        elif oracleInput_state.lower() == 'nd':
            oracleInput_state = 28 
        elif oracleInput_state.lower() == 'ne':
            oracleInput_state = 29 
        elif oracleInput_state.lower() == 'nh':
            oracleInput_state = 30 
        elif oracleInput_state.lower() == 'nj':
            oracleInput_state = 31 
        elif oracleInput_state.lower() == 'nm':
            oracleInput_state = 32 
        elif oracleInput_state.lower() == 'nv':
            oracleInput_state = 33 
        elif oracleInput_state.lower() == 'ny':
            oracleInput_state = 34 
        elif oracleInput_state.lower() == 'oh':
            oracleInput_state = 35 
        elif oracleInput_state.lower() == 'ok':
            oracleInput_state = 36 
        elif oracleInput_state.lower() == 'or':
            oracleInput_state = 37 
        elif oracleInput_state.lower() == 'pa':
            oracleInput_state = 38 
        elif oracleInput_state.lower() == 'ri':
            oracleInput_state = 39 
        elif oracleInput_state.lower() == 'sc':
            oracleInput_state = 40 
        elif oracleInput_state.lower() == 'sd':
            oracleInput_state = 41 
        elif oracleInput_state.lower() == 'tn':
            oracleInput_state = 42 
        elif oracleInput_state.lower() == 'tx':
            oracleInput_state = 43 
        elif oracleInput_state.lower() == 'ut':
            oracleInput_state = 44 
        elif oracleInput_state.lower() == 'vt':
            oracleInput_state = 45 
        elif oracleInput_state.lower() == 'va':
            oracleInput_state = 46 
        elif oracleInput_state.lower() == 'wa':
            oracleInput_state = 47 
        elif oracleInput_state.lower() == 'wi':
            oracleInput_state = 48 
        elif oracleInput_state.lower() == 'wv':
            oracleInput_state = 49 
        elif oracleInput_state.lower() == 'wy':
            oracleInput_state = 50 
        
        
    if oracleInput_date:
        oracleInput_date = re.sub('\d+\-\d+\-', '',oracleInput_date)
    
    if oracleInput_market == "sales":
        test_set = np.array(oracleInput_state), np.array(oracleInput_date)
        s_prediction = predict_sales.predict([test_set])
        print(s_prediction)
        print("\n\n")
        mainmenu()
    elif oracleInput_market == "rental":
        test_set = np.array(oracleInput_state), np.array(oracleInput_date)
        r_prediction = predict_rental.predict([test_set])
        print(r_prediction)
        print("\n\n")
        mainmenu()

def scatterPlots():
### Still under construction
# function for scatterplots
	print('You chose {} \n\n'.format(input1_op6))
	scatinput_market = input("Type \"rental\" or \"sales\" to pick a market to calculate a scatter plot for \n\n")
	scatinput_state = input("Type the two letter abbreviation of the state you want a scatter plot for or \"all\" for national metrics (not case sensitive) \n\n")
	scatinput_chart = input("Choose an option:\n\n 1 = Change over time  2 = Price difference month-over-month \n\n")
	print('You chose to generate a scatterplot for the {} market in the region of {} \n\n'.format(scatinput_market,scatinput_state))
    ### Pandas dataframe definitions for scatterplots
    #Sales price Difference over time
	df_WindowTMB_all = pd.read_sql("SELECT * FROM Window_TMB", cnxn)
	df_WindowTMB_state = pd.read_sql("SELECT * FROM Window_TMB WHERE Lstate LIKE \'{}\'".format(scatinput_state.upper()), cnxn)
    # Sales price Forecast 2022
	df_ForecastSalesAvg2022_all = pd.read_sql("SELECT * FROM ForecastSalesAvg2022", cnxn)
	df_ForecastSalesAvg2022_state = pd.read_sql("SELECT * FROM ForecastSalesAvg2022 WHERE Lstate LIKE \'{}\'".format(scatinput_state.upper()), cnxn)
    # Sales price Change over time
	df_AllThreeUnPivSalesPriceMo_all = pd.read_sql("SELECT * FROM AllThreeUnPivSalesPriceMo", cnxn)
	df_AllThreeUnPivSalesPriceMo_state = pd.read_sql("SELECT * FROM AllThreeUnPivSalesPriceMo WHERE Lstate LIKE \'{}\'".format(scatinput_state.upper()), cnxn)
    # Rental rates Difference over time
	df_RentalRates_Window_all = pd.read_sql("SELECT * FROM RentalRates_Window", cnxn)
	df_RentalRates_Window_state = pd.read_sql("SELECT * FROM RentalRates_Window WHERE Lstate LIKE \'{}\'".format(scatinput_state.upper()), cnxn)
    # Rental rates change over time 
	df_RentalRatesUnPiv_all = pd.read_sql("SELECT * FROM RentalRatesUnPiv", cnxn)
	df_RentalRatesUnPiv_state = pd.read_sql("SELECT * FROM RentalRatesUnPiv WHERE Lstate LIKE \'{}\'".format(scatinput_state.upper()), cnxn)
    ##########################################################################################
	if scatinput_market.lower() == "sales" and scatinput_state.lower() == "all" and scatinput_chart == "1":
		Tier_input = input("Which price tier do you want information for? \n\n 1 = Bottom Tier  2 = Mid Tier  3 = Top Tier \n\n")
		spcdate = np.array(df_AllThreeUnPivSalesPriceMo_all.Date)
        # *** SPC / "ALL" OPTION
		spcvalue1 = np.array(df_AllThreeUnPivSalesPriceMo_all.BottomTier)
		spcvalue2 = np.array(df_AllThreeUnPivSalesPriceMo_all.MiddleTier)
		spcvalue3 = np.array(df_AllThreeUnPivSalesPriceMo_all.TopTier)
		spcstate1 = np.array(df_AllThreeUnPivSalesPriceMo_all.Lstate)
		if Tier_input == "1":
            # Bottom Tier
			plt.figure(figsize=(10,6))
			plt.title("Bottom Tier Sales Price Change Over Time",fontsize=20)
			plt.xlabel("{}".format(scatinput_state.upper()),fontsize=16)
			plt.ylabel("Value",fontsize=16)
			plt.grid (False)
			plt.ylim(100000,300000)
			plt.xticks([i*6 for i in range(10)],fontsize=15)
			plt.yticks(fontsize=15)
			plt.scatter(x=spcdate , y=spcvalue1 , c='red' , s=20 , edgecolors='m')
            #plt.text(x=30,y=45,s="Weights are more or less similar \nafter 18-20 years of age",fontsize=15)
			plt.vlines(x=40,ymin=0,ymax=100,linestyles='dashed',color='k',lw=3)
			plt.legend(['Home Values'],loc=2,fontsize=12)
			plt.show()
		elif Tier_input == "2":
            # Mid Tier
			plt.figure(figsize=(10,6))
			plt.title("Mid Tier Sales Price Change Over Time",fontsize=20)
			plt.xlabel("{}".format(scatinput_state.upper()),fontsize=16)
			plt.ylabel("Value",fontsize=16)
			plt.grid (False)
			plt.ylim(100000,300000)
			plt.xticks([i*6 for i in range(10)],fontsize=15)
			plt.yticks(fontsize=15)
			plt.scatter(x=spcdate , y=spcvalue2 , c='red' , s=20 , edgecolors='m')
            #plt.text(x=30,y=45,s="Weights are more or less similar \nafter 18-20 years of age",fontsize=15)
			plt.vlines(x=40,ymin=0,ymax=100,linestyles='dashed',color='k',lw=3)
			plt.legend(['Home Values'],loc=2,fontsize=12)
			plt.show()
		elif Tier_input == "3":
            # Tier Tier
			plt.figure(figsize=(10,6))
			plt.title("Top Tier Sales Price Change Over Time",fontsize=20)
			plt.xlabel("{}".format(scatinput_state.upper()),fontsize=16)
			plt.ylabel("Value",fontsize=16)
			plt.grid (False)
			plt.ylim(100000,300000)
			plt.xticks([i*6 for i in range(10)],fontsize=15)
			plt.yticks(fontsize=15)
			plt.scatter(x=spcdate , y=spcvalue3 , c='red' , s=20 , edgecolors='m')
            #plt.text(x=30,y=45,s="Weights are more or less similar \nafter 18-20 years of age",fontsize=15)
			plt.vlines(x=40,ymin=0,ymax=100,linestyles='dashed',color='k',lw=3)
			plt.legend(['Home Values'],loc=2,fontsize=12)
			plt.show()
	elif scatinput_market.lower() == "sales" and scatinput_state.lower() != "all" and scatinput_chart == "1":
		Tier_input = input("Which price tier do you want information for? \n\n 1 = Bottom Tier  2 = Mid Tier  3 = Top Tier \n\n")
        # state and date definitions for Change over Time (AllThreeUnPivSalesPriceMo) Scatterplot
		spcdate = np.array(df_AllThreeUnPivSalesPriceMo_all.Date)
        # *** SPC / "STATE" OPTION
		spcvalue4 = np.array(df_AllThreeUnPivSalesPriceMo_state.BottomTier)
		spcvalue5 = np.array(df_AllThreeUnPivSalesPriceMo_state.MiddleTier)
		spcvalue6 = np.array(df_AllThreeUnPivSalesPriceMo_state.TopTier)
		spcstate2 = np.array(df_AllThreeUnPivSalesPriceMo_state.Lstate)
		if Tier_input == "1":
            # Bottom Tier
			plt.figure(figsize=(10,6))
			plt.title("Bottom Tier Sales Price Change Over Time",fontsize=20)
			plt.xlabel("{}".format(scatinput_state.upper()),fontsize=16)
			plt.ylabel("Value",fontsize=16)
			plt.grid (False)
			plt.ylim(100000,300000)
			plt.xticks([i*6 for i in range(10)],fontsize=15)
			plt.yticks(fontsize=15)
			plt.scatter(x=spcdate , y=spcvalue4 , c='red' , s=20 , edgecolors='m')
            #plt.text(x=30,y=45,s="Weights are more or less similar \nafter 18-20 years of age",fontsize=15)
			plt.vlines(x=40,ymin=0,ymax=100,linestyles='dashed',color='k',lw=3)
			plt.legend(['Home Values'],loc=2,fontsize=12)
			plt.show()
		elif Tier_input == "2":
            # Mid Tier
			plt.figure(figsize=(10,6))
			plt.title("Mid Tier Sales Price Change Over Time",fontsize=20)
			plt.xlabel("{}".format(scatinput_state.upper()),fontsize=16)
			plt.ylabel("Value",fontsize=16)
			plt.grid (False)
			plt.ylim(100000,300000)
			plt.xticks([i*6 for i in range(10)],fontsize=15)
			plt.yticks(fontsize=15)
			plt.scatter(x=spcdate , y=spcvalue5 , c='red' , s=20 , edgecolors='m')
            #plt.text(x=30,y=45,s="Weights are more or less similar \nafter 18-20 years of age",fontsize=15)
			plt.vlines(x=40,ymin=0,ymax=100,linestyles='dashed',color='k',lw=3)
			plt.legend(['Home Values'],loc=2,fontsize=12)
			plt.show()
		elif Tier_input == "3":
            # Tier Tier
			plt.figure(figsize=(10,6))
			plt.title("Top Tier Sales Price Change Over Time",fontsize=20)
			plt.xlabel("{}".format(scatinput_state.upper()),fontsize=16)
			plt.ylabel("Value",fontsize=16)
			plt.grid (False)
			plt.ylim(100000,300000)
			plt.xticks([i*6 for i in range(10)],fontsize=15)
			plt.yticks(fontsize=15)
			plt.scatter(x=spcdate , y=spcvalue6 , c='red' , s=20 , edgecolors='m')
            #plt.text(x=30,y=45,s="Weights are more or less similar \nafter 18-20 years of age",fontsize=15)
			plt.vlines(x=40,ymin=0,ymax=100,linestyles='dashed',color='k',lw=3)
			plt.legend(['Home Values'],loc=2,fontsize=12)
			plt.show()
        ############################################################################
	elif scatinput_market.lower() == "sales" and scatinput_state.lower() == "all" and scatinput_chart == "2":
		Tier_input = input("Which price tier do you want information for? \n\n 1 = Bottom Tier  2 = Mid Tier  3 = Top Tier \n\n")
		# state and date definitions for Difference Month-over-Month (WindowTMB) Scatterplot
		spddate = np.array(df_WindowTMB_all.Date)
		# *** "ALL" OPTION
		spdvalue1 = np.array(df_WindowTMB_all.BottomDiffPrevMonth)
		spdvalue2 = np.array(df_WindowTMB_all.MidDiffPrevMonth)
		spdvalue3 = np.array(df_WindowTMB_all.TopDiffPrevMonth)
		spdstate1 = np.array(df_WindowTMB_all.Lstate)
		if Tier_input == "1":
            # Bottom Tier
			plt.figure(figsize=(10,6))
			plt.title("Bottom Tier Sales Price Difference Month-over-Month",fontsize=20)
			plt.xlabel("{}".format(scatinput_state.upper()),fontsize=16)
			plt.ylabel("Value",fontsize=16)
			plt.grid (False)
			plt.ylim(100000,300000)
			plt.xticks([i*6 for i in range(10)],fontsize=15)
			plt.yticks(fontsize=15)
			plt.scatter(x=spcdate , y=spcvalue1 , c='red' , s=20 , edgecolors='m')
            #plt.text(x=30,y=45,s="Weights are more or less similar \nafter 18-20 years of age",fontsize=15)
			plt.vlines(x=40,ymin=0,ymax=100,linestyles='dashed',color='k',lw=3)
			plt.legend(['Home Values'],loc=2,fontsize=12)
			plt.show()
		elif Tier_input == "2":
            # Mid Tier
			plt.figure(figsize=(10,6))
			plt.title("Mid Tier Sales Price Difference Month-over-Month",fontsize=20)
			plt.xlabel("{}".format(scatinput_state.upper()),fontsize=16)
			plt.ylabel("Value",fontsize=16)
			plt.grid (False)
			plt.ylim(100000,300000)
			plt.xticks([i*6 for i in range(10)],fontsize=15)
			plt.yticks(fontsize=15)
			plt.scatter(x=spcdate , y=spcvalue2 , c='red' , s=20 , edgecolors='m')
            #plt.text(x=30,y=45,s="Weights are more or less similar \nafter 18-20 years of age",fontsize=15)
			plt.vlines(x=40,ymin=0,ymax=100,linestyles='dashed',color='k',lw=3)
			plt.legend(['Home Values'],loc=2,fontsize=12)
			plt.show()
		elif Tier_input == "3":
            # Tier Tier
			plt.figure(figsize=(10,6))
			plt.title("Top Tier Sales Difference Month-over-Month",fontsize=20)
			plt.xlabel("{}".format(scatinput_state.upper()),fontsize=16)
			plt.ylabel("Value",fontsize=16)
			plt.grid (False)
			plt.ylim(100000,300000)
			plt.xticks([i*6 for i in range(10)],fontsize=15)
			plt.yticks(fontsize=15)
			plt.scatter(x=spcdate , y=spcvalue3 , c='red' , s=20 , edgecolors='m')
            #plt.text(x=30,y=45,s="Weights are more or less similar \nafter 18-20 years of age",fontsize=15)
			plt.vlines(x=40,ymin=0,ymax=100,linestyles='dashed',color='k',lw=3)
			plt.legend(['Home Values'],loc=2,fontsize=12)
			plt.show()
	elif scatinput_market.lower() == "sales" and scatinput_state.lower() != "all" and scatinput_chart == "2":
		Tier_input = input("Which price tier do you want information for? \n\n 1 = Bottom Tier  2 = Mid Tier  3 = Top Tier \n\n")
		# state and date definitions for Difference Month-over-Month (WindowTMB) Scatterplot
		spddate = np.array(df_WindowTMB_all.Date)
		# *** "STATE" OPTION
		spdvalue4 = np.array(df_WindowTMB_state.BottomDiffPrevMonth)
		spdvalue5 = np.array(df_WindowTMB_state.MidDiffPrevMonth)
		spdvalue6 = np.array(df_WindowTMB_state.TopDiffPrevMonth)
		spdstate2 = np.array(df_WindowTMB_state.Lstate)
		if Tier_input == "1":
            # Bottom Tier
			plt.figure(figsize=(10,6))
			plt.title("Bottom Tier Sales Price Difference Month-over-Month",fontsize=20)
			plt.xlabel("{}".format(scatinput_state.upper()),fontsize=16)
			plt.ylabel("Value",fontsize=16)
			plt.grid (False)
			plt.ylim(100000,300000)
			plt.xticks([i*6 for i in range(10)],fontsize=15)
			plt.yticks(fontsize=15)
			plt.scatter(x=spcdate , y=spcvalue4 , c='red' , s=20 , edgecolors='m')
            #plt.text(x=30,y=45,s="Weights are more or less similar \nafter 18-20 years of age",fontsize=15)
			plt.vlines(x=40,ymin=0,ymax=100,linestyles='dashed',color='k',lw=3)
			plt.legend(['Home Values'],loc=2,fontsize=12)
			plt.show()
		elif Tier_input == "2":
            # Mid Tier
			plt.figure(figsize=(10,6))
			plt.title("Mid Tier Sales Price Difference Month-over-Month",fontsize=20)
			plt.xlabel("{}".format(scatinput_state.upper()),fontsize=16)
			plt.ylabel("Value",fontsize=16)
			plt.grid (False)
			plt.ylim(100000,300000)
			plt.xticks([i*6 for i in range(10)],fontsize=15)
			plt.yticks(fontsize=15)
			plt.scatter(x=spcdate , y=spcvalue5 , c='red' , s=20 , edgecolors='m')
            #plt.text(x=30,y=45,s="Weights are more or less similar \nafter 18-20 years of age",fontsize=15)
			plt.vlines(x=40,ymin=0,ymax=100,linestyles='dashed',color='k',lw=3)
			plt.legend(['Home Values'],loc=2,fontsize=12)
			plt.show()
		elif Tier_input == "3":
            # Tier Tier
			plt.figure(figsize=(10,6))
			plt.title("Top Tier Sales Difference Month-over-Month",fontsize=20)
			plt.xlabel("{}".format(scatinput_state.upper()),fontsize=16)
			plt.ylabel("Value",fontsize=16)
			plt.grid (False)
			plt.ylim(100000,300000)
			plt.xticks([i*6 for i in range(10)],fontsize=15)
			plt.yticks(fontsize=15)
			plt.scatter(x=spcdate , y=spcvalue6 , c='red' , s=20 , edgecolors='m')
            #plt.text(x=30,y=45,s="Weights are more or less similar \nafter 18-20 years of age",fontsize=15)
			plt.vlines(x=40,ymin=0,ymax=100,linestyles='dashed',color='k',lw=3)
			plt.legend(['Home Values'],loc=2,fontsize=12)
			plt.show()
	mainmenu()

	
		
# Programming for user input data navigation prompt:
def mainmenu():
    input_1 = input("""What would you like to know? \n\n
    Type the number of the option that best fits your question and press enter.\n\n 
    1 = Avg Sales price table data  2 = Avg Rental Rates table data \n
    3 = Oracle Prediction
    \n\n""")

    if input_1 == "3":
        oraclePredict()
    
    else:
        input_2 = input("""
        What state would you like to know about? \n\n 
        Type the two letter state abbreviation for state isolated metrics \n\n 
        or \"all\" for national metrics.\n\n 
        example: tx (not case sensitive) \n\n""")
    

        if input_1 == "1" and input_2.lower() == "all":
            print('You chose {} with a filter of {}\n\n'.format(input1_op1, input_2.upper()))
            print(sales)
            reset()
        elif input_1 == "1":
            print('You chose {} with a filter of {}\n\n'.format(input1_op1, input_2.upper()))
            print(sales[sales.Lstate == input_2.upper()])
            reset()
        elif input_1 == "2" and input_2.lower() == "all":
            print('You chose {} with a filter of {}\n\n'.format(input1_op2, input_2.upper()))
            print(rental)
            reset()
        elif input_1 == "2":
            print('You chose {} with a filter of {}\n\n'.format(input1_op2, input_2.upper()))
            print(rental[rental.Lstate == input_2.upper()]) 
            reset()                                     
mainmenu()  