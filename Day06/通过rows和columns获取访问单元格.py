# --coding:utf-8--

from openpyxl import load_workbook
wb=load_workbook('lucky.xlsx')

ws=wb.active

for row in ws.rows:
    for r in row:
        print(r.value)