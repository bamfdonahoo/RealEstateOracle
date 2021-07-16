Originally, I intended to simply upload a *.bak file of the database I started with. Throughout maintaining the project and updating and manipulating the information, that file became too large to upload. Instead, here are the actual *.csv files that were obtained from https://www.zillow.com/research/data/ . 

*** ABOUT THE RAW DATA
  - Each of the three avgSalesPrice tables (Pre-Unpivoted) are 309 Columns with 52 Rows 
	- TopTier & BottomTier UnPivAvgSalesPrice tables are 7 columns with 15,332 rows and MidTier is 7 columns with 3,600 rows
	- ForecastCity consists of 6 columns and 30,557 rows
  
By using the attached RealEstateQ.sql / RealEstateQ_v2.sql / and then RealEstateQ_v3.sql query files, you can easily recreate an instance of the same database that I built to use for active background queries in the RealEstateOracle.py program.

To make things easy for you, I uploaded original versions as well as Un-pivoted versions of the tables that I created in PowerQuery. 
