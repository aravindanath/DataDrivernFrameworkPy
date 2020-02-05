'''
Created on Aug 2, 2019

@author: Arvind
'''
import xlrd
import xlwt


class XLReader:
    
    def __init__(self,path):
        self.path=path
        self.readXLS=xlrd.open_workbook(path)
        self.writeXLS=xlwt.Workbook(encoding='ascii')
        
    def getCellData(self,rowIndex,colIndex,sheetName):
        s=self.readXLS.sheet_by_name(sheetName)
        return s.cell_value(rowIndex,colIndex)
    
    
    def getCellDataByColName(self,rowIndex,colName,sheetName):
        s=self.readXLS.sheet_by_name(sheetName)
        for i in range(0,s.ncols):
            extractedColumnName=s.cell_value(0,i)
            if (colName==extractedColumnName):
                return s.cell_value(rowIndex,i)
        
    
    
    def checkEmptyUsingColIndex(self,rowIndex,colIndex,sheetName):
        s=self.readXLS.sheet_by_name(sheetName)
        cellType=0
        try:
            cellType= s.cell_type(rowIndex,colIndex)
        except Exception:
            pass
        
        if cellType== xlrd.XL_CELL_EMPTY:
            return True
        else:
            return False
        
    def rowCount(self,sheetName):
        s=self.readXLS.sheet_by_name(sheetName)
        return s.nrows
    
    def colCount(self,sheetName):
        s=self.readXLS.sheet_by_name(sheetName)
        return s.ncols
        