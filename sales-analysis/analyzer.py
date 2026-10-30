import os
import pandas as pd
from helpers import cac_total, format_currency

# Check the current working directory
print('Current Working Directory:', os.getcwd())

# Check if our data file exists
data_file_path = 'data/sales.csv'

if (os.path.exists(data_file_path)):
    print(f"✅ The file '{data_file_path}' exists.")
else:
    print(f"❌ The file '{data_file_path}' does not exist.")
    print("Please ensure the file is in the correct directory.")
    

### Read the CSV file into a DataFrame
df = pd.read_csv(data_file_path)
print('CSV Data:')
print(df)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

totals = []
#df['total_price'] = df['quantity'] * df['price']
for index, row in df.iterrows():
    total = cac_total(row['quantity'], row['price'])
    totals.append(total)

df['total_price'] = totals
print("\nData with Total Price:")
print(df)

for index, row in df.iterrows():
    formatted_total = format_currency(row['total_price'])
    #df['total_price'][index] = formatted_total
    print(f"{row['product']}: {formatted_total}")

grant_total = df['total_price'].sum()
formatted_grant_total = format_currency(grant_total)
print(f"\nGrand Total: {formatted_grant_total}")

os.makedirs('output', exist_ok=True)

# To CSV
output_file_path = 'output/sales_with_total.csv'
df.to_csv(output_file_path, index=False)
print(f"\n✅ Data with total price saved to '{output_file_path}'")

# To JSON
output_json_path = 'output/sales_with_total.json'
df.to_json(output_json_path, orient='records', indent=2)
print(f"✅ Data with total price saved to '{output_json_path}'")

# To Excel
output_excel_path = 'output/sales_with_total.xlsx'
df.to_excel(output_excel_path, index=False)
print(f"✅ Data with total price saved to '{output_excel_path}'")