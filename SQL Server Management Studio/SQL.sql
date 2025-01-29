--SELECT TOP (1000) [EmployeeID]
--      ,[FirstName]
--      ,[LastName]
--      ,[Age]
--      ,[Gender]
--  FROM [SQL].[dbo].[warehouseEmployeeDemographics]

--  SELECT *
--  FROM SQL.dbo.EmployeeDemographics
--  SELECT *
--  FROM SQL.dbo.EmployeeSalary
  SELECT *
  FROM SQL.dbo.EmployeeDemographics
  inner join SQL.bdo.EmployeeSalary
   ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
