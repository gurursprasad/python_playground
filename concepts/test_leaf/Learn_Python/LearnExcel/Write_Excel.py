from openpyxl import Workbook

# Create object for Workbook
wb = Workbook()

# Activate sheet in the workbook with object for the sheet
sh = wb.active

# Create sheet name
sh.title = "pythondetails"

# Write Values
sh['A1'].value = "TestLeaf"
# sh['B1'].value = "Mentors"
sh.append(['1', '2', '3'])
sh.append(['1', '2', '3'])

# Saving the file
wb.save('C:\\Users\\gurur\\PycharmProjects\\Learn_Python\\ExcelData\\WriteExcel.xlsx')
