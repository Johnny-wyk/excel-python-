# --coding:utf-8--
import xlrd

file='test.xlsx'
data=xlrd.open_workbook(file)

table=data.sheets()[0]

nrows=table.nrows

print(nrows)

print(table.row(0))

for i in range(nrows):
    print(table.row(i))


print(table.row_len(0))