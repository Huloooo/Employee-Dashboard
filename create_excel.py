import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
file_path = 'example.xlsx'
df.to_excel(file_path, index=False)

print(f"Excel file created at: {file_path}") 