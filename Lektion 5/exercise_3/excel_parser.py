import openpyxl
from openpyxl.utils import get_column_letter
import csv

# Skapa en arbetsbok och välj aktivt kalkylblad
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = 'Sales'

# Skapa andra sheets
region_sheet = workbook.create_sheet(title="Sales per region")

# Öppna CSV-filen och läs datan
with open('sales_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = list(csv_reader)

# Sätt rubrikerna på första raden
headers = data[0]
for column_index, header in enumerate(headers):
    worksheet.cell(row=1, column=column_index+1, value=header)
    column_letter = get_column_letter(column_index+1)
    worksheet.column_dimensions[column_letter].width = len(header) + 2

# Skriv data till Excel från andra raden
for row_index, row_data in enumerate(data[1:], start=2):
    for column_index, cell_data in enumerate(row_data):
        worksheet.cell(row=row_index, column=column_index+1, value=cell_data)

# Lägg till kolumn med total försäljning
worksheet.cell(row=1, column=6, value='Total försäljning')
for row_index in range(2, worksheet.max_row + 1):
    count = int(worksheet.cell(row=row_index, column=4).value)
    price = float(worksheet.cell(row=row_index, column=5).value)
    total_amount = count * price
    worksheet.cell(row=row_index, column=6, value=total_amount).number_format = "#,##0"

# Formatera rubrikerna i feststil
for cell in worksheet[1]:
    cell.font = openpyxl.styles.Font(bold=True, size=14)


region_sales = {}
for row_index in range(2, worksheet.max_row + 1):
    region = worksheet.cell(row=row_index, column=3).value
    total_sales = float(worksheet.cell(row=row_index, column=6).value)
    region_sales[region] = round(region_sales.get(region, 0) + total_sales,2)

worksheet = workbook[region_sheet.title]

worksheet.cell(row=1, column=1, value='Region')
worksheet.cell(row=1, column=2, value='Sales')

# Formatera rubrikerna i feststil
for cell in worksheet[1]:
    cell.font = openpyxl.styles.Font(bold=True, size=14)

for index, (name, sales) in enumerate(sorted(region_sales.items()), start=2):
    worksheet.cell(row=index, column=1, value=name)
    worksheet.cell(row=index, column=2, value=sales)

# Spara arbetsboken
workbook.save('output.xlsx')
