import os
import pandas as pd

class FinancialAnalysis :
	"""Constructor For Instantiating and Initializing The Required Object"""
	def __init__(self, inFilePath) :
		self.inFilePath = inFilePath
		self.data = None
	
	def validateDataFile(self) :
		"""Method To Validate The Required Dataset File is Existing and it is in Correct Format"""
		try :
			if not os.path.exists(self.inFilePath) :
				raise FileNotFoundError(f"\nFatal Error! The Requested File is Not Found : {self.inFilePath}\n")
		
			if not self.inFilePath.endswith('.xlsx') :
				raise ValueError(f"\nFatal Error! The File To be Analyzed Should Be Only An Excel File With .xlsx Extension\n")
		except FileNotFoundError as fnfObject :
			print(f"\nFatal Error! File Not Found : {fnfObject}", end = "\n")
			raise
		except ValueError as valueErrorObject :
			print(f"\nFatal Error! Error Encountered in Validating The Correct File Extension : {valueErrorObject}", end = "\n")
			raise
		except Exception as exceptObject :
			print(f"\nFatal Error! Error Encountered in Validating The File Existence and File Formatting  : {exceptObject}", end = "\n")
			raise

	def loadData(self) :
		"""Method To Load The Data For Analysis"""
		try :
			self.data = pd.read_excel(self.inFilePath)
			if self.data.empty :
				raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")
			
			print(f"\nFinancial Analysis Data is Loaded Successfully From The File : {self.inFilePath}", end = "\n")
		except FileNotFoundError as fnfObject :
			print(f"\nFatal Error! File Not Found : {fnfObject}", end = "\n")
			raise
		except Exception as exceptObject :
			print(f"\nFatal Error! Error Encountered in Loading The Data : {exceptObject}", end = "\n")
			raise

	def showData(self) :
		"""Method To Show The Original Data as is"""
		try :
			if self.data is None :
				raise ValueError(f"\nFatal Error! Data Not Loaded, Call The Proper Method For Loading The Data First...")
			
			print(f"\nDisplaying The Original Dataset, as Extracted For The File System...\n", end = "\n")
			print(self.data)
		except Exception as exceptObject :
			print(f"\nFatal Error! Error Displaying The Data : {exceptObject}", end = "\n")
			raise
	
	def addAnalysisColumns(self) :
		"""Method To Add The Required Analysis Columns as Recommended By The Financila Consultant"""
		if self.data is None :
			raise ValueError(f"\nFatal Error! Data Not Loaded, Call The Proper Method For Loading The Data First...")

		try :
			"""Adding The Column For Representing The Growth Rate (%), If The Corresponding Column is Not Present in The Original Dataset"""
			if 'Growth Rate (%)' not in self.data.columns :
				self.data['Growth Rate (%)'] = 0
			
			"""Adding The Column For Representing The Market Adjustment Factor, If The Corresponding Column is Not Present in The Original Dataset"""
			if 'Market Adjustment Factor' not in self.data.columns :
				self.data['Market Adjustment Factor'] = 1.0
			
			"""Adding The Column For Representing The Predicted Revenue ($ Million), If The Corresponding Column is Not Present in The Original Dataset"""
			if 'Predicted Revenue ($ Million)' not in self.data.columns :
				self.data['Predicted Revenue ($ Million)'] =  (
					self.data['Revenue ($ Million)'] + (self.data['Revenue ($ Million)'] * self.data['Growth Rate (%)'] / 100 * self.data['Market Adjustment Factor'])
					)

			"""Adding The Column For Representing Impossible Events, If The Corresponding Column is Not Present in The Original Dataset"""
			if 'Impossible Events' not in self.data.columns :
				self.data['Impossible Events'] =  self.data['Predicted Revenue ($ Million)'] > 0
			
			print(f"\nThe Required Analysis Columns Are Added Successfully...\n", end = "\n")
			self.showData()
		except KeyError as keyErrorObject :
			raise KeyError(f"\nFatal Error! Missing The Essential Column in The Loaded Dataset...\n")
		except Exception as exceptObject :
			print(f"\nFatal Error! Error While Adding The Columns For Analysis : {exceptObject}", end = "\n")
			raise
	
	def calculateProbability(self):
		"""Method To Calculate The Probability of Sure Outcome of Events."""
		
		if self.data is None :
			raise Exception(f"\nFatal Error! Data is Not Loaded. Please Load The Data First.")
		
		try :
			totalEvents = len(self.data)
			impossibleEvents = self.data['Impossible Events'].sum()
			outProbability = impossibleEvents / totalEvents if totalEvents > 0 else 0
		
			print(f"\nProbability of Impossible Events : {outProbability}", end="\n")
			return outProbability
	
		except Exception as exceptObject :
			print(f"\nFatal Error! Error While Calculating Probabilities : {exceptObject}", end="\n")
			raise
 
def main() :
	"""Main Function For Imlementing The Solution"""
	filePath = r"E:\AIML2024\Implementations\001_Probability\DataSets\FinancialForecastAndImpossibilityAnalysisDataset.xlsx"

	try :
		"""Creating The Object Instance For The Weather Forecasting Sure Outcome Event Class"""
		financialAnalysisObject = FinancialAnalysis(filePath)

		financialAnalysisObject.validateDataFile()
		financialAnalysisObject.loadData()
		financialAnalysisObject.showData()
		financialAnalysisObject.addAnalysisColumns()
		financialAnalysisObject.calculateProbability()

	except Exception as exceptObject :
		print(f"\nFatal Error! An Error Encountered While Executing The Application : {exceptObject}", end = "\n")
	
if __name__ == "__main__" :
	main()