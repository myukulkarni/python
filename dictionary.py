# Step 1: Read the number of students
n = int(input())

# Step 2: Initialize an empty dictionary to store student names and their marks
student_marks = {}

# Step 3: Read the students' names and marks
for _ in range(n):
    # Split the input into name and scores
    data = input().split()
    name = data[0]
    # Convert scores to a list of floats
    marks = list(map(float, data[1:]))
    # Store the name and marks in the dictionary
    student_marks[name] = marks

# Step 4: Read the query name
query_name = input()

# Step 5: Retrieve the marks of the queried student
marks = student_marks[query_name]

# Step 6: Calculate the average of the marks
average = sum(marks) / len(marks)

# Step 7: Print the average rounded to 2 decimal places
print(f"{average:.2f}")
