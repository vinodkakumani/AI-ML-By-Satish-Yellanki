import pandas as pd
import os

class IndependentEventsProbabilityCalculator:
    """Constructor For Instantiating and Initializing The Required Object"""
    def __init__(self, inFilePath):
        self.inFilePath = inFilePath
        self.data = None

    def validateDataFile(self):
        """Method To Validate The Required Dataset File is Existing and it is in Correct Format"""
        try:
            if not os.path.exists(self.inFilePath):
                raise FileNotFoundError(f"\nFatal Error! The Requested File is Not Found : {self.inFilePath}\n")

            if not self.inFilePath.endswith('.xlsx'):
                raise ValueError(f"\nFatal Error! The File To be Analyzed Should Be Only An Excel File With .xlsx Extension\n")
        except ValueError as valueErrorObject :
            print(f"\nFatal Error! Error Encountered in Finalizing The File Extension : {valueErrorObject}", end="\n")
            raise
        except FileNotFoundError as fnfErrorObject :
            print(f"\nFatal Error! Error Encountered Finding The Specified File : {fnfErrorObject}", end="\n")
            raise
        except Exception as exceptObject :
            print(f"\nFatal Error! Error Encountered in Validating The File: {exceptObject}", end="\n")
            raise

    def loadData(self):
        """Method To Load The Data For Analysis"""
        try:
            self.data = pd.read_excel(self.inFilePath)
            if self.data.empty:
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")

            print(f"\nFinancial Analysis Data is Loaded Successfully From The File : {self.inFilePath}", end="\n")
        except ValueError as valueErrorObject :
            print(f"\nFatal Error! Data Not Found in The Loaded Dataset : {valueErrorObject}", end="\n")
            raise
        except Exception as exceptObject:
            print(f"\nFatal Error! Error Encountered in Loading The Data : {exceptObject}", end="\n")
            raise

    def showData(self):
        """Method To Show The Original Data as is"""
        try:
            if self.data is None:
                raise ValueError(f"\nFatal Error! Data Not Loaded, Call The Proper Method For Loading The Data First...")

            print(f"\nDisplaying The Original Dataset, as Extracted For The File System...\n", end="\n")
            print(self.data)
        except ValueError as valueErrorObject :
            print(f"\nFatal Error! Data Not Found in The Loaded Dataset : {valueErrorObject}", end="\n")
            raise
        except Exception as exceptObject:
            print(f"\nFatal Error! Error Displaying The Data : {exceptObject}", end="\n")
            raise

    def validateEventColumns(self, inRequiredColumns):
        """Method To Validate The Required Event Columns Are Available in The Dataset OR Not"""
        try:
            if self.data is None:
                raise ValueError(f"\nFatal Error! The Data is Not Loaded, Please Load The Data First...\n")

            missingColumns = [outColumn for outColumn in inRequiredColumns if outColumn not in self.data.columns]

            if missingColumns:
                raise ValueError(f"\nFatal Error! Missing Required Columns : {', '.join(missingColumns)}\n")
        except ValueError as valueErrorObject :
            print(f"\nFatal Error! Data Not Found in The Loaded Dataset OR Missing Columns : {valueErrorObject}", end="\n")
            raise
        except Exception as exceptObject:
            print(f"\nFatal Error! Error Validating The Columns : {exceptObject}", end="\n")
            raise

    def independentEventProbabilityCalculator(self, inEventColumn01, inEventColumn02):
        """Method To Calculate The Probability of The Given Independent Events"""
        try:
            self.validateEventColumns([inEventColumn01, inEventColumn02])

            totalRecords = len(self.data)

            if totalRecords == 0:
                raise ValueError(f"\nFatal Error! Dataset Contains No Records")
            
            """Calculating The Probability of Each Event, Suppliend By The End User"""
            event01Probability =  
            
            """
            1. self.data[inEventColumn01] Will Access The Specified Columns in The Dataset
            2. value_counts(normalize = True) 
                1. value_counts Returns The Count of Usnique Values in The Columns
                2. normalize = True Converts The Counts into Probabilities i.e. Relative Frequencies
             Note : The Result is a Normalized Count Where The Sum of All The Values Equals To 1
            3. get("Yes", 0") Fetches The Probability of "Yes" From The Normalized Value Counts 
                Note : If "Yes" Doesnot Exists in The Column, Then it is Defaulted To 0
            """
            event02Probability = self.data[inEventColumn02].value_counts(normalize = True).get("Yes", 0)
            
            """Claculating The Joint Probability of Both The Events Happening Together"""
            bothEventsCount = self.data[
                (self.data[inEventColumn01] == "Yes") & (self.data[inEventColumn02] == "Yes")
              ].shape[0]
            
            bothEventsProbability = bothEventsCount / totalRecords
            
            """Cheking For Independence Using The Formula P(E ∩ H) = P(E) × P(H)"""
            claculatedJointProbability = event01Probability * event02Probability
            
            print(f"\nDisplaying The Probabilities For The Independent Events\n", end = "\n")
            print(f"\nTotal Records Registered in The Given Sample : {totalRecords}\n", end = "\n")
            print(f"\nProbability of {inEventColumn01} (P(E) : {event01Probability : .4f}\n", end = "\n")
            print(f"\nProbability of {inEventColumn02} (P(H) : {event02Probability : .4f}\n", end = "\n")
            print(f"\nThe Joint Probability of (P(E ∩ H)) : {bothEventsProbability : .4f}\n", end = "\n")
            print(f"\nThe Calculated Joint Probability (P(E) × P(H)) : {claculatedJointProbability : .4f}\n", end = "\n")
            
            if abs(bothEventsProbability - claculatedJointProbability) < 1e-4 :
                print(f"\nThe Final Conclusion is : The Events '{inEventColumn01}' And '{inEventColumn02}' Are ***Independent***.\n", end = "\n")
            else :
                print(f"\nThe Final Conclusion is : The Events '{inEventColumn01}' And '{inEventColumn02}' Are ***Not Independent***.\n", end = "\n")
        except ValueError as valueErrorObject :
            print(f"\nFatal Error! Data Not Found in The Loaded Dataset : {valueErrorObject}", end="\n")
            raise
        except Exception as exceptObject:
            print(f"\nFatal Error! in Handling The Required Probability Calculations : {exceptObject}", end="\n")
            raise

def main():
    """Main Function For Implementing The Solution"""
    filePath = r"E:\AIML2024\Implementations\001_Probability\DataSets\RetailPurchaseBehavior.xlsx"

    try:
        """Creating The Object Instance For The Retail Customer Behavior Analysis For Independent Event Class"""
        purchaseBehaviorObject = IndependentEventsProbabilityCalculator(filePath)

        purchaseBehaviorObject.validateDataFile()
        purchaseBehaviorObject.loadData()
        purchaseBehaviorObject.showData()
        eventColumn01 = "Bought Electronics"
        eventColumn02 = "Bought Home Appliances"
        purchaseBehaviorObject.independentEventProbabilityCalculator(eventColumn01, eventColumn02)

    except Exception as exceptObject:
        print(f"\nFatal Error! An Error Encountered While Executing The Application : {exceptObject}", end="\n")

if __name__ == "__main__":
    main()