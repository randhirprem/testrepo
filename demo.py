import pandas as pd #pip install pandas onpenpyxl

df = pd.read_excel(
    io='supermarkt_sales.xlsx',
    engine='openpyxl',
    sheet_name='Sales'
    #skiprows=3,
    usecols'B:R',
    nrows=1000,
)
print(df)
