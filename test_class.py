'''
Created on 30-Mar-2019

@author: whizdom
'''

from DataDrivenFrameWork.ReadingData import XLReader
import pytest


def getTestData():
    # Initializing Array to be Returned
    myData = []
    
    # Initializing XLS Reader
    xls = XLReader("C:\\Users\\whizdom\\Desktop\\Book1.xlsx")
    
    # Specifying Test Case Name
    testCaseName = "TestA"
    
    # Calculating Test Start Row Index
    # First Considering it as 0
    testStartRowIndex = 0
    
    # Now Calculating the same
    while not xls.getDataUsingColumnIndex(testStartRowIndex, 0, "Sheet1") == testCaseName:
        testStartRowIndex = testStartRowIndex + 1
        
    # Calculating Column Name Row Index
    colStartRowIndex = testStartRowIndex + 1
    
    # Calculating Data Start Row Index
    dataStartRowIndex = testStartRowIndex + 2
    
    # Calculating Maximum Number of Rows
    maxRows = 0
    while not xls.checkEmptyUsingColumnIndex(dataStartRowIndex + maxRows, 1, "Sheet1"):
        maxRows = maxRows + 1
    
    # Calculating Maximum Columns
    maxCols = 0
    while not xls.checkEmptyUsingColumnIndex(colStartRowIndex, maxCols, "Sheet1"):
        maxCols = maxCols + 1
    
    # Reading Data from Table
    # Loop for Iterating over Rows
    for rowNum in range(dataStartRowIndex, dataStartRowIndex + maxRows):
        
        # Initializing Dictionary
        Dict = {}
        
        # Loop for Iterating over Cols
        for colNum in range(0, maxCols):
            
            # Reading Key
            dataKey = xls.getDataUsingColumnIndex(colStartRowIndex, colNum, "Sheet1")
            
            # Reading Value
            dataVal = xls.getDataUsingColumnIndex(rowNum, colNum, "Sheet1")
            
            # Inserting Data Into Dictionary
            Dict[dataKey] = dataVal
            
        # Inserting Dictionary Inside Array
        myData.append(Dict)
        
    return myData
                        

@pytest.mark.parametrize("dataRetrievedDictionary", getTestData())
def test_a(dataRetrievedDictionary):
    print(dataRetrievedDictionary.get("FirstName"), dataRetrievedDictionary.get("LastName"))
#     print(dataRetrievedDictionary[0].get("Runmode"))
