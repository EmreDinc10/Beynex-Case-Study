import pandas as pd
import openpyxl

# Load the Excel file
excel_file = "Job Postings.xlsx"
data_frame = pd.read_excel(excel_file, engine="openpyxl")

# Get the column names
column_names = data_frame.columns.tolist()

# Print the column names
print("Column Names:")
for column_name in column_names:
    print(column_name)

# Access the data rows
print("\nData Rows:")
for index, row in data_frame.iterrows():
    job_id = row["Job ID"]
    position = row["Position"]
    required_skills = row["Required Skills"]
    benefits = row["Benefits"]
    salary_range = row["Yearly Salary Range"]

    # Perform operations on the data
    # For example, you can print the details of each job posting
    print("Job ID:", job_id)
    print("Position:", position)
    print("Required Skills:", required_skills)
    print("Benefits:", benefits)
    print("Salary Range:", salary_range)
    print()

# Perform other important operations on the Excel data as needed
# You can manipulate, filter, or analyze the data using pandas functions

# Save the modified data back to the Excel file if required
# For example, you can save the modified DataFrame to a new sheet
# data_frame.to_excel(excel_file, sheet_name="Modified Data", index=False)
