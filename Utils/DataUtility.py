'''
Created on Aug 2, 2019

@author: Arvind
'''
from Utils.ReadingData import XLReader
from Utils import Constants



#Read the test data from the external XLS file 
def getTestData(testCaseName,XLSFilePath):

    myData=[]
    xls = XLReader(XLSFilePath)
    testStartRowIndex=0
    
    if isRunnable(testCaseName, XLSFilePath):
        while not xls.getCellData(testStartRowIndex,0,Constants.DATASHEET)==testCaseName:
            testStartRowIndex=testStartRowIndex+1
    
        colStartRowIndex=testStartRowIndex+1
        dataStartRowIndex=testStartRowIndex+2
        
        maxRows=0
        while not xls.checkEmptyUsingColIndex(dataStartRowIndex+maxRows,1,Constants.DATASHEET):
            maxRows=maxRows+1
            
        maxCols=0
        while not xls.checkEmptyUsingColIndex(colStartRowIndex,maxCols,Constants.DATASHEET):
            maxCols=maxCols+1
            
        
        for rowNum in range(dataStartRowIndex,dataStartRowIndex+maxRows):
            Dict={}
            for colNum in range(0,maxCols):
                dataKey=xls.getCellData(colStartRowIndex,colNum,Constants.DATASHEET)
                dataVal=xls.getCellData(rowNum,colNum,Constants.DATASHEET)
                Dict[dataKey]=dataVal
            
            Dict["testName"]=testCaseName
            myData.append(Dict)
    
    Dict={}
    return myData

def isRunnable(testCaseName,readXLS):
    sheetName="TestCases"
    xls=XLReader(readXLS)
    row=xls.rowCount(sheetName)
    
    for i in range (0,row):
        tName=xls.getCellDataByColName(i, Constants.TCID_COL, sheetName)
        if (tName == testCaseName):
            runMode=xls.getCellDataByColName(i, Constants.RUNMODE_COL, sheetName)
            if (runMode=='Y'):
                return True
            else:
                return False
    
