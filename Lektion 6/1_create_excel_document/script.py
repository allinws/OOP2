import openpyxl
import os


# Skapa en arbetsbok
workbook = openpyxl.Workbook()

# Välj aktivt kalkylblad
worksheet = workbook.active

# Sätt namn på kalkylbladet
worksheet.title = 'Sales sheet'

# Lägg till värden
worksheet.cell(row=1, column=1, value='Hello world')

# Spara filen
path = os.path.join(os.path.dirname(__file__), 'output.xlsx')
workbook.save(path)