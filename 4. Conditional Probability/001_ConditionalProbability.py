import pandas as pd
import os

class ConditionalProbability :
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

    def addNewColumn(self, inNewColumnName, inLogicRule) :
        """Method To Add a New Column To The Dataset, With Respect To The Provided Logic"""
        try :
            if inNewColumnName in self.data.columns :
                print(f"\nColumn '{inNewColumnName}' Already Exists, Hence Cannot Add\n", end = "\n")
            else :
                self.data[inNewColumnName] = self.data.apply(inLogicRule, axis = 1)
                print(f"\nNew Column '{inNewColumnName}' Added Successfully\n", end = "\n")
                self.showData()
        except Exception as exceptObject:
            print(f"\nFatal Error! Error Displaying The Data : {exceptObject}", end="\n")
            raise
    
    def calculateConditionalProbability(self, inCondition, inSubSetCondition) :
        """Method To Calculate The Conditional Probability Based on The Supplie Conditions, and Return The Calculated Conditional Probability"""
        try :
            subSetConditionData = self.data[self.data.apply(inSubSetCondition, axis = 1)]
            outNumeratorValues = subSetConditionData[subSetConditionData.apply(inCondition, axis = 1)]
            outConditionalProbability = len(outNumeratorValues)  / len(subSetConditionData) if len(subSetConditionData) > 0 else 0
            return outConditionalProbability
        except Exception as exceptObject:
            print(f"\nFatal Error! Error Calculating The Conditional Probability : {exceptObject}", end="\n")
            raise
            
def main():
    """Main Function For Implementing The Solution"""
    filePath = r"E:\AIML2024\Implementations\001_Probability\002_ConditionalProbabilities\DataSets\EmployeesData.xlsx"

    try:
        """Creating The Object Instance For The Retail Customer Behavior Analysis For Independent Event Class"""
        conditionalProbabilityObject = ConditionalProbability(filePath)

        conditionalProbabilityObject.validateDataFile()
        conditionalProbabilityObject.loadData()
        conditionalProbabilityObject.showData()
        
        conditionalProbabilityObject.addNewColumn("PerformanceCategory", lambda addRow : "High" if addRow["PerformanceRating"] >= 4 else "Low")
        
        print(f"\nCalculating The Conditional Probabilities as Supplied By The Relevant Conditions...\n", end = "\n")
        
        probabilityPromotedGivenHR = conditionalProbabilityObject.calculateConditionalProbability(
                    inCondition = lambda addRow : addRow["Promoted"] == "Yes",
                    inSubSetCondition = lambda addRow : addRow["Department"] == "HR"
                )
        
        print(f"\nP(Promoted | Department = HR)  : {probabilityPromotedGivenHR : .2f}\n", end = "\n")
        
        probabilityPromotedGivenHighPerformance = conditionalProbabilityObject.calculateConditionalProbability(
                    inCondition = lambda addRow : addRow["Promoted"] == "Yes",
                    inSubSetCondition = lambda addRow : addRow["PerformanceCategory"] == "High"
                )
        
        print(f"\nP(Promoted | PerformanceRating >= 4)  : {probabilityPromotedGivenHighPerformance : .2f}\n", end = "\n")

        probabilityPromotedGivenNoAttrition = conditionalProbabilityObject.calculateConditionalProbability(
                    inCondition = lambda addRow : addRow["Promoted"] == "Yes",
                    inSubSetCondition = lambda addRow : addRow["Attrition"] == "No"
                )
        
        print(f"\nP(Promoted | Attrition = No)  : {probabilityPromotedGivenNoAttrition : .2f}\n", end = "\n")

        probabilityAttritionGivenNotPromoted = conditionalProbabilityObject.calculateConditionalProbability(
                    inCondition = lambda addRow : addRow["Attrition"] == "Yes",
                    inSubSetCondition = lambda addRow : addRow["Promoted"] == "No"
                )
        
        print(f"\nP(Attrition = Yes | Promoted = No)  : {probabilityAttritionGivenNotPromoted : .2f}\n", end = "\n")
        
        #conditionalProbabilityObject.showData()
                   
    except Exception as exceptObject:
        print(f"\nFatal Error! An Error Encountered While Executing The Application : {exceptObject}", end="\n")

if __name__ == "__main__":
    main()            