import pandas as pd
import os
import matplotlib.pyplot as plt

class StudentScoresArithmentiMeanCalculator :
    """Class to calculate arithmetic mean of the student's examination scores"""
    def __init__(self, inFilePath, outFilePath) -> None:
        """Constructor to initialise the file path and load the data"""
        self.inFilePath = inFilePath
        self.outFilePath = outFilePath
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
    
    def showData(self):
        """
        Show the first 10 rows
        """
        try:
            if self.data is None:
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")
            
            print("\nDisplaying first 10 rows of data...")
            print(self.data.head(10))
        except Exception as oExcepObj:
            print("Error occurred while loading the data {oExcepObj}", end="\n")
            

    def displaySummary(self) :
        """
        Displays The Summary of The Loaded Dataset
        """
        try :
            if self.data is None :
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")

            print("\nDisplaying The Summary of The Loaded Dataset...", end = "\n")
            print(self.data.describe())
        except Exception as exceptionObject :
            raise Exception("\nHey! An Error Occured While Displaying The Dataset Summary : {exceptionObject}")
        
    def addGradeColumn(self):
        """
        Add Grade column to the dataset
        """
        try:            
            if self.data is None :
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")
            
            self.data["Grade"] = self.data["Score"].apply(lambda inScore: "A" if inScore >= 90 else "B+" if inScore >= 85 else "B" if inScore >=80 else "C+" if inScore >= 75 else "C")
            self.showData()
        except Exception as exceptionObject :
            raise Exception("\nHey! An Error Occured While Adding Grade Column to Dataset : {exceptionObject}")
        
    def calculateArithmeticMean(self):
        """
        Method to calclulate the arithmetic mean of the students score in Mathemetics
        """
        try: 
            if self.data is None:
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")

            # aritmeticMean = self.data["Score"].sum() / self.data["Score"].count()
            aritmeticMean = self.data["Score"].mean()
            print(f"Arithmeic Mean of the Students Score in Mathemtics is {aritmeticMean}")
        except Exception as exObj:
            raise Exception(f"\nHey! An Error Occured While Calculating Arithmethic Mean of the Students Score : {exObj}")

    def saveModifiedData(self):
        """
        Method to save the modified dataset
        """
        try:
            if self.data is None:
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")
            self.data.to_csv(self.outFilePath)
        except Exception as excpObj:
            raise Exception(f"\nHey! An Error Occured While Saving Modified Data : {excpObj}")
    
    def plotData(self):
        """
        Method to plot the data.
        """
        try:
            if self.data is None:
                raise ValueError(f"\nFatal Error! Dataset is Empty, Please Provide a Valid Dataset")
            """Plot to show the marks scored by students"""
            plt.figure(figsize=(12, 6))
            plt.bar(self.data["Student Name"], self.data["Score"], color="skyblue")
            plt.title("Students Performance in Mathematics Exam")
            plt.xlabel("Student Name")
            plt.ylabel("Score")
            plt.xticks(rotation = 45, ha = "right")
            plt.tight_layout()
            # Calculate and plot the arithmetic mean
            mean_score = self.data["Score"].mean()
            plt.axhline(y=mean_score, color='red', linestyle='--', label=f'Arithmetic Mean: {mean_score:.2f}')
            plt.legend()

            plt.show()  # Display the plot

            """Plot to show class participation vs score"""
            plt.figure(figsize=(12, 6))
            plt.scatter(self.data["Class Participation (%)"], self.data["Score"], color="red", alpha = 0.7)
            plt.title("Class Participarion Vs Scores")
            plt.xlabel("Class Participarion %")
            plt.ylabel("Score")
            plt.xticks(rotation = 45, ha = "right")
            plt.tight_layout()
            plt.grid(True)
            
            plt.show()  # Display the plot

            # Plot Arithmethic mean



        except Exception as excpObj:
            raise Exception(f"\nHey! An Error Occured While Plotting The Data : {excpObj}")

def main():
    try :
        """Main Function For Implementing The Solution"""
        inFilePath = r"/Users/vinodkakumani/git/vinodkakumani/AI-ML-By-Satish-Yellanki/4. Statistics/001_ArtithmeticMean/StudentsScores.csv"
        outFilePath = r"/Users/vinodkakumani/git/vinodkakumani/AI-ML-By-Satish-Yellanki/4. Statistics/001_ArtithmeticMean/StudentsScores_Output.csv"

        """Create StudentScoresArithmentiMeanCalculator Object"""
        calculator = StudentScoresArithmentiMeanCalculator(inFilePath, outFilePath)

        """Load the data"""
        calculator.loadData()
        calculator.showData()
        calculator.displaySummary()
        calculator.addGradeColumn()
        calculator.calculateArithmeticMean()
        calculator.saveModifiedData()
        calculator.plotData()
    except Exception as exceptionObj:
        print(f"Fatal error occurred while executing the solution {exceptionObj}", end="\n")


if __name__ == "__main__":
    main()