# --coding:utf-8--

import xlrd

file='test.xlsx'
data=xlrd.open_workbook(file)

table=data.sheets()[0]

# print(table.cell(0,0))
#
# print(table.cell_value(0,0))


nrows=table.nrows

ncols=table.ncols

for i in range(nrows):
    for j in range(ncols):
        print(table.cell_value(i,j),end='')
    print()


