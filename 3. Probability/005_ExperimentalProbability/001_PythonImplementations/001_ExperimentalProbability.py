import pandas as pd

class ExperimentalProbability :
    def __init__(self, inFilePath) :
        """Constructor To Initialize The File Path And Load The Dataset."""
        self.inFilePath = inFilePath
        self.data = None

    def load_data(self) :
        """Loads The Dataset From The Specified Excel File."""
        try :
            self.data = pd.read_excel(self.inFilePath)
            print("Dataset Loaded Successfully.")
        except FileNotFoundError :
            raise Exception(f"File Not Found at {self.inFilePath}. Please Check The Path.")
        except Exception as exceptObject :
            raise Exception(f"An Error Occurred While Loading The File : {str(exceptObject)}")

    def calculate_probability(self) :
        """Calculates The Experimental Probabilities of Defective And Non-Defective Products."""
        try :
            if self.data is None :
                raise Exception("Data Not Loaded. Please Load The Dataset First.")

            totalTrials = len(self.data)
            defectiveCount = self.data[self.data['Outcome'] == 'Defective'].shape[0]
            nonDefectiveCount = self.data[self.data['Outcome'] == 'Non-Defective'].shape[0]

            # Calculate probabilities
            defective_probability = (defectiveCount / totalTrials) * 100
            non_defective_probability = (nonDefectiveCount / totalTrials) * 100

            return {
                "Defective": {
                    "Count": defectiveCount,
                    "Probability": defective_probability
                },
                "Non-Defective": {
                    "Count": nonDefectiveCount,
                    "Probability": non_defective_probability
                }
            }
        except ZeroDivisionError :
            raise Exception("The Dataset Contains No Records. Cannot Calculate Probabilities.")
        except KeyError :
            raise Exception("The Required 'Outcome' Column is Missing in The Dataset.")
        except Exception as exceptObject :
            raise Exception(f"An Error Occurred During Probability Calculation : {str(exceptObject)}")

    def displayResults(self, inResults) :
        """Displays The Results in A Formatted Way."""
        try :
            print("\nExperimental Probability Results : ")
            print(f"Total Trials : {inResults['Defective']['Count'] + inResults['Non-Defective']['Count']}")
            print(f"Defective : {inResults['Defective']['Count']} trials, Probability : {inResults['Defective']['Probability'] :.2f}%")
            print(f"Non-Defective : {inResults['Non-Defective']['Count']} trials, Probability: {inResults['Non-Defective']['Probability'] :.2f}%")
        except Exception as exceptObject :
            raise Exception(f"An error occurred while displaying the inResults: {str(exceptObject)}")

def main() :
    """Main function to execute the program."""
    try:
        inFilePath = r"E:\\AIML2024\\Implementations\\001_Probability\\005_ExperimentalProbability\\001_ExcelImplementations\\001_ExperimentalProbability.xlsx"
        experimentalProbabilityObject = ExperimentalProbability(inFilePath)

        experimentalProbabilityObject.load_data()

        inResults = experimentalProbabilityObject.calculate_probability()

        experimentalProbabilityObject.displayResults(inResults)

    except Exception as exceptObject:
        print(f"Fatal Error : {str(exceptObject)}")

if __name__ == "__main__" :
    main()
