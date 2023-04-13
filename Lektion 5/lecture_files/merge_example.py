import pandas as pd

students = pd.DataFrame({
    'student_id': [1, 2, 3, 4],
    'name': ['Anna', 'Bengt', 'Caroline', 'David']
})

grades = pd.DataFrame({
    'student_id': [1, 2, 3, 4],
    'grade': [80, 85, 90, 95]
})

merged_data = pd.merge(students, grades, on='student_id', how='outer')
print(merged_data)