# --coding:utf-8--
import xlwt

workbook=xlwt.Workbook(encoding='ascii')
worksheet=workbook.add_sheet('sheet1')

border = xlwt.Borders()
border.left=xlwt.Borders.DOUBLE
border.bottom=xlwt.Borders.DASHED

border.left_colour=0
border.bottom_colour=1

style=xlwt.XFStyle()
style.borders=border

worksheet.write(0,0,'dskrr',style)


workbook.save('test.xls')