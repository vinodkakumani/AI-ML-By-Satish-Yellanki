import os
import pandas as pd

class SureOutcomeEventCalculator :
	"""Constructor For Instantiating and Initializing The Required Object"""
	def __init__(self, inFilePath, sheetName = "WeatherInfo") :
		self.inFilePath = inFilePath
		self.sheetName = sheetName
		self.data = None

	def loadData(self) :
		"""Method To Load The Data For Analysis"""
		try :
			if not os.path.exists(self.inFilePath) :
				raise FileNotFoundError(f"\nFatal Error! The Requested File is Not Found : {self.inFilePath}")
			
			self.data = pd.read_excel(self.inFilePath)
			if self.data.empty :
				raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")
			
			print(f"\nWeather Forecasting Data is Loaded Successfully From The File : {self.inFilePath}", end = "\n")
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
			
			print(f"\nDisplaying The Original Dataset, as Extracted For The File System..\n.", end = "\n")
			print(self.data)
		except Exception as exceptObject :
			print(f"\nFatal Error! Error Displaying The Data : {exceptObject}", end = "\n")
			raise
	
	def addSureOutcomeColumn(self) :
		"""Method To Add 'Sure Outcome (Always Y)' Column To The Existing Dataset With All Values Set To 'Y'"""
		try : 
			self.data["Sure Outcome (Always Y)"] = "Y"
			print(f"\n'Sure Outcome (Always Y)' Column Added Successfully...\n", end = "\n")
		except Exception as exceptObject :
			print(f"\nFatal Error! An Error Occurred While Adding The Column : {exceptObject}", end = "\n")
			raise		
	
	def saveModifiedDataset(self, outFilePath) :
		"""Method To Save The Modified Dataset With Added Columns"""
		try :
			self.data.to_excel(outFilePath, index = False)
			print(f"\nModified Dataset Saved Successfully To The Path : {outFilePath}", end = "\n")
		except Exception as exceptObject :
			print(f"\nFatal Error! An Error Occurred While Saving The Modified File: {exceptObject}", end = "\n")
			raise		
	
	def calculateProbabilities(self, columnName, value = "Y") : 
		"""Method To Calculate The Required Probabilities"""
		try :
			if columnName not in self.data.columns :
				raise ValueError(f"\nThe Given Column '{columnName}' Doesnot Exist in The Loaded Dataset...\n")
			
			totalRecords = len(self.data)
			eventCount = self.data[columnName].value_counts().get(value, 0)

			if totalRecords == 0 :
				raise ZeroDivisionError(f"\nThe Dataset is Empty, Cannot Calculate The Required Probabilities...")
			
			outProbability = eventCount / totalRecords
			return outProbability
		except Exception as exceptObject :
			print(f"\nFatal Error! An Error Occurred While Calculating The Probability {exceptObject}", end = "\n")
			raise	

def main() :
	"""Main Function For Imlementing The Solution"""
	filePath = r"E:\AIML2024\Implementations\001_Probability\DataSets\WeatherPredictions.xlsx"
	outModifiedFile = r"E:\AIML2024\Implementations\001_Probability\DataSets\WeatherPredictionsModified.xlsx"

	try :
		"""Creating The Object Instance For The Weather Forecasting Sure Outcome Event Class"""
		sureOutcomeEventObject = SureOutcomeEventCalculator(filePath)

		sureOutcomeEventObject.loadData()
		sureOutcomeEventObject.showData()
		sureOutcomeEventObject.addSureOutcomeColumn()
		sureOutcomeEventObject.showData()
		sureOutcomeEventObject.saveModifiedDataset(outModifiedFile)

		sureOutComeProbability = sureOutcomeEventObject.calculateProbabilities("Sure Outcome (Always Y)")
		print(f"\nThe Probability of The Sure Outcome Event is : {sureOutComeProbability : .2f}\n", end = "\n")

		sunnyEventProbability = sureOutcomeEventObject.calculateProbabilities("Is it Sunny? (Y/N)", value = "Y")
		print(f"\nThe Probability of The Sunny days is : {sunnyEventProbability : .2f}\n", end = "\n")

	except Exception as exceptObject :
		print(f"\nFatal Error! An Error Encountered While Executing The Application : {exceptObject}", end = "\n")
	
if __name__ == "__main__" :
	main()