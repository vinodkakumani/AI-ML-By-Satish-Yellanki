#! python3

import pandas as pd
import numpy as np
import random
import traceback

class EquallyLikelyEventsProbabilityCalculator:
	
	def __init__(self, inFilePath) :
		try:
			self.filePath = inFilePath
			self.originalData = None
			self.rewardData = None
		except Exception as e:
			print(f"Error initializing calculator: {e}")
			raise

	def loadData(self) :
		try:
			self.originalData = pd.read_excel(self.filePath)
			self.rewardData = pd.read_excel(self.filePath, sheet_name='Rewards')
		except FileNotFoundError:
			print(f"File not found at path: {self.filePath}")
			raise
		except Exception as e:
			print(f"Error loading data: {e}")
			raise

	def displaySummary(self) :
		try:
			print(self.originalData.info())
			print(self.originalData.head())
			print(self.rewardData.info())
			print(self.rewardData.head())
		except Exception as e:
			print(f"Error displaying summary: {e}")
			raise

	def populateRewardsToCustomers(self) :
		try:
			reward_ids = self.rewardData['Reward ID'].values
			self.originalData['Reward ID'] = random.choices(reward_ids, k=len(self.originalData))
			# Merge the two dataframes on the 'Reward ID' column - Ref: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html#pandas.merge
			self.mergedData = pd.merge(self.originalData, self.rewardData, on='Reward ID', how='left')
			
			# This is the alternative way to populate the rewards to the customers
			# self.originalData['Reward'] = self.rewardData['Reward Type'].sample(
			# 		n=len(self.originalData),
			# 		replace=True
			# 	).values
			print(self.mergedData.columns)
			print(self.mergedData.info())
			print(self.mergedData.head(20))
		except Exception as e:
			print(f"Error populating rewards: {e}")
			raise

	def calculateProbabilityOfASpecificReward(self, inRewardType) :
		try:
			total_rewards = len(self.mergedData)
			specific_reward_count = len(self.mergedData[self.mergedData['Reward Type'] == inRewardType])
			return specific_reward_count / total_rewards
		except ZeroDivisionError:
			print("Error: No rewards data available")
			raise
		except Exception as e:
			print(f"Error calculating probability for {inRewardType}: {e}")
			raise

	def calculateProbabilityOfAllRewards(self) :
		try:
			unique_rewards = self.mergedData['Reward Type'].unique()
			probabilities = [self.calculateProbabilityOfASpecificReward(reward) for reward in unique_rewards]
			return dict(zip(unique_rewards, probabilities))
		except Exception as e:
			print(f"Error calculating probabilities for all rewards: {e}")
			raise

def main() :
	filePath = r"/Users/vinodkakumani/Library/CloudStorage/OneDrive-Personal/AI & ML By Satish Yellanki/3. Probability/CustomerRewards.xlsx"
	probabilityCalculatorObject = EquallyLikelyEventsProbabilityCalculator(filePath)

	try :
		probabilityCalculatorObject.loadData()
		probabilityCalculatorObject.displaySummary()
		probabilityCalculatorObject.populateRewardsToCustomers()
		print(probabilityCalculatorObject.calculateProbabilityOfASpecificReward('Bonus Points'))
		print(probabilityCalculatorObject.calculateProbabilityOfAllRewards())
	except Exception as exceptionObject :
		traceback.print_exc(exceptionObject)
		print(f"\nHey! An Error Occured While Processing The Data : {exceptionObject}")

if __name__ == "__main__" :
	main()
