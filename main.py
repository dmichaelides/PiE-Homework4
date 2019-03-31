"""
'Python-is-Easy' Homework #4 (Lists)
DESCRIPTION: 
The main goal of this file created, is to get acquianted with creating and managing Lists in Python.  It is the forth homework assigment in the
'Python is Easy' course, from Pirple.

The assigment requied creating two Lists, with a Function to add items to the Lists.  
More details in comments below. 
"""


myUniqueList = [] # This list needs to have unique values. If the added item already exists, it would be added to the 'myLeftovers' list. 
myLeftovers = [] 

# Created the PrintLists function to be used at the end of the application to show the items in each list. 
def PrintLists(n):
	print(n,"Unique List",myUniqueList)
	print(n,"Leftover List",myLeftovers)

# The AddItem function used to add items to the lists, based on the condition of uniqueness in the myUniqueList list. 
def AddItem(n):
	if n not in myUniqueList:
		myUniqueList.append(n)
		return True
	else:
		myLeftovers.append(n)
		return False

# Add two unique items "A" and "B" several times over. 
AddItem("A")
AddItem("B")

PrintLists("First print of")

AddItem("A")
AddItem("B")

PrintLists("Second Print of")

AddItem("A")
AddItem("B")
AddItem("A")
AddItem("B")
AddItem("A")
AddItem("B")

PrintLists("Final")