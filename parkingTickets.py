#Maya Anderson
#this program prints the given attribute from the user 

inFile = input("Enter file name: ")
attribute = input("Enter attribute: ")


import pandas as pd
csvFile = inFile
myFile = pd.read_csv(csvFile)
print("The 10 worst offenders are:")

print(myFile[attribute].value_counts()[:10])
