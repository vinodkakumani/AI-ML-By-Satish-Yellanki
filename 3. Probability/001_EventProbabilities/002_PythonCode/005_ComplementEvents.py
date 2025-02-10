import os
import pandas as pd

class SalesProbabilitityCalculator :
	"""Constructor For Instantiating and Initializing The Required Object"""
	def __init__(self, inFilePath) :
		self.inFilePath = inFilePath
		self.data = None

	def loadData(self) :
		"""Method To Load The Data For Analysis"""
		try :
			if not os.path.exists(self.inFilePath) :
				raise FileNotFoundError(f"\nFatal Error! The Requested File is Not Found : {self.inFilePath}")
			
			self.data = pd.read_excel(self.inFilePath)
			if self.data.empty :
				raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")
			
			print(f"\nSales Data is Loaded Successfully...", end = "\n")
		except Exception as exceptObject :
			print(f"\nFatal Error! Error Encountered in Loading The Data : {exceptObject}", end = "\n")
			raise
			
	def showOriginalData(self) :
		"""Method To Show The Original Data as is"""
		try :
			if self.data is None :
				raise ValueError(f"\nFatal Error! Data Not Loaded, Call The Proper Method For Loading The Data First...")
			
			print(f"\nDisplaying The Original Dataset, as Extracted For The File System...", end = "\n")
			print(self.data)
		except Exception as exceptObject :
			print(f"\nFatal Error! Error Displaying The Data : {exceptObject}", end = "\n")
			raise
	
	def calculateDiscountedSales(self) :
		"""Method To Calculate The Discounted Sales"""
		try :
			if self.data is None :
				raise ValueError(f"\nFatal Error! Data Not Loaded, Call The Proper Method For Loading The Data First...")
			
			self.data['Discounted Sales Amount ($)'] = self.data['Sales Amount ($)'] - (self.data['Sales Amount ($)'] * self.data['Discount Applied (%)'] / 100)

			print(f"\nDiscounted Sales Amount Calculated Successfully!", end = "\n")
		except Exception as exceptObject :
			print(f"\nFatal Error! Error Calculating The Discounted Sales : {exceptObject}", end = "\n")
			raise
	
	def classifyEvents(self) :
		"""Method To Classify The Events Based on a Condition"""
		try : 
			if self.data is None :
				raise ValueError(f"\nFatal Error! Data Not Loaded, Call The Proper Method For Loading The Data First...")
			
			self.data['Event (> $500)'] = self.data['Discounted Sales Amount ($)'].apply(lambda eventState : 'Yes' if eventState > 500 else 'No')

			print(f"\nEvent Classification Completed Successfully!", end = "\n")
		except Exception as exceptObject :
			print(f"\nFatal Error! Error in Classifying The Events : {exceptObject}", end = "\n")
			raise
	
	def calculateProbabilities(self) :
		"""Method To Calculate Probabilities For Their Events and Complements"""
		try :
			if self.data is None or 'Event (> $500)' not in self.data.columns :
				raise ValueError("Fatal Error! Event Classification is Not Performed. Implement Event Classification First")
			
			totalRecords = len(self.data)
			eventYes = len(self.data[self.data['Event (> $500)'] == 'Yes'])
			eventNo = len(self.data[self.data['Event (> $500)'] == 'No'])
			
			probabilityEventYes = eventYes / totalRecords
			probabilityEventNo = eventNo / totalRecords
			
			return {
				"P(Event > $500)" : probabilityEventYes,
				"P(Event <= $500)" : probabilityEventNo
			}
		
		except Exception as exceptObject :
			print(f"Fatal Error! Error Calculating Probabilities: {exceptObject}")
			raise
	
	def displayResults(self) :
		"""Method To Display The Probability Results Along With The Appended Columns"""
		try :
			print(f"\nDisplaying The Updated Sales Dataset With Applied New Columns...\n", end = "\n")
			print(self.data)
			totalrecords = len(self.data)
			print(f"\nTotal Records in The Dataset Are : {totalrecords}\n", end = "\n")
			
			eventProbabilities = self.calculateProbabilities()
			print(f"\nDisplaying The Calculated Probabilities of The Events\n")
			
			for event, probability in eventProbabilities.items() :
				print(f"\n{event} : {probability : .2f}")
		
		except Exception as exceptObject :
			print(f"\nFatal Error! Error in Displaying The Results : {exceptObject}", end = "\n")
			raise	

def main() :
	"""Main Function For Imlementing The Solution"""
	filePath = r"E:\AIML2024\Implementations\001_Probability\DataSets\SalesSystemData.xlsx"

	try :
		"""Creating The Object Instance For The Sales Probabilitity Calculator Class"""
		salesProbabilitityCalculator = SalesProbabilitityCalculator(filePath)

		salesProbabilitityCalculator.loadData()
		salesProbabilitityCalculator.showOriginalData()
		salesProbabilitityCalculator.calculateDiscountedSales()
		salesProbabilitityCalculator.classifyEvents()
		salesProbabilitityCalculator.displayResults()

	except Exception as exceptObject :
		print(f"\nFatal Error! An Error Encountered While Executing The Application : {exceptObject}", end = "\n")
	
if __name__ == "__main__" :
	main()