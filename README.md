# Employee Dashboard

This program processes Excel files containing daily reports and new employee information to generate a dashboard showing new employees under each team member.

## Requirements

- Python 3.7 or higher
- Required packages (install using `pip install -r requirements.txt`):
  - pandas
  - openpyxl
  - streamlit

## File Formats

### Daily Report Files
- Filename format: `Daily report_YYYYMMDD_Name_Surname.xls`
- Required columns:
  - Date
  - Candidate Name
  - Role
  - Interview
  - Status
  - Remark

### New Employee File
- Filename format: `New Employee_YYYYMM.xls`
- Required columns:
  - Employee Name
  - Join Date
  - Role
  - DOB (Date of Birth)
  - ID Card
  - Remark

## How to Run

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run employee_dashboard.py
   ```

3. Enter the directory path containing your Excel files when prompted.

4. The dashboard will display a table showing:
   - Employee Name
   - Join Date
   - Role
   - Team Member

5. You can download the dashboard data as a CSV file using the download button.

## Notes

- Make sure all Excel files are in the same directory
- The program will match new employees with passed candidates based on their name and role
- Only candidates with "Pass" status in the daily reports will be considered 