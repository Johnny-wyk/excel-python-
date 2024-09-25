# --coding:utf-8--

from openpyxl import Workbook
from openpyxl.chart import BarChart,Series,Reference
from copy import deepcopy
wb=Workbook()
ws=wb.active

rows=[('month','salary'),
      (1,20),
      (2,30),
      (3,40),
      (4,50)]

for row in rows:
    ws.append(row)

#图表一
chart1=BarChart()
#图表类型
chart1.type='col'
#设置图标样式
chart1.style=30
#设置图标标题
chart1.title='图标1'
#设置x轴和y轴
chart1.x_axis.title='月份'
chart1.y_axis.title='工资'
#引用单元格的范围
data=Reference(ws,min_row=1,max_row=6,min_col=1,max_col=3)
#引用工作表的范围
labels=Reference(ws,min_col=1,min_row=2,max_col=6)

chart1.add_data(data,titles_from_data=True)
chart1.set_categories(labels)
ws.add_chart(chart1,'A10')

#图表3
chart3=deepcopy(chart1)
chart3.type='col'
chart3.grouping='stacked'
chart3.overlap=100
chart3.title='图标三'
ws.add_chart(chart3,'C20')

chart4=deepcopy(chart1)

wb.save('2D.xlsx')