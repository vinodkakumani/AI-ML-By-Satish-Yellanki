import pandas as pd
from collections import Counter

class ProbabilityFrequencyDistribution :
    def __init__(self, inFilePath) :
        """Constructor To Initialize The Dataset File Path And Load Data."""
        self.inFilePath = inFilePath
        self.data = self.loadData()
    
    def loadData(self) :
        """Method To Load Dataset From The Given File Path With Exception Handling."""
        try :
            data = pd.read_excel(self.inFilePath)
            return data
        except FileNotFoundError as fileNotFound :
            print("Fatal Error! File Not Found. Please Check The File Path.")
        except Exception as exceptObject :
            print(f"Fatal Error! Error Loading The Data File: {exceptObject}")
        return None
    
    def calculateProbabilityDistribution(self, inColumnName) :
        """Method To Calculate Probability Frequency Distribution For A Given Column."""
        if self.data is None :
            print("Fatal Error! Required Data is Not Loaded.")
            return None
        
        try :
            outValues = self.data[inColumnName].tolist()
            freqCount = Counter(outValues)
            totalCount = sum(freqCount.values())
            probDistribution = {outKey : outValue / totalCount for outKey, outValue in freqCount.items()}
            return probDistribution
        except KeyError as keyError:
            print(f"Fatal Error! Column '{inColumnName}' Not Found in The Dataset.")
            return None
        except Exception as exceptObject :
            print(f"Fatal Error! Unexpected Error : {exceptObject}")
            return None
    
    def displayDistribution(self, inDistribution, inTitle) :
        """Method To Display Probability Frequency Distribution."""
        if inDistribution :
            print(f"\n{inTitle}:")
            print("Unique Value\tFrequency Distribution")
            for outKey, outValue in inDistribution.items() :
                print(f"{outKey}\t{outValue:.2f}")
        else :
            print(f"Fatal Error! Unable To Display {inTitle}.")


def main() :
    """Main Function To Execute The Probability Frequency Distribution Analysis."""
    inFilePath = "E:\\AIML2024\\Implementations\\001_Probability\\007_ProbabilityFrequencyDistribution\\DataSets\\CustomerHourlyVisits.xlsx"
    
    ProbFreqDistributionObject = ProbabilityFrequencyDistribution(inFilePath)
    
    visit_distribution = ProbFreqDistributionObject.calculateProbabilityDistribution("No. of Customers")
    ProbFreqDistributionObject.displayDistribution(visit_distribution, "Probability Frequency Distribution By Number of Customer Visits")
    
    categoryDistribution = ProbFreqDistributionObject.calculateProbabilityDistribution("Category")
    ProbFreqDistributionObject.displayDistribution(categoryDistribution, "Probability Frequency Distribution By Number of Sales Categories")
    
if __name__ == "__main__" :
    main()
