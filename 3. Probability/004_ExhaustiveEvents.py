import os
import pandas as pd

class ExhaustiveEventsCalculator :
    def __init__(self, inFilePath) :
        """Constructor To Instantiate and Initialize The Class With The Required Dataset And The File Path"""
        self.inFilePath = inFilePath
        self.data = None
    
    def dataLoader(self) :
        """Method To Load The Data From The Referenced Data Set in The Form of Excel File"""
        try :
            if not os.path.exists(self.inFilePath) :
                raise FileNotFoundError(f"\nHey! Fatal Error, File Not Found At Path : {self.inFilePath}")
            
            self.data = pd.read_excel(self.inFilePath)
            print(f"\nSucces! Dataset Loaded Successfully From {self.inFilePath}", end = "\n")
        except FileNotFoundError as fnfErrorObject :
            print(f"\nEncountered An Error : {fnfErrorObject}", end = "\n")
        except Exception as exceptObject :
            print(f"\nAn Unexpected Error Occurred While Loading The Dataset {exceptObject}", end = "\n")
    
    def validateData(self) :
        """Method To Validate The Loaded Data For All The Required Columns"""
        try :
            requiredColumns = ["FavoriteProduct", "StoreLocation", "AgeGroup", "Gender"]
            missingColumns = [outColumn for outColumn in requiredColumns if outColumn not in self.data.columns]

            if missingColumns :
                print(f"\nWarning : The Following Columns Are Missing From The Dataset : {missingColumns}", end = "\n")
            else :
                print(f"\nDataset Validation is Successful, All The Required Columns Are Present in The Dataset", end = "\n")
        except Exception as exceptObject :
            print(f"\nAn Unexpected Error Occurred While Executing The Data Validation : {exceptObject}", end = "\n")
    
    def displayAllRecords(self) :
        """Method To Display All The Records in The Data Set"""
        try :
            if self.data is not None :
                print(f"\nDisplaying All The Records From The Dataset\n", end = "\n")
                print(self.data.to_string(index = False))
            else :
                print(f"\nData is Not Loaded From The Dataset, Check The Dataset is Loaded OR Not", end = "\n")
        except Exception as exceptObject :
            print(f"\nAn Unexpected Error Occurred While Displaying The Data : {exceptObject}", end = "\n")

    def calculateProbabilitiesByGroup(self, inGroupColumns) :
        """Method To Calculate Probabilities By Groups Within The Dataset"""
        try :
            if inGroupColumns not in self.data.columns :
                print(f"\nWarning : Column '{inGroupColumns}' is Not Available in The Dataset, Hence Setting The Probabilities To 0", end = "\n")
                return {inGroupColumns : 0}
            
            groupCounts = self.data[inGroupColumns].value_counts()
            totalCounts = len(self.data)

            outProbabilities = {outGroup : grpCount / totalCounts for outGroup, grpCount in groupCounts.items()}
            return outProbabilities
        except Exception as exceptObject :
            print(f"\nAn Unexpected Error Occurred While Calculating Probabilities By {inGroupColumns} : {exceptObject}", end = "\n")
            return {}
    
    def calculateCombinationProbabilities(self, inColumns) :
        """Method To Calculate The Probabilities in Combinations of Two OR Three Columns"""
        try :
            for outColumns in inColumns :
                if outColumns not in self.data.columns :
                    print(f"\nWarning : Column '{outColumns}' is Not Available in The Dataset.")
                    return {}
            
            combinationCounts = self.data.groupby(inColumns).size().to_dict()
            totalCount = len(self.data)
            
            outProbabilities = {}
            for outCombination, count in combinationCounts.items() :
                outNested = outProbabilities
                for outKey in outCombination[:-1] :
                    outNested = outNested.setdefault(outKey, {})
                outNested[outCombination[-1]] = count / totalCount
            
            return outProbabilities
        except Exception as exceptObject :
            print(f"\nAn Unexpected Error Occurred While Calculating Combination Probabilities For {inColumns}: {exceptObject}")
            return {}

    def displayProbabilities(self, inProbabilities, inDescription) :
        """Method To Display Probabilities in a Readable Format."""
        print(f"\nProbabilities For {inDescription}")
        self._recursive_display(inProbabilities, level = 0)
    
    def _recursive_display(self, inData, level = 0) :
        """Helper Method For Recursive Display of Nested Dictionaries."""
        if isinstance(inData, dict) :
            for key, value in inData.items() :
                print("  " * level + f"{key} : ")
                self._recursive_display(value, level + 1)
        else :
            print("  " * level + f"{inData:.2f}")

def main() :
    """Defining The File Path To The Location of The Dataset"""
    inFilePath = r"E:\AIML2024\Implementations\001_Probability\DataSets\CustomerPurchasePreferences.xlsx"

    """Creating an Object Instance of The Defined Class"""
    exhaustiveEventsCalculatorObject = ExhaustiveEventsCalculator(inFilePath)

    """Calling The Method For Data Loading"""
    exhaustiveEventsCalculatorObject.dataLoader()
    
    """Calling The Method For Displaying All The Data"""
    exhaustiveEventsCalculatorObject.displayAllRecords()

    """Calling The Data Validation Method"""
    if exhaustiveEventsCalculatorObject.data is not None :
        exhaustiveEventsCalculatorObject.validateData()
    
    """Calling Method To Calculate The Probabilities By Individual Columns"""
    for outColumn in ["FavoriteProduct", "StoreLocation", "AgeGroup", "Gender"] :
        groupProbabilities = exhaustiveEventsCalculatorObject.calculateProbabilitiesByGroup(outColumn)
        exhaustiveEventsCalculatorObject.displayProbabilities(groupProbabilities, f"Group Probabilities for {outColumn}")

    """Calling Method To Calculate The Combination Probabilities"""
    combinationColumns = ["FavoriteProduct", "StoreLocation"]
    combinationProbabilities = exhaustiveEventsCalculatorObject.calculateCombinationProbabilities(combinationColumns)
    exhaustiveEventsCalculatorObject.displayProbabilities(combinationProbabilities, f"Combination Probabilities for {combinationColumns}")

if __name__ == "__main__" :
    main()
