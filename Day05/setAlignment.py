
import xlwt

workbook=xlwt.Workbook(encoding='ascii')
worksheet=workbook.add_sheet('sheet1')

worksheet.write(1,0,'skfnskefn')

style=xlwt.XFStyle()

al=xlwt.Alignment()
#设置水平居中
al.horz=0x02
#设置垂直居中
al.vert=0x01

style.alignment=al

worksheet.write(1,3,'skfnskefn',style)
workbook.save('dsfs.xls')

