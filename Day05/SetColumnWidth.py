# --coding:utf-8--

import xlwt

workbook=xlwt.Workbook(encoding='ascii')

worksheet=workbook.add_sheet('sheet1')

#写入内容
worksheet.write(0,0,'sjai')

#设置列宽
worksheet.col(0).width=256*20
workbook.save('johnny.xls')