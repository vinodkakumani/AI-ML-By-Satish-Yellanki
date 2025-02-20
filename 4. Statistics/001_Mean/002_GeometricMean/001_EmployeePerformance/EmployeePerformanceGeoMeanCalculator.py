import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from math import prod

class EmployeePerformanceGeoMeanCalculator:
    """Class to calculate geometric mean of the employee values"""

    def __init__(self, inFilePath, outFilePath) -> None:
        """Constructor to initialize the file path and load the data"""
        self.inFilePath = inFilePath
        self.outFilePath = outFilePath
        self.data = None

    def loadData(self):
        """Loads the dataset from the given path"""
        try:
            self.data = pd.read_csv(self.inFilePath)
            self.data["Date"] = pd.to_datetime(self.data["Date"])  # Convert the Date column to datetime
            print(f"\nDataset Loaded Successfully...", end="\n")
        except FileNotFoundError as fileNotFoundObject:
            print(f"\nHey! Encountered an Exception, Exception Stack is : {fileNotFoundObject}", end="\n")
            raise Exception(f"\nFile Not Found at : {self.inFilePath}. Please Cross Verify The Path...")
        except Exception as exceptionObject:
            raise Exception(f"\nAn Error Occurred While Loading The Dataset : {exceptionObject}")

    def showData(self):
        """
        Show the first 10 rows
        """
        try:
            if self.data is None:
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")
            
            print("\nDisplaying first 10 rows of data...")
            print(self.data.head(10))
        except Exception as oExcepObj:
            print(f"Error occurred while loading the data {oExcepObj}", end="\n")

    def displaySummary(self):
        """
        Displays the summary of the loaded dataset
        """
        try:
            if self.data is None:
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")

            print("\nDisplaying the Summary of the Loaded Dataset...", end="\n")
            print(self.data.describe())
        except Exception as exceptionObject:
            raise Exception(f"\nHey! An Error Occurred While Displaying The Dataset Summary : {exceptionObject}")

    def addAdditionalColumns(self):
        """
        Method to add additional columns required for analysis
        """
        try:
            if self.data is None:
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")
            
            # Adding a column for logarithm of Value for geometric mean calculation
            self.data["Log Value"] = self.data["Value"].apply(lambda x: np.log(x) if x > 0 else 0)
            print("\nAdditional Columns Added Successfully...", end="\n")
            self.showData()
        except Exception as exceptionObject:
            print(f"\nHey! An Error Occurred While Adding Additional Columns to Dataset : {exceptionObject}")
            raise Exception(f"\nHey! An Error Occurred While Adding Additional Columns to Dataset : {exceptionObject}")

    def calculateGeometricMean(self):
        """
        Method to calculate the geometric mean of the employee values
        """
        try:
            if self.data is None:
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")
            
            # Using the logarithmic method to calculate geometric mean
            log_sum = self.data["Log Value"].sum()
            count = self.data["Value"].count()
            geometricMean = np.exp(log_sum / count)
            print(f"Geometric Mean of the Employee Values is {geometricMean}")
        except Exception as exObj:
            raise Exception(f"\nHey! An Error Occurred While Calculating Geometric Mean of the Employee Values : {exObj}")

    def saveModifiedData(self):
        """
        Method to save the modified dataset
        """
        try:
            if self.data is None:
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")
            self.data.to_csv(self.outFilePath, index=False)
            print(f"\nModified data saved to {self.outFilePath}")
        except Exception as excpObj:
            raise Exception(f"\nHey! An Error Occurred While Saving Modified Data : {excpObj}")

    def plotData(self):
        """
        Plotting the employee data with geometric mean represented on the graph
        """
        try:
            if self.data is None:
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")

            # Plot to show the employee values
            plt.figure(figsize=(12, 6))
            plt.bar(self.data["Name"], self.data["Value"], color="skyblue", edgecolor="black", alpha=0.7)
            plt.title("Employee Values")
            plt.xlabel("Name")
            plt.ylabel("Value")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.grid(axis="y", linestyle="--", alpha=0.7)

            # Calculate and plot the geometric mean
            geometric_mean = np.exp(self.data["Log Value"].mean())
            plt.axhline(y=geometric_mean, color='red', linestyle='--', label=f'Geometric Mean: {geometric_mean:.2f}')
            plt.legend()
            plt.show()  # Display the plot

        except Exception as excpObj:
            raise Exception(f"\nHey! An Error Occurred While Plotting The Data : {excpObj}")

def main():
    try:
        """Main Function For Implementing The Solution"""
        inFilePath = r"/Users/vinodkakumani/git/vinodkakumani/AI-ML-By-Satish-Yellanki/4. Statistics/002_GeometricMean/001_EmployeePerformance/EmployeePerformance.csv"
        outFilePath = r"/Users/vinodkakumani/git/vinodkakumani/AI-ML-By-Satish-Yellanki/4. Statistics/002_GeometricMean/001_EmployeePerformance/EmployeePerformance_Output.csv"

        """Create EmployeePerformanceGeoMeanCalculator Object"""
        calculator = EmployeePerformanceGeoMeanCalculator(inFilePath, outFilePath)

        """Load the data"""
        calculator.loadData()
        calculator.showData()
        calculator.displaySummary()
        calculator.addAdditionalColumns()
        calculator.calculateGeometricMean()  # Changed method to calculate geometric mean
        calculator.saveModifiedData()
        calculator.plotData()
    except Exception as exceptionObj:
        print(f"Fatal error occurred while executing the solution {exceptionObj}", end="\n")

if __name__ == "__main__":
    main()