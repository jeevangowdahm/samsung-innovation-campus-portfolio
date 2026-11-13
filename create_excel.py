from openpyxl import Workbook

# Create a new workbook
workbook = Workbook()

# Select the active worksheet
sheet = workbook.active
sheet.title = "Students"

# Add headings
sheet["A1"] = "Name"
sheet["B1"] = "Age"
sheet["C1"] = "Course"

# Add data
sheet["A2"] = "Jeevan"
sheet["B2"] = 21
sheet["C2"] = "CSE AI/ML"

sheet["A3"] = "Rahul"
sheet["B3"] = 22
sheet["C3"] = "CSE"

# Save the Excel file
workbook.save("students.xlsx")

print("Excel file created successfully!")