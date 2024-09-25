from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
print(sheet.title)
sheet.title="Johnny"

sheet["B9"]="djdjfj"

wb.save("exceltest.xlsx")