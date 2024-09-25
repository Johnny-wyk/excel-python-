# --coding:utf-8--

from openpyxl import load_workbook

wb=load_workbook('lucky.xlsx')

ws=wb.active

ws.row_dimensions[2].height=40

ws.column_dimensions['C'].width=100

wb.save('lucky.xlsx')