import pandas as pd

class TheoreticalProbability :
	def __init__(self, inFilePath) :
		self.inFilePath = inFilePath
		self.data = None
	
	def loadData(self) :
		"""Loads The Dataset From The Given File Path"""
		try :
			self.data = pd.read_excel(self.inFilePath)
			print("Data Loaded Successfully")
		except FileNotFoundError :
			print("Fatal Error! File Not Found At The Specified Path")
		except Exception as exceptObject :
			print(f"Fatal Error! Encountered Error While Loading Data{exceptObject}")
	
	def calculateProbability(self, inColumnName, inEventValue) :
		"""Method To Calculate The Theoretical Probability of an Event Occurring"""
		
		try :
			if self.data is None :
				raise ValueError("Fatal Error! Data Not Loaded. Please Load The Dataset First..")
			
			inTotalEvents = len(self.data)
			inFavorableEvents = len(self.data[self.data[inColumnName] == inEventValue])
			outProbability = inFavorableEvents / inTotalEvents if inTotalEvents > 0 else 0
			return round(outProbability, 4)
		except KeyError :
			print("Fatal Error!: Specified column does not exist in the dataset.")
		except Exception as exceptObject :
			print(f"Fatal Error! Encountered Error Calculating Theoretical Probability: {exceptObject}")
	
	def displayProbability(self, inColumnName, inEventValue) :
		"""Method To Display The Probability Result in a Readable Format"""
		outProbability = self.calculateProbability(inColumnName, inEventValue)
		if outProbability is not None :
			print(f"The Theoretical Probability of '{inEventValue}' in '{inColumnName}' is : {outProbability}")

def main() :
    inFilePath = "E:\\AIML2024\\Implementations\\001_Probability\\006_TheoreticalProbability\\DataSets\\CustomerPurchaseBehaviorAnalysis2024.xlsx"
    probabilityCalculator = TheoreticalProbability(inFilePath)
    
    probabilityCalculator.loadData()
    
    probabilityCalculator.displayProbability("Product Category", "Electronics")
    
    probabilityCalculator.displayProbability("Payment Method", "PayPal")
    
if __name__ == "__main__" :
    main()