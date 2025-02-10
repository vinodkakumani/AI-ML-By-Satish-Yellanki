#! python3

import pandas as pd
import os
os.system("cls")

inFilePath = r"E://AIML2024//Implementations//001_Probability//DataSets//EmployeeDepartmentalTrainingRecords.csv"

print(f"\nLoading The Data into The Data Frame...Please Wait...", end = "\n")

df = pd.read_csv(inFilePath)

#print(df)

inDepartment = input("\nPlease Enter The Department Name : ")

deptFilterEmployees = df[df['Department'] == inDepartment]

inTrainingStatus = input("\nPlease Enter The Training Status (Yes OR No) : ")

trainedDeptWiseEmployeeCount = deptFilterEmployees[deptFilterEmployees['Trained'] == inTrainingStatus].shape[0]

#print(f"The Count of Employees in Department {inDepartment} Whose Trained Status is {inTrainingStatus} Are : {trainedDeptWiseEmployeeCount}", end = "\n")

totalDepartmentCount = deptFilterEmployees.shape[0]

#print(f"\nThe Total Count of Employees in Department {inDepartment} Are : {totalDepartmentCount}", end = "\n")

conditionalProbability = trainedDeptWiseEmployeeCount / totalDepartmentCount if totalDepartmentCount > 0 else 0

print(f"\nP(Trained | Sales) = {conditionalProbability}", end = "\n")