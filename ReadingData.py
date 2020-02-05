
import xlrd
import xlwt
# from _overlapped import NULL
import null as NULL






class XLReader:
    readXLS =NULL
#     writeXLS = NULL

    def __init__(self, path):
        self.path = path
        self.readXLS = xlrd.open_workbook(path)
        self.writeXLS = xlwt.Workbook(encoding = 'ascii')
        
    def rowCount(self, sheetName):
        s = self.readXLS.sheet_by_name(sheetName)
        return s.nrows
    
    def columnCount(self, sheetName):
        s = self.readXLS.sheet_by_name(sheetName)
        return s.ncols
    
    def getDataUsingColumnIndex(self,rowIndex, columnIndex, sheetName):
        s = self.readXLS.sheet_by_name(sheetName)
        return s.cell_value(rowIndex, columnIndex)
    
    def checkEmptyUsingColumnIndex(self,rowIndex, columnIndex, sheetName):
        s = self.readXLS.sheet_by_name(sheetName)
        cellType = 0
        try:
            cellType = s.cell_type(rowIndex, columnIndex)
        except Exception:
            pass
        if cellType == xlrd.XL_CELL_EMPTY:
            return True
        else:
            return False 
#         return s.cell_type(rowIndex, columnIndex)
    
    def getDataUsingColumnName(self,rowIndex, columnName, sheetName):
        s = self.readXLS.sheet_by_name(sheetName)
        for i in range (0,s.ncols):
            extractedColumnName = s.cell_value(0,i)
            if (columnName == extractedColumnName):
                return s.cell_value(rowIndex, i)

 