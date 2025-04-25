import pandas as pd

# Create a new employee file
new_employee_data = {
    'Employee Name': ['John Doe', 'Jane Smith'],
    'Join Date': ['2023-10-01', '2023-10-15'],
    'Role': ['Engineer', 'Designer'],
    'DOB': ['1990-01-01', '1992-02-02'],
    'ID Card': ['12345', '67890'],
    'Remark': ['N/A', 'N/A']
}
new_employee_df = pd.DataFrame(new_employee_data)
new_employee_df.to_excel('New Employee_202310.xlsx', index=False)

# Create a daily report file
daily_report_data = {
    'Date': ['2023-10-01', '2023-10-02'],
    'Candidate Name': ['John Doe', 'Jane Smith'],
    'Role': ['Engineer', 'Designer'],
    'Interview': ['Yes', 'Yes'],
    'Status': ['Pass', 'Pass'],
    'Remark': ['Good', 'Excellent']
}
daily_report_df = pd.DataFrame(daily_report_data)
daily_report_df.to_excel('Daily report_20231001_John_Doe.xlsx', index=False) 