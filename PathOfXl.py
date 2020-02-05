
from DataDrivenFrameWork.ReadingData import XLReader
xl = XLReader("C:\\Users\\whizdom\\Desktop\\Data.xlsx")
print(xl.rowCount("Sheet1"))
print(xl.columnCount("Sheet1"))
print(xl.getDataUsingColumnIndex(1,1,"Sheet1"))
print(xl.getDataUsingColumnName(3,"Password","Sheet1"))

