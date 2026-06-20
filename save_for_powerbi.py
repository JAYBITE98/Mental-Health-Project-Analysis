import pandas as pd

# Load the raw data
df = pd.read_csv('mental_health_survey.csv')

# Apply all your cleaning steps
df['treatment'] = df['treatment'].replace({'Y': 'Yes', 'N': 'No'})
average_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(average_age)
df = df.drop(columns=['Timestamp', 'Country'])

# Save the cleaned data
df.to_csv('cleaned_mental_health_data.csv', index=False)

print("="*60)
print("✅ CLEANED DATA SAVED FOR POWER BI!")
print("="*60)
print(f"   File: cleaned_mental_health_data.csv")
print(f"   Rows: {len(df)}")
print(f"   Columns: {len(df.columns)}")
print("="*60)
print("\n📋 The file is now ready to import into Power BI!")