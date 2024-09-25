# --coding:utf-8--
import xlrd

data=xlrd.open_workbook('test.xlsx')

table=data.sheet_by_index(0)

nrows=table.nrows

ncols=table.ncols

for i in range(nrows):
    print(table.cell_value(i,0))

