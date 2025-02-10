import pandas as pd

class ProbabilityAnalysis :
    
    def __init__(self, inFilePath) :
        self.inFilePath = inFilePath
        self.data = None
    
    def loadData(self) :
        try :
            self.data = pd.read_excel(self.inFilePath)
            
            if 'Complaint ID' not in self.data.columns or 'Response Time (seconds)' not in self.data.columns :
                raise ValueError("Required Columns ('Complaint ID', 'Response Time (seconds)') are Missing.")
            
            print("Data Loaded Successfully.")
        except FileNotFoundError :
            print(f"Fatal Error : The File At {self.inFilePath} Does Not Exist.")
        except ValueError as exceptObject :
            print(f"Fatal Error : {exceptObject}")
        except Exception as exceptObject :
            print(f"Fatal Error!! An Unexpected Error Occurred : {exceptObject}")
    
    def displayOriginalData(self) :
        if self.data is not None :
            print("Original Data : ")
            print(self.data.head())
        else :
            print("Data Not Loaded. Please Load The Data First.")
    
    def categorizeResponseTime(self) :
        if self.data is not None :
            self.data['Category'] = self.data['Response Time (seconds)'].apply(
                lambda x: '<30 seconds' if x < 30 else ('30-60 seconds' if x <= 60 else '>60 seconds')
            )
            print("Response Times Categorized Successfully.")
        else :
            print("Data Not Loaded. Please Load The Data First.")
    
    def countCategories(self) :
        if self.data is not None :
            outCounts = self.data['Category'].value_counts()
            print("Category Counts : ")
            print(outCounts)
            return outCounts
        else :
            print("Data Not Loaded. Please Load The Data First.")
            return None
    
    def calculateProbabilities(self) :
        if self.data is not None :
            outCounts = self.countCategories()
            if outCounts is not None :
                totalRecords = len(self.data)
                probabilities = outCounts / totalRecords
                print("Calculated Probabilities:")
                print(probabilities)
                return probabilities
            else :
                print("Unable To Calculate Probabilities as Outcounts Are Missing.")
        else :
            print("Data Not Loaded. Please Load The Data First.")
            return None
    
    def saveModifiedData(self, inSavePath) :
        if self.data is not None :
            try :
                self.data.to_excel(inSavePath, index = False)
                print(f"Modified Data Saved To {inSavePath}")
            except Exception as exceptObject :
                print(f"Error Saving Data : {exceptObject}")
        else :
            print("Data Not Loaded. Please Load The Data First.")
    
    def displayModifiedData(self) :
        if self.data is not None :
            print("Modified Data with Additional Columns : ")
            print(self.data.head())
        else :
            print("Data Not Loaded. Please Load The Data First.")

def main() :
    inFilePath = r"E:\AIML2024\Implementations\001_Probability\004_TrialInProbability\DataSets\ComplaintsAnalysis.xlsx"
    
    trialsProbabilityCalculator = ProbabilityAnalysis(inFilePath)
    
    trialsProbabilityCalculator.loadData()
    
    trialsProbabilityCalculator.displayOriginalData()
    
    trialsProbabilityCalculator.categorizeResponseTime()
    
    trialsProbabilityCalculator.countCategories()
    
    trialsProbabilityCalculator.calculateProbabilities()
    
    #inSavePath = r"E:\AIML2024\Implementations\001_Probability\004_TrialInProbability\DataSets\Modified_ComplaintsAnalysis.xlsx"
    #trialsProbabilityCalculator.saveModifiedData(inSavePath)
    
    #trialsProbabilityCalculator.displayModifiedData()

if __name__ == "__main__" :
    main()
