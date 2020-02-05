
import logging
# import time

# import allure
# from delayed_assert.delayed_assert import assert_expectations, expect
# import pytest

# from DataDrivenFrameWork import DataUtil
# from DataDrivenFrameWork.Base import abc
# from DataDrivenFrameWork.ReadingData import XLReader

logger = logging.getLogger()
logger.setLevel(logging.INFO)

global readXLS



def isRunnable(testCaseName, readXLS):
    sheetName = "Sheet2"
    row = readXLS.rowCount(sheetName)
    for i in range (0, row):
        tName = readXLS.getDataUsingColumnName(i , "TCID" , "Sheet2")
        if (tName == testCaseName):
            runMode = readXLS.getDataUsingColumnName(i , "RunModes" , "Sheet2")
            if (runMode == "Y"):
                return True
            else:
                return False

    
def getTestData(testCaseName, xls):
    try:
        pass
          
    except Exception as capturedError:
        logger.error(capturedError)
    # Initializing Array to be Returned
    myData = []
    
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
