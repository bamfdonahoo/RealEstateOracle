/*
Blake Donahoo 8-08-2021

FEATURE ENGINEERING FOR REAL ESTATE DATA 

Isolate the state of Texas for Rental market and Mortgage rates to be put into one *.CSV file for ML in Python

---------------------------------------------------------------------------------------------------------------*/



-- Top/Middle/Bottom Tier Sales Prices with 30,60 and 90 Day Price Changes 

SELECT StateName
	, Lstate
	, Date
	, BottomTier
	, LAG(BottomTier)
		OVER(PARTITION BY Lstate ORDER BY Date) AS B_PriorMonth
	, BottomTier - LAG(BottomTier)
		OVER(PARTITION BY Lstate ORDER BY Date) AS B_DiffPrevMonth
	, LAG(BottomTier, 2)
		OVER(PARTITION BY Lstate ORDER BY Date) AS B_60DayDiff
	, BottomTier - LAG(BottomTier, 2)
		OVER(PARTITION BY Lstate ORDER BY Date) AS B_60DayChange
	, LAG(BottomTier, 3)
		OVER(PARTITION BY Lstate ORDER BY Date) AS B_90DayDiff
	, BottomTier - LAG(BottomTier, 3)
		OVER(PARTITION BY Lstate ORDER BY Date) AS B_90DayChange
	, MiddleTier
	, LAG(MiddleTier)
		OVER(PARTITION BY Lstate ORDER BY Date) AS M_PriorMonth
	, MiddleTier - LAG(MiddleTier)
		OVER(PARTITION BY Lstate ORDER BY Date) AS M_DiffPrevMonth
	, LAG(MiddleTier, 2)
		OVER(PARTITION BY Lstate ORDER BY Date) AS M_60DayDiff
	, MiddleTier - LAG(MiddleTier, 2)
		OVER(PARTITION BY Lstate ORDER BY Date) AS M_60DayChange
	, LAG(MiddleTier, 3)
		OVER(PARTITION BY Lstate ORDER BY Date) AS M_90DayDiff
	, MiddleTier - LAG(MiddleTier, 3)
		OVER(PARTITION BY Lstate ORDER BY Date) AS M_90DayChange
	, TopTier
	, LAG(TopTier)
		OVER(PARTITION BY Lstate ORDER BY Date) AS T_PriorMonth
	, TopTier - LAG(TopTier)
		OVER(PARTITION BY Lstate ORDER BY Date) AS T_DiffPrevMonth
	, LAG(TopTier, 2)
		OVER(PARTITION BY Lstate ORDER BY Date) AS T_60DayDiff
	, TopTier - LAG(TopTier, 2)
		OVER(PARTITION BY Lstate ORDER BY Date) AS T_60DayChange
	, LAG(TopTier, 3)
		OVER(PARTITION BY Lstate ORDER BY Date) AS T_90DayDiff
	, TopTier - LAG(TopTier, 3)
		OVER(PARTITION BY Lstate ORDER BY Date) AS T_90DayChange
INTO SalesPrice_TMB_306090_Window_ByDate
FROM AllThreeUnPivSalesPriceMo
--WHERE Lstate LIKE 'TX'

-- ADD Monthly Mortgage Payment columns (Calculated at a high avg of 7% on a 30y ammortization)

SELECT *
	, (BottomTier/30)/12 AS B_PrincipalMonthly
	, (((Bottomtier + ((BottomTier * 0.07)*30))/30)/12) AS B_AvgMortgage
	, (MiddleTier/30)/12 AS M_PrincipalMonthly
	, (((MiddleTier + ((MiddleTier * 0.07)*30))/30)/12) AS M_AvgMortgage
	, (TopTier/30)/12 AS T_PrincipalMonthly
	, (((TopTier + ((TopTier * 0.07)*30))/30)/12) AS T_AvgMortgage
INTO SalesPrice_TMB_306090_Window_ByDate_wMort
--FROM Texas_SalesPrice_TMB_306090_Window_ByDate
FROM SalesPrice_TMB_306090_Window_ByDate


--ADD Monthly Principal, Monthly Interest columns

SELECT *
	, B_AvgMortgage - B_PrincipalMonthly AS B_InterestMonthly
	, M_AvgMortgage - M_PrincipalMonthly AS M_InterestMonthly
	, T_AvgMortgage - T_PrincipalMonthly AS T_InterestMonthly
INTO SalesPrice_FullEDA
--FROM Texas_SalesPrice_TMB_306090_Window_ByDate_wMort
FROM SalesPrice_TMB_306090_Window_ByDate_wMort

SELECT *
	, B_AvgMortgage*12 AS B_AvgAnnual
	, M_AvgMortgage*12 AS M_AvgAnnual
	, T_AvgMortgage*12 AS T_AvgAnnual
INTO SalesPrice_FullEDA2
--FROM Texas_SalesPrice_FullEDA
FROM SalesPrice_FullEDA

--#####################################################
--Now to do similar Ft.Eng. for the Rental Price Tables 
--#####################################################

SELECT Lstate
	, CityName
	, Date
	, Value*12 AS R_Annual
	, Value AS R_Monthly
	, LAG(Value)
		OVER(PARTITION BY Lstate ORDER BY Date) AS R_PriorMonth
	, Value - LAG(Value)
		OVER(PARTITION BY Lstate ORDER BY Date) AS R_DiffPrevMonth
	, LAG(Value, 2)
		OVER(PARTITION BY Lstate ORDER BY Date) AS R_60DayDiff
	, Value - LAG(Value, 2)
		OVER(PARTITION BY Lstate ORDER BY Date) AS R_60DayChange
	, LAG(Value, 3)
		OVER(PARTITION BY Lstate ORDER BY Date) AS R_90DayDiff
	, Value - LAG(Value, 3)
		OVER(PARTITION BY Lstate ORDER BY Date) AS R_90DayChange
--INTO Texas_Rental_FullEDA
INTO Rental_FullEDA
FROM RentalRatesUnPiv
--WHERE Lstate LIKE 'TX'


select *
from SalesPrice_FullEDA2

select *
from Rental_FullEDA








