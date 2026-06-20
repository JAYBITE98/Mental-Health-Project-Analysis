import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('mental_health_survey.csv')

# Show first 5 rows
print("="*50)
print("FIRST 5 ROWS OF THE DATA:")
print("="*50)
print(df.head())

# Show all column names
print("\n" + "="*50)
print("COLUMN NAMES IN YOUR DATASET:")
print("="*50)
print(df.columns.tolist())

# Count how many people said Yes vs No to treatment
treatment_counts = df['treatment'].value_counts()
print("\n" + "="*50)
print("TREATMENT COUNTS:")
print("="*50)
print(treatment_counts)

# Create the bar chart
plt.figure(figsize=(8, 5))
treatment_counts.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen', 'orange'])
plt.title('Have you sought treatment for mental health?', fontsize=14)
plt.xlabel('Sought Treatment', fontsize=12)
plt.ylabel('Number of People', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the chart
plt.show()

print("\n" + "="*50)
print("✅ CHART SHOULD HAVE POPPED UP ON YOUR SCREEN!")
print("="*50)