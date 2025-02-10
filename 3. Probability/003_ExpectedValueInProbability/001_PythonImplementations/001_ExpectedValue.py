import pandas as pd
import os

class ExpectedValueCalculator :
    """Constructor For Instantiating and Initializing The Required Object"""
    def __init__(self, inFilePath):
        self.inFilePath = inFilePath
        self.data = None
    
    def validateDataFile(self) :
        """Method To Validate The Required Dataset File is Existing and it is in Correct Format"""
        try :
            if not os.path.exists(self.inFilePath) :
                raise FileNotFoundError(f"\nFatal Error! The Requested File is Not Found : {self.inFilePath}\n")

            if not self.inFilePath.endswith('.xlsx'):
                raise ValueError(f"\nFatal Error! The File To be Analyzed Should Be Only An Excel File With .xlsx Extension\n")
        except ValueError as valueErrorObject :
            print(f"\nFatal Error! Error Encountered in Finalizing The File Extension : {valueErrorObject}", end = "\n")
            raise
        except FileNotFoundError as fnfErrorObject :
            print(f"\nFatal Error! Error Encountered Finding The Specified File : {fnfErrorObject}", end = "\n")
            raise
        except Exception as exceptObject :
            print(f"\nFatal Error! Error Encountered in Validating The File: {exceptObject}", end = "\n")
            raise

    def loadData(self) :
        """Method To Load The Data For Analysis"""
        try :
            self.data = pd.read_excel(self.inFilePath)
            if self.data.empty :
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")

            print(f"\nFinancial Analysis Data is Loaded Successfully From The File : {self.inFilePath}", end = "\n")
        except ValueError as valueErrorObject :
            print(f"\nFatal Error! Data Not Found in The Loaded Dataset : {valueErrorObject}", end = "\n")
            raise
        except Exception as exceptObject:
            print(f"\nFatal Error! Error Encountered in Loading The Data : {exceptObject}", end = "\n")
            raise

    def calculateExpectedValue(self) :
        """Method To Calculate The Expected Value And Updates The Dataset"""
        try :
            if self.data is None:
                raise ValueError(f"\nFatal Error! Data Not Loaded, Call The Proper Method For Loading The Data First...")

            totalSalesRevenue = self.data['Sales Revenue (USD)'].sum()

            self.data['Probability'] = self.data['Sales Revenue (USD)'] / totalSalesRevenue

            self.data['Contribution To EV'] = self.data['Sales Revenue (USD)'] * self.data['Probability']

            expectedValue = self.data['Contribution To EV'].sum()

            return expectedValue, totalSalesRevenue
        except Exception as exceptObject :
            print(f"\nFatal Error! Error Encountered During Expected Value Calculation : {exceptObject}", end = "\n")
            raise

    def showData(self) :
        """Method To Show The Original Data as is"""
        try :
            if self.data is None :
                raise ValueError(f"\nFatal Error! Data Not Loaded, Call The Proper Method For Loading The Data First...")

            print(f"\nDisplaying The Original Dataset, as Extracted For The File System...\n", end = "\n")
            print(self.data)
        except ValueError as valueErrorObject :
            print(f"\nFatal Error! Data Not Found in The Loaded Dataset : {valueErrorObject}", end = "\n")
            raise
        except Exception as exceptObject:
            print(f"\nFatal Error! Error Displaying The Data : {exceptObject}", end = "\n")
            raise

    def saveModifiedData(self, outputPath) :
        """Method To Save The Modified Dataset With Additional Columns To A New File"""
        try :
            if self.data is None :
                raise ValueError("Data Has Not Been Loaded OR Modified. Cannot Save")

            self.data.to_excel(outputPath, index = False)
            print(f"\nModified Data Saved Successfully To : {outputPath}", end = "\n")
        except Exception as exceptObject :
            print(f"Fatal Error While Saving The Modified Data : {exceptObject}")
            raise

# Main routine
def main() :
    inFilePath = r"E:\\AIML2024\\Implementations\\001_Probability\\003_ExpectedValueInProbability\\DataSets\\SalesDataByDiscount.xlsx"
    outputPath = r"E:\\AIML2024\\Implementations\\001_Probability\\003_ExpectedValueInProbability\\DataSets\\Modified_SalesData.xlsx"

    try :
        expectedValueCalculator = ExpectedValueCalculator(inFilePath)

        expectedValueCalculator.loadData()

        print(f"\nDisplaying The Original Data...\n", end = "\n")
        expectedValueCalculator.showData()

        expectedValue, totalSalesRevenue = expectedValueCalculator.calculateExpectedValue()
        print(f"\nTotal Sales Revenue (USD): {totalSalesRevenue:.2f}\n", end = "\n")
        print(f"Calculated Expected Value: {expectedValue:.2f}\n", end = "\n")

        print(f"\nDisplaying Modified Data With Additional Columns...", end = "\n")
        expectedValueCalculator.showData()

        expectedValueCalculator.saveModifiedData(outputPath)

    except Exception as exceptObject :
        print(f"\nAn Error Occurred in Executing The Application : {exceptObject}")

if __name__ == "__main__" :
    main()
