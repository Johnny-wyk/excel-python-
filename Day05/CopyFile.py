import xlrd
from xlutils.copy import copy

workbook=xlrd.open_workbook('test.xlsx')

newWorkbook=copy(workbook)


sheet=workbook.sheet_by_index(0)
col=sheet.col_values(0)
print(col)

cel_val=sheet.cell_value(0,0)

#写入表格信息
sheet_write=newWorkbook.get_sheet(0)
sheet_write.write(1,1,'shkekf')

newWorkbook.save('newFile.xls')
