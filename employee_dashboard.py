import pandas as pd
import os
import streamlit as st
from datetime import datetime
import glob

def extract_team_member_name(filename):
    """Extract team member name from daily report filename"""
    parts = filename.split('_')
    if len(parts) >= 4:
        return f"{parts[2]} {parts[3].split('.')[0]}"
    return None

def process_daily_reports(directory):
    """Process all daily report files and return a DataFrame with passed candidates"""
    all_passed_candidates = []
    
    # Find all daily report files
    daily_reports = glob.glob(os.path.join(directory, "Daily report_*.xls"))
    
    for report_file in daily_reports:
        try:
            # Read the Excel file
            df = pd.read_excel(report_file)
            
            # Get team member name from filename
            team_member = extract_team_member_name(os.path.basename(report_file))
            
            # Filter for passed candidates
            passed_candidates = df[df['Status'] == 'Pass']
            
            # Add team member information
            for _, row in passed_candidates.iterrows():
                all_passed_candidates.append({
                    'Candidate Name': row['Candidate Name'],
                    'Role': row['Role'],
                    'Team Member': team_member
                })
                
        except Exception as e:
            st.error(f"Error processing file {report_file}: {str(e)}")
    
    return pd.DataFrame(all_passed_candidates)

def process_new_employees(directory):
    """Process new employee file and return a DataFrame"""
    new_employee_file = glob.glob(os.path.join(directory, "New Employee_*.xls"))
    
    if not new_employee_file:
        st.error("No new employee file found!")
        return None
    
    try:
        df = pd.read_excel(new_employee_file[0])
        return df
    except Exception as e:
        st.error(f"Error processing new employee file: {str(e)}")
        return None

def create_dashboard():
    st.title("New Employee Dashboard")
    
    # Get directory path from user
    directory = st.text_input("Enter the directory path containing the Excel files:")
    
    if directory and os.path.exists(directory):
        # Process files
        passed_candidates = process_daily_reports(directory)
        new_employees = process_new_employees(directory)
        
        if passed_candidates is not None and new_employees is not None:
            # Merge the data
            merged_data = pd.merge(
                new_employees,
                passed_candidates,
                left_on=['Employee Name', 'Role'],
                right_on=['Candidate Name', 'Role'],
                how='left'
            )
            
            # Select and rename columns for display
            display_data = merged_data[['Employee Name', 'Join Date', 'Role', 'Team Member']]
            
            # Display the dashboard
            st.dataframe(display_data)
            
            # Add download button
            csv = display_data.to_csv(index=False)
            st.download_button(
                label="Download Dashboard Data",
                data=csv,
                file_name="employee_dashboard.csv",
                mime="text/csv"
            )
        else:
            st.error("Failed to process one or more files. Please check the file formats and try again.")
    else:
        st.warning("Please enter a valid directory path.")

if __name__ == "__main__":
    create_dashboard() 