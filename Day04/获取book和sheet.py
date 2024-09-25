import xlrd

file='test.xlsx'
data=xlrd.open_workbook(file)
# print(data)


# sheets=data.sheets()
# print(sheets)
#
# sheet=data.sheets()[0]
# print(sheet)
#
# sheet=data.sheet_by_name('Sheet1')
# print(sheet)
#以上三个函数都会返回⼀个xlrd.sheet.Sheet()对象

#获取sheet名字
names=data.sheet_names()
print(names)

data.sheet_loaded(names)


