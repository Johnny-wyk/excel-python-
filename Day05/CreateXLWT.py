# --coding:utf-8--
import xlwt


workbook=xlwt.Workbook(encoding='ascii')
print(workbook)

#创建新的sheet表
worksheet=workbook.add_sheet('new sheet')

#写入内容
#worksheet.write(0,0,'johnny')

#创建样式对象
style=xlwt.XFStyle()

font=xlwt.Font()

font.name='黑体'
font.bold=True
font.italic=True
font.underline=True

#设置样式
style.font=font

#向单元格中写入内容
worksheet.write(0,0,'johnny')
worksheet.write(2,1,'woejw',style)

workbook.save('te.xls')