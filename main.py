import pandas as pd
import glob

filepaths = glob.glob("*xlsx")
print(filepaths)

for i in filepaths:
    df = pd.read_excel(i, sheet_name='Sheet 1')
    print(df)