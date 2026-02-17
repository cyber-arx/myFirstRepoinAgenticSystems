# Student Marks Analyzer

# Store marks of at least 8 students
marks = [78, 85, 90, 65, 72, 88, 92, 80]

# Print full list
print("All Marks:", marks)

# Print first 3 marks using slicing
print("First 3 marks:", marks[:3])

# Print last 3 marks using slicing
print("Last 3 marks:", marks[-3:])

# Calculate highest, lowest, and average
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

# Display results
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", round(average, 2))
