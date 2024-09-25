# --coding:utf-8--

import xlsxwriter

workbook=xlsxwriter.Workbook('lucky.xlsx')

worksheet=workbook.add_worksheet('sheet1')

worksheet.write('A1','Johnny')
worksheet.write(0,1,12)
worksheet.write(1,1,123)

#写入函数
worksheet.write(2,1,'=sum(B1:B2)')
# worksheet.insert_image(0,5,'蓝桥杯证书.jpg')

import datetime
#写入日期
d = workbook.add_format({'num_format': 'yyyy-mm-dd'})
worksheet.write(0, 2,
datetime.datetime.strptime('2017-09-13', '%Y-%m-%d'), d)

#设置行高与列宽
worksheet.set_row(0,40)
worksheet.set_column('A:B',20)

#批量写入数据
worksheet.write_column('A1',[1,2,3,4])
worksheet.write_row('A2',[6,54,4,4])


workbook.close()