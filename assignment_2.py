
'''

This assignment is supposed to  read in the CSV
file and calculate an average grade for the class.

Please find the error and fix it!

You will know the problem is solved when you get an output of:

The average grade for the class is: 84.75

'''


#%%

with open('student_grades.csv', 'r') as f:  # Open in read mode
    lines = f.readlines()

# Validate file has data
if len(lines) > 1:  # Ensures there is at least a header and one data row
    grades = []

    for line in lines[1:]:  # Skip the header
        row = line.strip().split(',')  # Correct variable name & remove newline
        
        try:
            grade = float(row[3])  # Convert to float
            grades.append(grade)
        except ValueError:
            print(f"Skipping invalid grade: {row[3]}")  # Handle bad data gracefully

    if grades:  # Avoid division by zero
        avg = sum(grades) / len(grades)
        print(f'The average grade for the class is: {avg:.2f}')
    else:
        print("No valid grades found.")
else:
    print("File is empty or only contains a header.")

        
# %%


