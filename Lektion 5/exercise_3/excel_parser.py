import openpyxl
from openpyxl.utils import get_column_letter
import csv
from openpyxl.chart import BarChart, Reference
import datetime

SALES_SHEET_NAME = 'Sales'
REGION_SHEET_NAME = "Sales per region"
PRODUCT_SHEET_NAME = 'Sales per product'

# Skapa en arbetsbok och välj aktivt kalkylblad
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = 'Sales'

# Skapa Sales per region sheet
sales_sheet = workbook[SALES_SHEET_NAME]
region_sheet = workbook.create_sheet(title=REGION_SHEET_NAME)
product_sheet = workbook.create_sheet(title=PRODUCT_SHEET_NAME)


# Öppna CSV-filen och läs datan
with open('sales_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = list(csv_reader)

""" Total försäljning """

# Sätt rubrikerna på första raden 
headers = data[0]
for column_index, header in enumerate(headers):
    worksheet.cell(row=1, column=column_index+1, value=header)

data = sorted(data[1:], key=lambda x: datetime.datetime.strptime(x[0], '%Y-%m-%d'))

# Skriv data till Excel resterande av dokumentet
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


""" PER REGION """

# Spara försäljning per region i en dict
region_sales = {}
for row_index in range(2, worksheet.max_row + 1):
    region = worksheet.cell(row=row_index, column=3).value
    total_sales = float(worksheet.cell(row=row_index, column=6).value)
    region_sales[region] = round(region_sales.get(region, 0) + total_sales,2)

# Byt sheet till region-sheetet
worksheet = workbook[region_sheet.title]

# Skapa rubriker
worksheet.cell(row=1, column=1, value='Region')
worksheet.cell(row=1, column=2, value='Sales')

# Formatera rubrikerna i feststil
for cell in worksheet[1]:
    cell.font = openpyxl.styles.Font(bold=True, size=14)

# Skriv in datan för försäljning per region
for index, (name, sales) in enumerate(sorted(region_sales.items()), start=2):
    worksheet.cell(row=index, column=1, value=name)
    worksheet.cell(row=index, column=2, value=sales).number_format = "#,##0"

# Skapa diagram för regionsförsäljningen

# Skapa en datareferens till försäljningsdata
data = Reference(worksheet, min_col=2, min_row=1, max_col=2, max_row=worksheet.max_row)

# Skapa en kategorireferens till regioner
categories = Reference(worksheet, min_col=1, min_row=1, max_row=worksheet.max_row)

# Skapa ett stapeldiagram
chart = BarChart()
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)
chart.title = "Försäljning per region"
chart.x_axis.title = "Region"
chart.y_axis.title = "Försäljning (kr)"

# Lägg till diagrammet i arbetsboken
worksheet.add_chart(chart, "D2")

# Spara arbetsboken
workbook.save('output.xlsx')
