
import xlrd
from _overlapped import NULL

class XLReader:
    readXLS =NULL
    
    def __init__(self, path):
        self.path = path
        self.readXLS = xlrd.open_workbook(path)
        
    def rowCount(self, sheetName):
        s = self.readXLS.sheet_by_name(sheetName)
        return s.nrows
    
    def columnCount(self, sheetName):
        s = self.readXLS.sheet_by_name(sheetName)
        return s.ncols
    
    def getDataUsingColumnIndex(self,rowIndex, columnIndex, sheetName):
        s = self.readXLS.sheet_by_name(sheetName)
        return s.cell_value(rowIndex, columnIndex)