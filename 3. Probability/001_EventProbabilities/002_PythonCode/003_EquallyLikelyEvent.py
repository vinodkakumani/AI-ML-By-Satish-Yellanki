#pip install openpyxl
import pandas as pd
import os
import random

class RewardsProbabilityCalculator :
	def __init__(self, inFilePath) :
		"""Constructor To Initialize and Instantiate The Object of Class RewardsProbabilityCalculator, Supplied With The Given Dataset File Path"""
		self.inFilePath = inFilePath
		self.customerData = None
		self.rewardsData = None

	def loadData(self, customerInfoSheet, rewardsSheet) :
		"""Method To Load The Data From The Specified Sheets Existing in The Excel File"""
		try :
			if not os.path.exists(self.inFilePath) :
				raise FileNotFoundError(f"\nHey! Fatal Error, File Not Found At The Specified Path : {self.inFilePath}")
			
			self.customerData = pd.read_excel(self.inFilePath, sheet_name = customerInfoSheet)
			self.rewardsData = pd.read_excel(self.inFilePath, sheet_name = rewardsSheet)

			print(f"\nData Loaded Successfully From The Supplied Sheets '{customerInfoSheet}' And '{rewardsSheet}'.", end = "\n")
		except FileNotFoundError as fnfError :
			print(fnfError)
		except Exception as excepObject :
			print(f"\nSorry! Fatal Error Occured While Loading The Data : {excepObject}", end = "\n")

	def displayLoadedData(self) :
		"""Method To Display The Few Records From The Loaded Data From The Supplied Sheets For Verification"""
		try :
			if self.customerData is not None :
				print(f"\nCustomer Data Preview...", end = "\n")
				print(self.customerData.head(), end = "\n")
			else :
				print(f"\nCustomer Data is Not Loaded...Cross Verify The Data Load and Debug...", end = "\n")
			
			if self.rewardsData is not None :
				print(f"\nRewards Data Preview...", end = "\n")
				print(self.rewardsData.head(), end = "\n")
			else :
				print(f"\nRewards Data is Not Loaded...Cross Verify The Data Load and Debug...", end = "\n")
		except Exception as excepObject :
			print(f"\nSorry! Fatal Error Occured While Displaying The Data : {excepObject}", end = "\n")

	def assignRewardsRandomly(self) :
		"""Method To Assign Rewards Randomly To The Customers And Ensure That The Merged Data Includes Reward Details"""
		try :
			if self.customerData is None or self.rewardsData is None :
				raise ValueError(f"\nSorry! Data Not Loaded, Please Load The Data First, And Then Try Allocating The Rewards To The Customer")
			
			"""Debug Statements : Printing The Columns of Both The Data Sets"""
			print(f"\nCustomer Data Columns : {self.customerData.columns.tolist()}", end = "\n")
			print(f"\nRewards Data Columns : {self.rewardsData.columns.tolist()}", end = "\n")

			"""Routine For Generating Random Rewards For Each Identified Customer"""
			rewardIDs = self.rewardsData["Reward ID"].tolist()
			self.customerData["Reward ID"] = [
								random.choice(rewardIDs) for _ in range(len(self.customerData))
						]
			
			"""Merging The Customer Data With Rewards Data To Include The Reward Names"""
			mergedData = pd.merge(self.customerData, self.rewardsData, on = "Reward ID", how = "left")

			"""Debug Statements : Printing The Columns After Merging The Data"""
			print(f"\nMerged Data Columns : {mergedData.columns.tolist()}", end = "\n")

			if "Reward Type" not in mergedData.columns :
				raise KeyError("\n'Reward Type' Column is Missing in The Merged Data Set. Verify Your Rewards Data.")
			
			print("\nRewards Successfully Assigned To The Customers Randomly...", end = "\n")
			return mergedData
		
		except KeyError as keyErrorObject :
			print(f"\nKey Error Encountered : {keyErrorObject}", end = "\n")
		except Exception as exepObject :
			print(f"\nAn Error Encountered While Assigning The Rewards To Customers : {exepObject}", end = "\n")

	def calculateProbabilityForAllRewards(self, inData) :
		"""Method For Calculating The Probability For Equally Likey Event For Rwards Allocation To ustomers"""
		try :
			if inData is None :
				raise ValueError("\nSorry! No Data To Display...")
			
			"""Capturing The Count For The Total Number of Customers"""
			totalCustomers = len(inData)

			"""Calculating The Probability For Each Reward Type"""
			rewardProbabilities = {}
			rewardTypes = inData["Reward Type"].unique()

			for rewardType in rewardTypes :
				rewardCount = inData[inData["Reward Type"] == rewardType].shape[0]
				outProbability = rewardCount / totalCustomers
				rewardProbabilities[rewardType] = outProbability
				print(f"\nThe Probability of Receiving '{rewardType}' is : {outProbability :.4f}", end = "\n")
			
			return rewardProbabilities
		except ValueError as valueErrorObject :
			print(f"\nProcess Returned : {valueErrorObject}", end = "\n")
		except Exception as exceptObject :
			print(f"\nAn Error Occured While Calculating The Probabilities For All Rewards : {exceptObject}", end = "\n") 

	def calculateRewardProbability(self, inData, inRewardType) :
		pass

	def displayAllCustomers(self, inData) :
		"""Method To Display All The Customers Information With The Assigned Rewards"""
		try :
			if inData is None :
				raise ValueError("\nSorry! No Data To Display...")
			
			print("\nDisplaying The Information of All The Customers With Assigned Rewards...", end = "\n")
			print(inData)
		except ValueError as valueErrorObject :
			print(f"\nProcess Returned : {valueErrorObject}", end = "\n")
		except Exception as exceptObject :
			print(f"\nAn Error Occured While Displaing The Data : {exceptObject}", end = "\n")

def main() :
	filePath = r"E:\AIML2024\Implementations\001_Probability\DataSets\CustomerRewards.xlsx"
	customerSheet = "CustomerInfo"
	rewardsSheet = "Rewards"

	try :
		"""Instantiating The Object of The Class RewardsProbabilityCalculator"""
		rewardsCalculator = RewardsProbabilityCalculator(filePath)

		"""Calling The Routine For Data Loading Process into The Instantiated Object"""
		rewardsCalculator.loadData(customerSheet, rewardsSheet)

		"""Calling The Routine For Displaying The Loaded Data, For Verification"""
		rewardsCalculator.displayLoadedData()

		"""Calling The Method For Randomly Assigning The Rewards To Customers and Merge The Rewards Data"""
		randomRewardsData = rewardsCalculator.assignRewardsRandomly()
		if randomRewardsData is not None :
			rewardsCalculator.displayAllCustomers(randomRewardsData)

			"""Calculate The Probability For All The Rewards Assigned To The Customer"""
			rewardsCalculator.calculateProbabilityForAllRewards(randomRewardsData)
	
	except Exception as excepObject :
		print(f"\nSorry! Fatal Error Occured While Displaying The Data : {excepObject}", end = "\n")

if __name__ == "__main__" :
	main()