import pandas as pd

df = pd.read_excel('covid.xlsx', usecols= ['indicator_display', 'country','sample_total', 'indicator_val', 'urban_rural', 'industry', 'month'])
df['country'] = df['country'].astype("category")
filter2 = df['country'] == 'Tajikistan'
filter3 = df['country'] == 'Croatia'
filter = df['indicator_display'] == 'Are concerned today about the potential effects of COVID-19 on their family (% of HHs)'
df2 = df[filter2 & filter]
df3 = df[filter3 & filter]
print(df2['indicator_val'].mean())
print(df3['indicator_val'].mean())
