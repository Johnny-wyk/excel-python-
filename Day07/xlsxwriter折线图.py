# --coding:utf-8--

import xlsxwriter

workbook=xlsxwriter.Workbook('lineChart.xlsx')

worksheet=workbook.add_worksheet()

bold=workbook.add_format({'bold':1})

headings = ['Number', 'testA', 'testB']
data = [
    ['2017-9-1', '2017-9-2', '2017-9-3',
'2017-9-4', '2017-9-5', '2017-9-6'],
    [10, 40, 50, 20, 10, 50],
    [30, 60, 70, 50, 40, 30],
]

worksheet.write_row('A1',headings,bold)
worksheet.write_column('A2',data[0])
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])

# 创建⼀个折线图(line chart)
chart_col = workbook.add_chart({'type':
'line'})

# 配置第⼀个系列数据
chart_col.add_series({
 # 这⾥的sheet1是默认的值，因为我们在新建sheet时没有指定sheet名
# 如果我们新建sheet时设置了sheet名，这⾥就要设置成相应的值
'name': '=Sheet1!$B$1',
'categories': '=Sheet1!$A$2:$A$7',
'values':
'=Sheet1!$B$2:$B$7',
'line': {'color': 'red'},})

# 配置第⼆个系列数据
chart_col.add_series({
 'name': '=Sheet1!$C$1',
 'categories':  '=Sheet1!$A$2:$A$7',
 'values':
'=Sheet1!$C$2:$C$7',
 'line': {'color': 'yellow'},})

# 设置图表的title 和 x，y轴信息
chart_col.set_title({'name': 'The xxx site Bug Analysis'})
chart_col.set_x_axis({'name': 'Test number'})
chart_col.set_y_axis({'name':  'Sample length (mm)'})

# 设置图表的⻛格
chart_col.set_style(1)

 # 把图表插⼊到worksheet并设置偏移
worksheet.insert_chart('A10', chart_col,
{'x_offset': 25, 'y_offset': 10})

workbook.close()