# --coding:utf-8--

import xlwt
workbook=xlwt.Workbook(encoding='ascii')

worksheet= workbook.add_sheet('sheet1')

pattern= xlwt.Pattern()

#设置背景模式
pattern.pattern=xlwt.Pattern.SOLID_PATTERN
#设置背景色颜色
pattern.pattern_fore_colour=52

style=xlwt.XFStyle()
style.pattern=pattern

worksheet.write(0,0,'sadeed',style)

workbook.save('frf.xls')