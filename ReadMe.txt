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




As a supplement to my main capstone project of the RealData Application (currently on hold) this is an analysis of the real estate market in the US with data obtained 
from https://www.zillow.com/research/data/ as *.CSV files and constructed into a SQL database. While this analysis is done partly out of personal interest (having studied
real estate in California, Nevada and Texas), it also serves as a better lab-rat to test and illustrate analytical and ML ability acquired through content taught in the 
Divergence DSI course. I was otherwise finding myself preoccupied with UI/UX properties of the application I was developing and not focusing enough of my energy into 
displaying the more relevant concepts at-hand :)

The data obtained consists of:::
-Average sales price of a Single Family Residence (SFR) (Top Tier) from January 1996 to May 2021
-Average sales price of a SFR (Bottom Tier) from January 1996 to May 2021
-New listings per state from November 2017 to May 2021
-Predicted percentage of increase by May 2022 (One year forecast)
SOURCE: https://www.zillow.com/research/data/

The first steps of cleaning and shaping the data through a series of SQL queries will give us the calculated and aggregated tables that will be used in Microsoft Power Bi to 
build visual models of findings which will be further trunicated through DAX queries for further calculations.

Isolated data that is observed as being peculiar or particularly interesting will be further tested and analyzed in Python and Jupyter Notebooks to identify trends that are 
valuble enough to be showcased as official "findings" along side the Power Bi visuals.

This project can be seen as a "hedge" bet against my primary capstone which follows a Machine Learning/Feature Engineering (Data Engineer) blueprint
as opposed to "RDA" which follows a full application development blueprint. 

I will be uploading a *.bak of the database file I created (DEPRICATED - backup too large) , TSQL queries, DAX queries, *.pbix for visual models, as well as *.ipynb for a finished product.

Finished product will be a user-input based command line application to easily navigate through an extensive library of tables and visuals pertaining to the real estate market.

~ Enjoy
