'''
Created on 06-Apr-2019

@author: Arvind
'''


from Utils.ReadingData import XLReader



class DataManagement:
    readXLS = XLReader("../testData/TestData.xlsx")
    testCaseName = "TestB"
    testStartRowIndex = 0
    testStartRowNum = testStartRowIndex + 1
    while not readXLS.getDataUsingColumnIndex(testStartRowIndex, 0, "Sheet1") == testCaseName:
        testStartRowIndex = testStartRowIndex + 1
    print("Test Starts at", testStartRowIndex)
    colStartRowIndex = testStartRowIndex + 1
    colStartRowNum = colStartRowIndex + 1
    
    dataStartRowIndex = testStartRowIndex + 2
    dataStartRowNum = dataStartRowIndex + 1
    print("Column Starts at", colStartRowIndex)
    print("Data Starts at", dataStartRowIndex)
    
    maxRows = 0
    while not readXLS.checkEmptyUsingColumnIndex(dataStartRowIndex + maxRows, 1, "Sheet1"):
        maxRows = maxRows + 1
    print("Maximum Number of Rows are", maxRows)
    
    maxCols = 0
    while not readXLS.checkEmptyUsingColumnIndex(colStartRowIndex, maxCols, "Sheet1"):
        maxCols = maxCols + 1
    print("Maximum Number of Cols are", maxCols) 
    
    for rowNum in range(dataStartRowIndex, dataStartRowIndex + maxRows):
        for colNum in range(0, maxCols):
            dataKey = readXLS.getDataUsingColumnIndex(colStartRowIndex, colNum, "Sheet1")
            dataVal = readXLS.getDataUsingColumnIndex(rowNum, colNum, "Sheet1")
            print(dataKey, ':', dataVal)
