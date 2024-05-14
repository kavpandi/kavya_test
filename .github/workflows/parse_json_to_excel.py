import pandas as pd

# Sample JSON data
json_data = api_data.json

# Parse JSON data into a DataFrame
df = pd.DataFrame(json_data)

# Write DataFrame to Excel file
excel_file = "output.xlsx"
df.to_excel(excel_file, index=False)

print("Excel file '{}' created successfully.".format(excel_file))
