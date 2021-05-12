# Name: Jamar Hill
# Date: 5/10/2021
# Description: CS 162 Project 6a

def list_max(numLst):  # numLst = [3, 2, 7, 8, 4], max is 8
    start_val = numLst[0]
    # start_val = 3
    return getmax(numLst, start_val)


# Recursive functions
# 1. Base case -> The most basic form of the question broken down
# 2. If not base, what can we do to break the problem down
# 3. Recursively call the function with the smaller problem

# listOfNo = [5, 4, 8, 9, 10], highestVal = 10
def getmax(numLst, highestVal):
    # Base case reached when list is empty
    if (len(numLst) == 0):
        return highestVal
    else:
        # Update highestVal if necessary
        if (numLst[0] > highestVal):
            highestVal = numLst[0]

        numLst.remove(numLst[0])  # Reducing to smaller problem on each recursive call

        return getmax(numLst, highestVal)
