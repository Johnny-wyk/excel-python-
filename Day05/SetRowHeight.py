# --coding:utf-8--

import xlwt

workbook=xlwt.Workbook(encoding='ascii')
worksheet=workbook.add_sheet('sheet1')

# #写入内容
# worksheet.write(0,0,'shuai')
# worksheet.write(1,1,'skke')
#
# #设置行高
# style=xlwt.easyxf('font:height 720;')
#
#
# row=worksheet.row(1)
# row.set_style(style)
#
# workbook.save('test.xls')

#合并列和行 合并2-3行 第1列
worksheet.write_merge(1,2,0,1,'sshuisd')