import pandas as pd
import matplotlib.pyplot as plt

# Load and clean the data
df = pd.read_csv('mental_health_survey.csv')
df['treatment'] = df['treatment'].replace({'Y': 'Yes', 'N': 'No'})
average_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(average_age)
df = df.drop(columns=['Timestamp', 'Country'])

print("="*60)
print("💼 ANALYSIS: Treatment Seeking by Work Interference")
print("="*60)

# Check work_interfere column
print("\n📊 Work Interference responses:")
print(df['work_interfere'].value_counts())

# Create crosstab
work_treatment = pd.crosstab(df['work_interfere'], df['treatment'])
print("\n📊 Work Interference vs Treatment Seeking:")
print(work_treatment)

# Add percentages
work_pct = work_treatment.div(work_treatment.sum(axis=1), axis=0) * 100
print("\n📊 Work Interference vs Treatment (Percentages):")
print(work_pct.round(1))

# Create grouped bar chart
fig, ax = plt.subplots(figsize=(10, 6))
work_treatment.plot(kind='bar', ax=ax, color=['#FF6B6B', '#4ECDC4'])
plt.title('Mental Health Treatment by Work Interference Level', fontsize=16, fontweight='bold')
plt.xlabel('Does work interfere with mental health?', fontsize=12)
plt.ylabel('Number of People', fontsize=12)
plt.xticks(rotation=0)
plt.legend(title='Sought Treatment')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add numbers on bars
for i, row in enumerate(work_treatment.iterrows()):
    for j, value in enumerate(row[1]):
        plt.text(i - 0.1 + j*0.2, value + 3, str(value), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('work_treatment_chart.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✅ Work analysis complete!")
print("✅ Chart saved as 'work_treatment_chart.png'")