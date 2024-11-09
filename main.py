import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
s_name = ['Rajveer', 'Yaksh', 'Anay', 'Soham', 'Ishaan']
s_marks = [95, 87, 45, 69, 85]

# Calculate marks percentage (out of 50)
marks_percentage = [(x / 50) * 100 for x in s_marks]
print(marks_percentage)

# Function to plot the data
def plot_student_marks():
    # Creating a bar chart where x is the student names, and y is the marks
    plt.bar(s_name, s_marks, color='blue')
    
    # Adding title and labels
    plt.title('Student Marks')
    plt.xlabel('Student Names')
    plt.ylabel('Marks')
    
    # Show the plot
    plt.show()

# Call the function to plot the data
plot_student_marks()
