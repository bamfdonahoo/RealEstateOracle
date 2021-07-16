/*Blake Donahoo June 20, 2021 
Analysis of Single Family Residences in the United States from January 1996 to May 2021.
A few basic calculations on the "RealEstate" Database I created with *.CSV files downloaded from https://www.zillow.com/research/data/ .
In preparation for further data manipulation in Jupyter Notebooks and PowerBi/DAX:::

Basic questions and expectations one might ask themselves when reviewing the data:
1) What are the current Top and Bottom Tier Single family residence sales prices as of May of 2021?
2) How big is the gap between the two Tiers?
3) What is the average sales price for any home within the United States?
4) What percentage of change can we see from the earliest data we have to the present (01/1996 - 05/2021)?

5) What is the average change per year that can be observed from the data? 
	avg(high) & avg(low)
5.2) What is the average aggregated change per year? 
	AVG(avg(high),avg(low))

) Create new data table for a (High & Low) price prediction (In any city in the USA) in May 2022 (One Year Forecast) 
	INCLUDING: AverageChangePerYear
*/

--Top Tier and Bottom Tier sales price of a single family residence (SFR) in Texas in May of 2021
--1) What are the current Top and Bottom Tier Single family residence sales prices as of May of 2021?
SELECT T.StateName, T.may2021 AS 'Top Tier'	
FROM avgSalesPriceMOtopTier AS T 
WHERE T.StateName LIKE 'Texas' 
------
SELECT B.StateName, B.may2021 AS 'Bottom Tier'	
FROM avgSalesPriceMObotTier AS B
WHERE B.StateName LIKE 'Texas'
/*
							StateName                                          Top Tier
							-------------------------------------------------- ---------------------------------------
							Texas                                              425969

							(1 row affected)

							StateName                                          Bottom Tier
							-------------------------------------------------- ---------------------------------------
							Texas                                              142658

							(1 row affected)
*/
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
--Percentage of the Top Tier that the Bottom Tier represents >> (State and National level)
--2) How big is the gap between the two Tiers?
SELECT avg(B.may2021 / (T.may2021/100)) AS ' Average Percentage Difference'
FROM avgSalesPriceMObotTier AS B, avgSalesPriceMOtopTier AS T
WHERE B.StateName LIKE 'Texas'

--SELECT avg(T.may2021-B.may2021) / (avg(T.may2021)/100) AS ' Average Percentage Difference'
--FROM avgSalesPriceMObotTier AS B, avgSalesPriceMOtopTier AS T

/* 
						 Average Percentage Difference			<< (Between Top & Bottom Tier Single Family Residences in Texas)
						---------------------------------------
						33.44022927261284

						(1 row affected)

		SANITY CHECK>>					RAW TEXAS STATE PERCENTAGE DIFFERENCE = 33.49%
										142658  =    x   
										-------   ------
										425969  =   100

										425969(X)=14265800 = 33.49%
*/
SELECT avg(B.may2021) AS ' Average National May2021 Low'
FROM avgSalesPriceMObotTier AS B
/*
										 Average National May2021 Low
										---------------------------------------
										184447.490196

										(1 row affected)
*/
SELECT avg(T.may2021) AS ' Average National May2021 High'
FROM avgSalesPriceMOtopTier AS T
/*
										 Average National May2021 High
										---------------------------------------
										499001.254901

										(1 row affected)
*/


SELECT (avg(B.may2021)*100) / avg(T.may2021) AS ' Average National Percentage Difference'
FROM avgSalesPriceMObotTier AS B, avgSalesPriceMOtopTier AS T
/*
										 Average National Percentage Difference = 36.96%		<< (Between Top & Bottom Tier Single Family Residences Nationally)
										---------------------------------------
										36.963331

										(1 row affected)

		SANITY CHECK>>					RAW NATIONAL PERCENTAGE DIFFERENCE = 
										184447.49  =    x   
										-------       ------
										499001.25  =   100

										499001.25(X)=18444749 = 36.96%
*/
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
--Average sales price of a SFR in the United States in May of 2021
--3) What is the average sales price for any home (IN EACH STATE) within the United States?
SELECT (T.may2021+B.may2021)/2 AS AverageSalesPrice, T.StateName
FROM avgSalesPriceMOtopTier AS T JOIN avgSalesPriceMObotTier AS B
ON T.Lstate = B.Lstate
WHERE T.StateName LIKE 'Texas'
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
-- Just a note to myself for further calculations:::
-- int to multiply avg sales price by
SELECT avg(ForecastPct)/100 AS 'Multipy by this'
FROM ForecastCity AS F
----------------------------------------------------
--Create new table for Forecasted Average sales price of a **TOP tier SFR in the US in May of 2022
--CREATE TABLE ForecastAvgCity
SELECT 
	(SELECT 
		AVG(T.may2021) 
		FROM avgSalesPriceMOtopTier AS T
	)
	* 
	(1+ AVG(ForecastPct)/100) AS 'NationalProjectedHigh2022' 
	,F.CityName
	,F.Lstate AS 'State'
FROM ForecastCity AS F 
	JOIN avgSalesPriceMOtopTier AS T
ON F.Lstate = T.Lstate
GROUP BY F.CityName, F.Lstate
ORDER BY NationalProjectedHigh2022 ASC
--Forecasted Average sales price of a **BOTTOM tier SFR in the US in May of 2022
SELECT 
	(SELECT 
		AVG(B.may2021) 
		FROM avgSalesPriceMObotTier AS B
	)
	* 
	(1+ AVG(ForecastPct)/100) AS 'NationalProjectedLow2022' 
	,F.CityName
	,F.Lstate AS 'State'
FROM ForecastCity AS F 
	JOIN avgSalesPriceMObotTier AS B
ON F.Lstate = B.Lstate
GROUP BY F.CityName, F.Lstate
ORDER BY NationalProjectedLow2022 ASC
--Combination table of the two National Projection queries above 
--NationalProjectedLow2022 | NationalProjectedHigh2022 | CityName | State

-- With A as (...) , B as (...) SELECT A.x, B.y FROM A JOIN B ..

WITH X AS (SELECT
				(SELECT
						AVG(T.may2021)
						FROM avgSalesPriceMOtopTier AS T
				)
				*
				(1+ AVG(ForecastPct)/100) AS 'TopTierProjection2022'
				,F.CityName
				,F.Lstate AS 'State'
			FROM ForecastCity AS F 
				JOIN avgSalesPriceMOtopTier AS T
			ON F.Lstate = T.Lstate
			GROUP BY F.CityName, F.Lstate
			)
,
Y AS (SELECT
				(SELECT
						AVG(B.may2021)
						FROM avgSalesPriceMObotTier AS B
				)
				*
				(1+ AVG(ForecastPct)/100) AS 'BottomTierProjection2022'
				,F.CityName
				,F.Lstate AS 'State'
			FROM ForecastCity AS F 
				JOIN avgSalesPriceMObotTier AS B
			ON F.Lstate = B.Lstate
			GROUP BY F.CityName, F.Lstate
			)
SELECT X.TopTierProjection2022
		, Y.BottomTierProjection2022
		, X.CityName
		, X.State
INTO ForecastAvg2022
FROM X 
	JOIN
	 Y
ON X.State = Y.State
	AND
	X.CityName = Y.CityName
ORDER BY Y.State DESC;
/*
(22639 rows affected)

Completion time: 2021-06-25T15:41:53.8433806-05:00
*/

--Forecasted Average sales price of a **TOP tier SFR in each city in TEXAS in May of 2022
SELECT 
	(SELECT 
		AVG(T.may2021) 
		FROM avgSalesPriceMOtopTier AS T
		WHERE T.Lstate LIKE 'TX')
	* 
	(1+ AVG(ForecastPct)/100) AS 'ProjectedHigh2022' 
	,F.CityName
FROM ForecastCity AS F 
	JOIN avgSalesPriceMOtopTier AS T
ON F.Lstate = T.Lstate
WHERE F.Lstate LIKE 'TX'
GROUP BY F.CityName
ORDER BY ProjectedHigh2022 ASC

--Forecasted Average sales price of a **BOTTOM tier SFR in each city in TEXAS in May of 2022
SELECT 
	(SELECT 
		AVG(B.may2021) 
		FROM avgSalesPriceMObotTier AS B
		WHERE B.Lstate LIKE 'TX')
	* 
	(1+ AVG(ForecastPct)/100) AS 'ProjectedLow2022' 
	,F.CityName
FROM ForecastCity AS F 
	JOIN avgSalesPriceMObotTier AS B
ON F.Lstate = B.Lstate
WHERE F.Lstate LIKE 'TX'
GROUP BY F.CityName
ORDER BY ProjectedLow2022 ASC
---------------------------------------------------
--4) What percentage of change can we see from the earliest data we have to the present (01/1996 - 05/2021)?
--436113.137255
SELECT AVG(T.may2021+B.may2021) - AVG(T.jan1996+B.jan1996) AS AverageSalesPriceDifference
FROM avgSalesPriceMOtopTier AS T JOIN avgSalesPriceMObotTier AS B
ON T.Lstate = B.Lstate
/*
AverageSalesPriceDifference
---------------------------------------
436113.137255

(1 row affected)
*/
SELECT (AVG(T.may2021+B.may2021) - AVG(T.jan1996+B.jan1996)) / (AVG(T.may2021+B.may2021)/100) AS AverageSalesPriceDifferencePercentage
FROM avgSalesPriceMOtopTier AS T, avgSalesPriceMObotTier AS B
/*
AverageSalesPriceDifferencePercentage
---------------------------------------
63.810657

(1 row affected)
*/




