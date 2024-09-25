# --coding:utf-8--

import xlrd

file='test.xlsx'
data=xlrd.open_workbook(file)

table=data.sheets()[0]
ncols=table.ncols

#返回列数据
col=table.col(0,0,None)
print(col)

for i in range(ncols):
    print(table.col(i,0,None))

