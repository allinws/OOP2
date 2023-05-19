import sys
from pathlib import Path
import os.path

""" How to save a file in a folder """

# Get path of current file
file_path = Path(sys.path[0])

# Exempel
# import datetime
# current_date = datetime.datetime.now().date()
# f'user/alexanderlidngren/download/{current_date}/'

# Set direcory to save to
directory = f'{file_path}/html/' 
filename = "file.html"
new_file_path = os.path.join(directory, filename)

# Check if directory exists, if not create it
if not os.path.isdir(directory):
    os.mkdir(directory)

# Write to file
file = open(new_file_path, "w")
file.write('<p>Hej</p>')
file.close()