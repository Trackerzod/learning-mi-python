from emdlibs import data_reader as dr
import pandas
import sys
import math as maths

backtrackCount = 5
initPlaceholderVals = 0.1
stdDevArr = []

def standardDeviation(valueList):
    m = 0.0
    s = 0.0
    k = 1
    for value in valueList: 
        tmpM = m
        m += (value - tmpM) / k
        s += (value - tmpM) * (value - m)
        k += 1
    return maths.sqrt(m / (k-2))

def getContinousStdDev(dataSet):
    skip = backtrackCount
    previousVals = []
    
    for val in range(0, backtrackCount):
        previousVals.append(dataSet[val])
    
    for data in dataSet:
        if skip > 0:
            skip -= 1
            stdDevArr.append(1)
            previousVals.append(data)
        else:
            stdDevArr.append(standardDeviation(previousVals) - data)
            previousVals.pop(0)
            previousVals.append(data)
            
    return stdDevArr
