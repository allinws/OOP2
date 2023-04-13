import pandas as pd

lstSrc = [1, 2, 3, 4]
df = pd.DataFrame() 
df["TimeTook"] = lstSrc
with pd.ExcelWriter("result.xlsx", engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='sheetname')