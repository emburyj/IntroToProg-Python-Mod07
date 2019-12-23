# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Demo of pickling and error handling
# ChangeLog (Who,When,What):
# JEmbury, 12/1/19,Created started script
# ------------------------------------------------------------------------ #

import pickle
# Data
shopping_list = []
FileName = "AppData.dat"

# Get info from user and save to list. Display input.
print("How much money can you spend on Christmas gifts?")
#try:
    # Get info from user
name_str = str(input("Enter a name on your shopping list: "))
budget_int = int(input("Enter a budget for this person($): "))

# Save to list and print back to user
shopping_list = [name_str, budget_int]
print(shopping_list)

# Store Data to binary file, begin pickling
objFile = open(FileName, "ab")
pickle.dump(shopping_list, objFile)
objFile.close()

    # Read data from binary file
objFile = open(FileName, "rb")
objFileData = pickle.load(objFile)
objFile.close()
print(objFileData)
# except ValueError as e:
#     print("Value entered for budget must be an integer!")
#     print("Built-In Python error info: ")
#     print(e,e.__doc__, type(e), sep='\n')
# except Exception as e:
#     print("There was a non-specific error!")
#     print("Built-In Python error info: ")
#     print(e, e.__doc__, type(e), sep='\n')