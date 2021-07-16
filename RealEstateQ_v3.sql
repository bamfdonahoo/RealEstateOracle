/*
FINAL QUERY PAGE FOR TABLE DATA MANIPULATION AND NEW TABLE CREATION FOR THE "REAL ESTATE ORACLE" PYTHON PROGRAM

***Older queries on previous pages ( RealEstateQ.sql & RealEstateQ_v2.sql ) may no longer work, as tables have been changed/renamed and/or deleted
*/

-- Avg difference between values in the same column (difference over time) BOTTOM TIER
-- Performed on the unpivoted tables 
-- ORIGINAL SCHEMA   RegionID | SizeRank | StateName | Lstate | Date | Value
-- NEW SCHEMA        StateName | Lstate | Date | Value | PriorMonth | DiffPrevMonth

SELECT StateName
		, Lstate
		, B.Date
		, Value
		, LAG(Value) 
			OVER(PARTITION BY Lstate ORDER BY B.Date) AS PriorMonth
		, Value - LAG(Value)
			OVER (PARTITION BY Lstate ORDER BY B.Date) AS DiffPrevMonth
--INTO WindowBottom
FROM UnPivAvgSalesPriceMoBotTier AS B
ORDER BY Lstate
		, B.Date
-----------------------------------------------------------------------------------
-- Avg difference between values in the same column (difference over time) TOP TIER
SELECT StateName
		, Lstate
		, T.Date
		, Value
		, LAG(Value) 
			OVER(PARTITION BY Lstate ORDER BY T.Date) AS PriorMonth
		, Value - LAG(Value)
			OVER (PARTITION BY Lstate ORDER BY T.Date) AS DiffPrevMonth
        --, (Value - LAG(Value) OVER (PARTITION BY Lstate ORDER BY T.Date)) / Value AS PercentageChange
--INTO WindowTop
FROM UnPivAvgSalesPriceMoTopTier AS T
ORDER BY Lstate
		, T.Date
	

-- New Table with top, middle(calculated), and bottom windowing values
-- SCHEMA   StateName | Lstate | Date | TopValue | TopPriorMonth | TopDiffPrevMonth | MiddleValue | MidPriorMonth | MidDiffPrevMonth | BottomValue | BottomPriorMonth | BottomDiffPrevMonth

SELECT T.StateName
		, T.Lstate
		, FORMAT(T.Date, 'MM-dd-yyyy' ) AS 'Date'
		, T.Value AS 'TopValue'
		, T.PriorMonth AS 'TopPriorMonth'
		, T.DiffPrevMonth AS 'TopDiffPrevMonth'
		, (T.Value+B.Value)/2 AS 'MiddleValue'
		, (T.PriorMonth+B.PriorMonth)/2 AS 'MidPriorMonth'
		, (T.DiffPrevMonth+B.DiffPrevMonth)/2 AS 'MidDiffPrevMonth'
		, B.Value AS 'BottomValue'
		, B.PriorMonth AS 'BottomPriorMonth'
		, B.DiffPrevMonth AS 'BottomDiffPrevMonth'
--INTO Window_TMB
FROM WindowTop AS T
	JOIN
	WindowBottom AS B
	ON T.StateName = B.StateName
	AND T.Lstate = B.Lstate
	AND T.Date = B.Date
-- WindowTop & WindowBottom tables deleted after table aggregation


-- Creation of new table with all three (Top, Middle, & Bottom Tier) Sales prices in Unpivoted format
SELECT B.StateName
		, B.Lstate AS 'State'
		, FORMAT(B.Date, 'MM-dd-yyyy' ) AS 'Date'
		, B.Value AS 'Bottom Tier'
		, (T.Value+B.Value)/2 AS 'MiddleTier'
		, T.Value AS 'Top Tier'
--INTO AllThreeUnPivSalesPriceMo 
FROM UnPivAvgSalesPriceMoBotTier AS B
	JOIN UnPivAvgSalesPriceMoTOPTier AS T
	ON B.StateName = T.StateName
	AND B.Lstate = T.Lstate
	AND B.Date = T.Date
ORDER BY B.StateName, B.Lstate, 'Date'
-- WindowTop & WindowBottom tables deleted after table aggregation


-- Creation of new UnPivAvgSalesPriceMoMidTier table by avg of Top and Bottom tier due to damaged middle tier data:::

SELECT A3.StateName
		, A3.State AS 'Lstate'
		, A3.Date
		, A3.MiddleTier AS 'Value'
--INTO UnPivAvgSalesPriceMoMidTier
FROM AllThreeUnPivSalesPriceMo AS A3

-- Creation of new ForecastSalesAvg2022 table by avg of Top and Bottom tier due to damaged middle tier data:::
SELECT State AS 'Lstate'
		, CityName
		, BottomTierProjection2022
		, (BottomTierProjection2022+TopTierProjection2022)/2 AS 'MidTierProjection2022'
		, TopTierProjection2022
--INTO ForecastSalesAvg2022
FROM ForecastAvg2022
-- ForecastAvg2022 table deleted after new table creation 





-- Tables to be used for Python "Real Estate Oracle" Program:::

SELECT * FROM AllThreeUnPivSalesPriceMo
SELECT * FROM ForecastSalesAvg2022
SELECT * FROM Window_TMB

