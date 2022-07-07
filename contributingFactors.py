#Maya Anderson
#this program prints the three contributing factors for collisions
#on june 15th, 2016

import pandas as pd

inFile = input("Enter CSV file name: ")

csvFile = inFile
myFile = pd.read_csv(csvFile)

print("Top three contributing factors for collisions:")

print(myFile['CONTRIBUTING FACTOR VEHICLE 1'].value_counts()[:3])
