import matplotlib.pyplot as plt

# Sample data
subjects = ['Maths', 'DSA', 'Python', 'Statistics']
marks = [80, 75, 90, 85]

# Line plot
plt.plot(subjects, marks, marker='o')
plt.title("Line Plot of Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Bar chart
plt.bar(subjects, marks)
plt.title("Subject-wise Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Histogram
plt.hist(marks, bins=4, edgecolor='black')
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()