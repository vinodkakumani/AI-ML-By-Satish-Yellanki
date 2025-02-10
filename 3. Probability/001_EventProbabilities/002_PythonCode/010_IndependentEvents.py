import pandas as pd
import os

class IndependentEventsProbabilityCalculator :
    """Constructor For Instantiating and Initializing The Required Object"""
    def __init__(self, inFilePath) :
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
            print(f"\nFatal Error! Error Encountered in Finalizing The File Extension : {valueErrorObject}", end="\n")
            raise
        except FileNotFoundError as fnfErrorObject :
            print(f"\nFatal Error! Error Encountered Finding The Specified File : {fnfErrorObject}", end="\n")
            raise
        except Exception as exceptObject :
            print(f"\nFatal Error! Error Encountered in Validating The File: {exceptObject}", end="\n")
            raise

    def loadData(self) :
        """Method To Load The Data For Analysis"""
        try :
            self.data = pd.read_excel(self.inFilePath)
            if self.data.empty :
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")

            print(f"\nFinancial Analysis Data is Loaded Successfully From The File : {self.inFilePath}", end="\n")
        except ValueError as valueErrorObject :
            print(f"\nFatal Error! Data Not Found in The Loaded Dataset : {valueErrorObject}", end="\n")
            raise
        except Exception as exceptObject:
            print(f"\nFatal Error! Error Encountered in Loading The Data : {exceptObject}", end="\n")
            raise

    def showData(self) :
        """Method To Show The Original Data as is"""
        try :
            if self.data is None :
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
    
    def calculateEventProbability(self, inEventColumn, eventValue = "Yes") :
        """Method To Calculate The Probability of Events Occuring As Supplied By The End User"""
        try :
            eventProbability = self.data[inEventColumn].value_counts(normalize = True).get(eventValue, 0)
            print(f"\nCalculating The Probability of Event Value {eventValue} in Event Column {inEventColumn}\n", end = "\n")
            print(f"\nThe Total Occurances of '{eventValue}' : {self.data[inEventColumn].value_counts().get(eventValue, 0)}\n", end = "\n")
            print(f"\nThe Total Number of Records in The Sample Are : {len(self.data)}\n", end = "\n")
            print(f"\nThe Calculated Probability of '{eventValue}' = {eventProbability : .4f}\n", end = "\n")
            return eventProbability
        except KeyError as keyErrorObj :
            print(f"\nFatal Error! {eventValue} Not Found in The Column {inEventColumn}\n", end = "\n")
            raise
        except Exception as exceptObj :
            print(f"\nFatal Error! Error Encountered in Calculating The Event Probability : {exceptObj}\n", end = "\n")
            raise
    
    def calculateJointProbability(self, inEventColumn01, inEventColumn02, eventValue01 = "Yes", eventValue02 = "Yes") :
        """Method To Calculate The Joint Probability of Two Independent Events Occuring Together"""
        try :
            eventColumn01 = self.data[inEventColumn01] == eventValue01
            eventColumn02 = self.data[inEventColumn02] == eventValue02 
            jointProbability = len(self.data[eventColumn01 & eventColumn02]) / len(self.data)
            print(f"\nCalculating The Joint Probability of '{eventValue01}' in {inEventColumn01} and '{eventValue02}' in {inEventColumn02}\n", end = "\n")
            print(f"\nThe Total Occurances of '{eventValue01}' in {inEventColumn01} : {len(self.data[eventColumn01])}\n", end = "\n")
            print(f"\nThe Total Occurances of '{eventValue02}' in {inEventColumn02} : {len(self.data[eventColumn02])}\n", end = "\n")
            print(f"\nThe Occurances of Both '{eventValue01}' in {inEventColumn01} and '{eventValue02}' in {inEventColumn02}: {len(self.data[eventColumn01 & eventColumn02])}\n", end = "\n")
            print(f"\nThe Calculated Joint Probability = {jointProbability}\n", end = "\n")
            return jointProbability
        except Exception as exceptObj :
            print(f"\nFatal Error! Error Encountered in Calculating The Joint Probability : {exceptObj}\n", end = "\n")
            raise    
    
	def checkIndependence(self, inEventColumn01, inEventColumn02, eventValue01 = "Yes", eventValue02 = "Yes"):
        """Check Whether The Two Events Are Independent Based on Calculated Vrobabilities"""
        try:
            probEventA = self.calculateEventProbability(inEventColumn01, eventValue01)
            probEventB = self.calculateEventProbability(inEventColumn02, eventValue02)
            probEventA_And_probEventB = self.calculateJointProbability(inEventColumn01, inEventColumn02, eventValue01, eventValue02)
            
            """Logic For Cecking Independence of The Events"""
            print(f"\nChecking Whether Events '{inEventColumn01}' and '{inEventColumn02}' are Independent...\n", end = "\n")
            if abs(probEventA * probEventB - probEventA_And_probEventB) < 0.01 :
                print(f"The Events '{inEventColumn01}' and '{inEventColumn02}' are Independent.\n", end = "\n")
            else:
                print(f"The Events '{inEventColumn01}' and '{inEventColumn02}' are Dependent.\n", end = "\n")
        
        except Exception as exceptObject:
            print(f"\nFatal Error! Error Encountered in Checking Independence of Events: {exceptObject}\n", end = "\n")
            raise

def main():
    """Main Function For Implementing The Solution"""
    filePath = r"E:\AIML2024\Implementations\001_Probability\DataSets\HealthCarePatientRecords.xlsx"

    try:
        """Creating The Object Instance For The Retail Customer Behavior Analysis For Independent Event Class"""
        healthcareAnalysis = IndependentEventsProbabilityCalculator(filePath)

        healthcareAnalysis.validateDataFile()
        healthcareAnalysis.loadData()
        healthcareAnalysis.showData()
        eventColumn01 = "Has Heart Disease"
        eventColumn02 = "Regular Exercise"
        
        healthcareAnalysis.validateEventColumns([eventColumn01, eventColumn02])
        
        healthcareAnalysis.checkIndependence(eventColumn01, eventColumn02)

    except Exception as exceptObject:
        print(f"\nFatal Error! An Error Encountered While Executing The Application : {exceptObject}", end="\n")

if __name__ == "__main__":
    main()