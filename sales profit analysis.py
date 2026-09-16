import pandas as pd

# Excel file load karna
df = pd.read_excel("sales profit analysis.xlsx", sheet_name="Raw_Data")

# First 5 rows dekhna
print(df.head())
