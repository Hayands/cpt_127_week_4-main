'''

For this assignment please do the following:

- Read in the student_grades.csv file

- calculate the average grade for the class

- for each student record calculate the difference between the student's grade and the average grade

- write the output to a new file called student_grade_differences.csv

'''
import csv

# Read student grades from the CSV file
input_file = 'student_grades.csv'
output_file = 'student_grade_differences.csv'

students = []

with open(input_file, 'r') as file:
    reader = csv.reader(file)
    
    # Read header and store data
    header = next(reader)  
    if header and len(header) >= 4:
        students.append(header + ['Difference from Average'])  # Add new column header

    grades = []
    
    # Read student data
    for row in reader:
        try:
            grade = float(row[3])  # Convert grade to float
            grades.append(grade)
            students.append(row)  # Store row data
        except (ValueError, IndexError):
            print(f"Skipping invalid row: {row}")

# Calculate average grade
if grades:
    avg_grade = sum(grades) / len(grades)
    print(f"The average grade for the class is: {avg_grade:.2f}")

    # Compute differences and store in the list
    for i in range(1, len(students)):  # Skip header
        student_grade = float(students[i][3])
        difference = student_grade - avg_grade
        students[i].append(f"{difference:.2f}")  # Append difference to the row

    # Write output to a new CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)

    print(f"Output written to {output_file}")
else:
    print("No valid grades found. No output file was created.")
