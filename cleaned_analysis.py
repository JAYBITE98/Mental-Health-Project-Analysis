import pandas as pd
import matplotlib.pyplot as plt

# Load the messy data
df = pd.read_csv('mental_health_survey.csv')

print("="*60)
print("🧹 STARTING DATA CLEANING PROCESS...")
print("="*60)

# --- 1. CLEAN THE TREATMENT COLUMN (Fix typos) ---
print("\n1️⃣ Cleaning treatment column...")
# Convert "Y" to "Yes" and "N" to "No"
df['treatment'] = df['treatment'].replace({'Y': 'Yes', 'N': 'No'})
print(f"   ✅ Fixed 'Y' → 'Yes' and 'N' → 'No'")

# --- 2. HANDLE MISSING AGES ---
print("\n2️⃣ Fixing missing ages...")
print(f"   Before: {df['Age'].isnull().sum()} missing ages")

# Calculate the average age
average_age = df['Age'].mean()
print(f"   📊 Average age is: {average_age:.1f}")

# Fill missing ages with the average age
df['Age'] = df['Age'].fillna(average_age)
print(f"   ✅ After: {df['Age'].isnull().sum()} missing ages")

# --- 3. REMOVE USELESS COLUMNS ---
print("\n3️⃣ Removing unnecessary columns...")
# Remove 'Timestamp' (we don't need it)
# Also remove 'Country' since it has too many missing values
original_columns = len(df.columns)
df = df.drop(columns=['Timestamp', 'Country'])
print(f"   ✅ Removed 'Timestamp' and 'Country'")
print(f"   ✅ Columns reduced from {original_columns} to {len(df.columns)}")

# --- 4. CHECK FOR OTHER ISSUES ---
print("\n4️⃣ Summary of cleaned data:")
print(f"   Total rows: {len(df)}")
print(f"   Total columns: {len(df.columns)}")
print(f"   Remaining columns: {', '.join(df.columns.tolist())}")

# --- 5. CREATE A CLEANER BAR CHART ---
print("\n5️⃣ Creating cleaned bar chart...")

# Count cleaned treatment responses
treatment_counts = df['treatment'].value_counts()
print("\n   Cleaned treatment counts:")
print(f"   {treatment_counts}")

# Create a beautiful bar chart
plt.figure(figsize=(8, 5))
bars = treatment_counts.plot(kind='bar', color=['#FF6B6B', '#4ECDC4'])
plt.title('Mental Health Treatment Seeking Behavior', fontsize=16, fontweight='bold')
plt.xlabel('Sought Treatment', fontsize=12)
plt.ylabel('Number of People', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add numbers on top of each bar
for i, v in enumerate(treatment_counts):
    plt.text(i, v + 5, str(v), ha='center', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('cleaned_mental_health_chart.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n" + "="*60)
print("✅ DATA CLEANING COMPLETE!")
print("✅ Cleaned chart saved as 'cleaned_mental_health_chart.png'")
print("="*60)