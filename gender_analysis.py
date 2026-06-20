import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('mental_health_survey.csv')

# Clean the data (same as before)
df['treatment'] = df['treatment'].replace({'Y': 'Yes', 'N': 'No'})
average_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(average_age)
df = df.drop(columns=['Timestamp', 'Country'])

print("="*60)
print("👥 ANALYSIS: Treatment Seeking by Gender")
print("="*60)

# See how many people in each gender
gender_counts = df['Gender'].value_counts()
print("\n📊 Gender distribution:")
print(gender_counts)

# Create a cross-tabulation: Gender vs Treatment
gender_treatment = pd.crosstab(df['Gender'], df['treatment'])
print("\n📊 Gender vs Treatment Seeking:")
print(gender_treatment)

# Create a grouped bar chart
gender_treatment.plot(kind='bar', figsize=(10, 6), color=['#FF6B6B', '#4ECDC4'])
plt.title('Mental Health Treatment by Gender', fontsize=16, fontweight='bold')
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Number of People', fontsize=12)
plt.xticks(rotation=0)
plt.legend(title='Sought Treatment')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add numbers on each bar
for i, row in enumerate(gender_treatment.iterrows()):
    for j, value in enumerate(row[1]):
        plt.text(i - 0.1 + j*0.2, value + 3, str(value), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('gender_treatment_chart.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✅ Gender analysis complete!")
print("✅ Chart saved as 'gender_treatment_chart.png'")