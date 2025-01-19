import pandas as pd
import os
import matplotlib.pyplot as plt

class StockMarketArithmentiMeanCalculator :
    """Class to calculate arithmetic mean of the student's examination scores"""
    def __init__(self, inFilePath, outFilePath) -> None:
        """Constructor to initialise the file path and load the data"""
        self.inFilePath = inFilePath
        self.outFilePath = outFilePath
        self.data = None

    def loadData(self) :
        """Loads The Dataset From The Given Path"""
        try :
            self.data = pd.read_csv(self.inFilePath)
            self.data["Date"] = pd.to_datetime(self.data["Date"]) # Convert the Date column to datetime
            print(f"\nDataset Loaded Successfully...", end = "\n")
        except FileNotFoundError as fileNotFoundObject :
            print("\nHey! Encounterd an Exception, Exception Stack is : {fileNotFoundObject}", end = "\n")
            raise Exception(f"\nFile Not Found at : {self.inFilePath}. Please Crosss Verify The Path...")
        except Exception as exceptionObject :
            raise Exception(f"\nAn Error Occured While Loading The Dataset : {exceptionObject}")
    
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
            print("Error occurred while loading the data {oExcepObj}", end="\n")
            

    def displaySummary(self) :
        """
        Displays The Summary of The Loaded Dataset
        """
        try :
            if self.data is None :
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")

            print("\nDisplaying The Summary of The Loaded Dataset...", end = "\n")
            print(self.data.describe())
        except Exception as exceptionObject :
            raise Exception("\nHey! An Error Occured While Displaying The Dataset Summary : {exceptionObject}")
        
    def addAdditionalColumns(self):
        """
        Method to add additional columns required for analysis
        """
        try:            
            if self.data is None :
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")
            
            self.data["Daily Price Change"] = self.data["Closing Price"] - self.data["Opening Price"]
            self.data["Percentage of Change"] = (self.data["Daily Price Change"] / self.data["Opening Price"]) * 100
            self.data["High Volume Indicator"] = self.data["Volume"] > self.data["Volume"].mean()
            print("\nAdditional Columns Added Successfully...", end = "\n")
            self.showData()
        except Exception as exceptionObject :
            print(f"\nHey! An Error Occured While Adding Additional Columns to Dataset : {exceptionObject}")
            raise Exception("\nHey! An Error Occured While Adding Additional Columns to Dataset : {exceptionObject}")
        
    def calculateArithmeticMean(self):
        """
        Method to calclulate the arithmetic mean of the students score in Mathemetics
        """
        try: 
            if self.data is None:
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")

            # aritmeticMean = self.data["Score"].sum() / self.data["Score"].count()
            aritmeticMean = self.data["Opening Price"].mean()
            print(f"Arithmeic Mean of the Opening Price of the market is is {aritmeticMean}")
        except Exception as exObj:
            raise Exception(f"\nHey! An Error Occured While Calculating Arithmethic Mean of the Students Score : {exObj}")

    def saveModifiedData(self):
        """
        Method to save the modified dataset
        """
        try:
            if self.data is None:
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")
            self.data.to_csv(self.outFilePath)
        except Exception as excpObj:
            raise Exception(f"\nHey! An Error Occured While Saving Modified Data : {excpObj}")
    
    def plotData(self):
        """
        Plotting the stock data with mean value represented on the graph
        """
        try:
            if self.data is None:
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")
            """Plot to show the stock closing proces"""
            plt.figure(figsize=(12, 6))
            plt.bar(self.data["Stock Symbol"].astype(str), self.data["Closing Price"], color="skyblue", label = "Closing Price", edgecolor = "black", alpha = 0.7)
            plt.title("Stock Market Closing Prices")
            plt.xlabel("Stock Symbol")
            plt.ylabel("Closing Price")
            plt.xticks(rotation = 45, ha = "right")
            plt.tight_layout()
            plt.grid(axis = "y", linestyle = "--", alpha = 0.7)
            plt.legend()
            # Calculate and plot the arithmetic mean
            mean_score = self.data["Closing Price"].mean()
            plt.axhline(y=mean_score, color='red', linestyle='--', label=f'Arithmetic Mean: {mean_score:.2f}')
            plt.show()  # Display the plot

            """Ploting the closing procices over the time"""
            plt.figure(figsize=(12, 6))
            for inStockSymbol in self.data["Stock Symbol"].unique():
                outPlotData = self.data[self.data["Stock Symbol"] == inStockSymbol]
                plt.plot(outPlotData["Date"], outPlotData["Closing Price"], label = inStockSymbol, marker = "o", linewidth = 2, alpha = 0.7)
            plt.axhline(y=mean_score, color='red', linestyle='--', label=f'Arithmetic Mean: {mean_score:.2f}')
            plt.title("Stock Market Closing Prices Over Time")
            plt.xlabel("Date")
            plt.ylabel("Closing Price")
            plt.xticks(rotation = 45, ha = "right")
            plt.tight_layout()
            plt.grid(axis = "both", linestyle = "--", alpha = 0.7)
            plt.legend()
            plt.show()  # Display the plot

            """Plot to show class Percentage Change Vs Volume"""
            plt.figure(figsize=(12, 6))
            plt.scatter(self.data["Class Participation (%)"], self.data["Score"], color="red", alpha = 0.7)
            plt.title("Class Participarion Vs Scores")
            plt.xlabel("Class Participarion %")
            plt.ylabel("Score")
            plt.xticks(rotation = 45, ha = "right")
            plt.tight_layout()
            plt.grid(True)
            plt.axhline(y=mean_score, color='red', linestyle='--', label=f'Arithmetic Mean: {mean_score:.2f}')
            plt.legend()
            
            plt.show()  # Display the plot

        except Exception as excpObj:
            raise Exception(f"\nHey! An Error Occured While Plotting The Data : {excpObj}")

def main():
    try :
        """Main Function For Implementing The Solution"""
        inFilePath = r"/Users/vinodkakumani/git/vinodkakumani/AI-ML-By-Satish-Yellanki/4. Statistics/001_ArtithmeticMean/002_StockMarketPerformance/StockMarketData.csv"
        outFilePath = r"/Users/vinodkakumani/git/vinodkakumani/AI-ML-By-Satish-Yellanki/4. Statistics/001_ArtithmeticMean/002_StockMarketPerformance/StockMarketData_Output.csv"

        """Create StudentScoresArithmentiMeanCalculator Object"""
        calculator = StockMarketArithmentiMeanCalculator(inFilePath, outFilePath)

        """Load the data"""
        calculator.loadData()
        calculator.showData()
        calculator.displaySummary()
        calculator.addAdditionalColumns()
        calculator.calculateArithmeticMean()
        calculator.saveModifiedData()
        calculator.plotData()
    except Exception as exceptionObj:
        print(f"Fatal error occurred while executing the solution {exceptionObj}", end="\n")


if __name__ == "__main__":
    main()