 SELECT *
  FROM SQL.dbo.EmployeeDemographics
  full outer join SQL.dbo.warehouseEmployeeDemographics
   ON EmployeeDemographics.EmployeeID = warehouseEmployeeDemographics.EmployeeID
SELECT *
FROM SQL.dbo.EmployeeDemographics

SELECT *
FROM SQL.dbo.EmployeeSalary
ORDER BY EmployeeID
   

