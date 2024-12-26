#! python3

import pandas as pd
import os
os.system("cls")

class ProbabilityCalculator :
	def __init__(self, inFilePath) :
		"""Here We Are Initializing The Probability Calculator With Required Dataset"""
		self.inFilePath = inFilePath
		self.data = None
	
	def loadData(self) :
		"""Loads The Dataset From The Given Path"""
		try :
			self.data = pd.read_csv(self.inFilePath)
			print(f"\nDataset Loaded Successfully...", end = "\n")
		except FileNotFoundError as fileNotFoundObject :
			print("\nHey! Encounterd an Exception, Exception Stack is : {fileNotFoundObject}", end = "\n")
			raise Exception(f"\nFile Not Found at : {self.inFilePath}. Please Crosss Verify The Path...")
		except Exception as exceptionObject :
			raise Exception(f"\nAn Error Occured While Loading The Dataset : {exceptionObject}")
		
	def calculateEventProbability(self, inCondition) :
		"""
		Calculates The Probability of a Specific Event
		inCondition is a Parameter That is Passed Through The Lambda Function in The Calling Environment
		This Function Returns The Value of The "Probability Event" Through The return Statement
		"""

		try :
			if self.data is None :
				raise Exception("\nHey! Data is Not Loaded, Please Load The Dataset First")
			
			eventCount = len(self.data[inCondition(self.data)])
			totalCount = len(self.data)
			outProbability = eventCount / totalCount
			return outProbability
		except Exception as exceptionObject :
			raise Exception("\nHey! An Error Occured While Calculating Event Probability : {exceptionObject}")
	
	def calculateIntersectionProbability(self, inCondition01, inCondition02) :
		"""
		Calculate The Probability of Compound Event, i.e. Intersection of Two Events
		inCondition01 is a Parameter That is Passed Through The Lambda Function in The Calling Environment
		inCondition02 is a Parameter That is Passed Through The Lambda Function in The Calling Environment
		This Function Returns The Value of The "Probability of Compound Event" Through The return Statement
		"""
		try :
			if self.data is None :
				raise Exception("\nHey! Data is Not Loaded, Please Load The Dataset First")
			
			intersectionCount = len(self.data[inCondition01(self.data) & inCondition02(self.data)])
			totalCount = len(self.data)
			outProbability = intersectionCount / totalCount
			return outProbability		
		except Exception as exceptionObject :
			raise Exception("\nHey! An Error Occured While Calculating Intersection Probability : {exceptionObject}")

	def displaySummary(self) :
		"""
		Displays The Summary of The Loaded Dataset
		"""
		try :
			if self.data is None :
				raise Exception("\nHey! Data is Not Loaded, Please Load The Dataset First")

			print("\nDisplaying The Summary of The Loaded Dataset...", end = "\n")
			print(self.data.describe())
		except Exception as exceptionObject :
			raise Exception("\nHey! An Error Occured While Displaying The Dataset Summary : {exceptionObject}")

def main() :
	"""Creating The Required String Object To manage The File Path"""
	inFilePath = r"E://AIML2024//Implementations//001_Probability//DataSets//SportsEventsAndParticipants.csv"

	"""Creating The Probability Calculator Object Using The ProbabilityCalculator() Class"""
	probabilityCalculatorObject = ProbabilityCalculator(inFilePath)

	try : 
		"""Loading The Data For Analysis into The probabilityCalculatorObject Instance"""
		probabilityCalculatorObject.loadData()

		"""Displaying The Summary of The Loaded Dataset"""
		probabilityCalculatorObject.displaySummary()

		"""Calculating The Probability of Event A P(A) : Probability of Sportsmen Registered For Given Sport By The End User"""
		inSportValue = input("\nPlease Give The Name of The Required Sport : ")
		probabilityGivenSport = probabilityCalculatorObject.calculateEventProbability(lambda df : df["Sport"] == inSportValue)
		print(f"\nThe Probability of The Sport Event {inSportValue} is : {probabilityGivenSport :.2f}")

		"""Calculating The Probability of Event B P(B) : Probability of Sportsmen Registered Greater Than The Given Age By The End User"""
		inAgeValue = int(input("\nPlease Give The Age of The Sports Man : "))
		probabilityGreaterAge = probabilityCalculatorObject.calculateEventProbability(lambda df : df["Age"] > inAgeValue)
		print(f"\nThe Probability of The Sports Men Above The Age of {probabilityGreaterAge} Years is : {probabilityGreaterAge :.2f}")

		"""Calculating The Probability of Compound Event P(A ∩ B) : Probability of Sportsmen Registered For The Given Sport and Also Having Age Greater Than The Given Age By The End User"""
		probabilitySportAndGreaterAge = probabilityCalculatorObject.calculateIntersectionProbability(lambda df : df["Sport"] == inSportValue, lambda df : df["Age"] > inAgeValue)
		print(f"\nThe Probability of The Compound Event P({inSportValue} ∩ Age > {inAgeValue}) is : {probabilitySportAndGreaterAge : .2f}")
	except Exception as exceptionObject :
		print(f"\nHey! Encountered Exception : {exceptionObject}")

if __name__ == "__main__" :
	main()