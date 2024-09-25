# --coding:utf-8--

from openpyxl import Workbook
from openpyxl.chart import Reference,Series,BarChart3D

wb=Workbook()
ws=wb.active

rows= [('month','salary'),
       (1,2000),
       (2,4000),
       (3,1500)]

for row in rows:
    ws.append(row)

chart=BarChart3D()
chart.title='3D'
data=Reference(ws,min_col=1,max_col=2,min_row=1,max_row=4)
labels=Reference(ws,min_col=1,min_row=2,max_row=4)
chart.add_data(data,titles_from_data=True)
chart.set_categories(labels)
ws.add_chart(chart,'E5')
wb.save('3DChart.xlsx')