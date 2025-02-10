import os
import pandas as pd

class DisjointEventProbabilityCalculator :
	"""Constructor For Instantiating and Initializing The Required Object"""
	def __init__(self, inFilePath) :
		self.inFilePath = inFilePath
		self.data = None

	def loadData(self) :
		"""Method To Load The Data For Analysis"""
		try :
			self.data = pd.read_excel(self.inFilePath)
			if self.data.empty :
				raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")
			
			print(f"\nRetail Sales Analysis Data is Loaded Successfully From The File : {self.inFilePath}", end = "\n")
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

	def validateDataColumns(self, inRequiredColumns) :
		"""Validate Whether Required Columns For Analysis Are Present OR Not in The Loaded Dataset"""
		try :
			if self.data is None :
				raise ValueError(f"\nFatal Error! Data Not Loaded, Call The Proper Method For Loading The Data First...")
			
			missingColumns = [inColumns for inColumns in inRequiredColumns if inColumns not in self.data.columns]

			if missingColumns : 
				raise ValueError(f"\nFatal Error! Data Missing The Required Columns : {', '.join(missingColumns)}")
		except ValueError as valueErrorObject :
			print(f"\nFatal Error! Exception Occurred : {exceptObject}", end = "\n")
			raise
		except Exception as exceptObject :
			print(f"\nFatal Error! Error Validating The Data Columns : {exceptObject}", end = "\n")
			raise	
	
	def calculateProbabilities(self, inCategoryColumn) :
		"""Method To Calculate The Probability of The Dis-Joint Events"""
		try :
			self.validateDataColumns([inCategoryColumn])

			totalRecords = len(self.data)

			if totalRecords == 0 :
				raise ValueError(f"\nFatal Error! Data Not Loaded, Call The Proper Method For Loading The Data First...")
			
			categoryColumnCounts = self.data[inCategoryColumn].value_counts()

			categoryProbabilities = {
				category : count / totalRecords
				for category, count in categoryColumnCounts.items()
			}

			totalProbability = sum(categoryProbabilities.values())

			print(f"\nThe Category Probabilities : ")
			for category, probability in categoryProbabilities.items() :
				print(f"\n{category} : {probability : .2f}", end = "\n")
		except Exception as exceptObject :
			print(f"\nFatal Error! Error Calculating The Probabilities : {exceptObject}", end = "\n")
			raise	

    def add_analysis_column(self, new_column_name, calculation_function):
        """Adds a new column to the dataset based on a calculation function."""
        try:
            if self.data is None:
                raise ValueError("No data loaded. Please load the dataset first.")

            self.data[new_column_name] = self.data.apply(calculation_function, axis=1)
            print(f"New column '{new_column_name}' added successfully.")

        except Exception as e:
            print(f"Error adding new column: {e}")

    def show_modified_data(self):
        """Displays the modified dataset with new columns."""
        if self.data is None:
            print("No data loaded. Please load the dataset first.")
            return
        print("Modified Dataset:")
        print(self.data)

def main() :
	"""Main Function For Imlementing The Solution"""
	filePath = r"E:\AIML2024\Implementations\001_Probability\DataSets\RetailSalesTransactionsDataset.xlsx"

	try :
		"""Creating The Object Instance For The Weather Forecasting Sure Outcome Event Class"""
		disJointEventObject = DisjointEventProbabilityCalculator(filePath)

		disJointEventObject.loadData()
		disJointEventObject.showData()

		categoryColumn = "Category"

		disJointEventObject.calculateProbabilities(categoryColumn)

	except Exception as exceptObject :
		print(f"\nFatal Error! An Error Encountered While Executing The Application : {exceptObject}", end = "\n")
	
if __name__ == "__main__" :
	main()