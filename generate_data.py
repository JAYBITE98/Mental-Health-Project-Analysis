import pandas as pd
import random
import numpy as np

# Set a "seed" so the random data is the same every time you run it (good for learning!)
random.seed(42)
np.random.seed(42)

# 1. Create a list of realistic fake people
num_people = 500

# Possible answers for our survey
genders = ['Male', 'Female', 'Non-binary', 'Male', 'Female']  # Biased slightly towards M/F
countries = ['United States', 'United Kingdom', 'Canada', 'Australia', 'India', 'Germany', 'Other']
ages = list(range(18, 70))
work_interfere = ['Often', 'Rarely', 'Sometimes', 'Never', 'Often', 'Rarely', 'Never']  # Some bias
treatment_options = ['Yes', 'No', 'Yes', 'No', 'No']  # 40% say Yes roughly
family_history = ['Yes', 'No', 'No', 'Yes', 'No']  # 40% say Yes

# 2. Generate the data row by row
data = {
    'Timestamp': [f'2024-01-{random.randint(1,30)}' for _ in range(num_people)],
    'Age': [random.choice(ages) for _ in range(num_people)],
    'Gender': [random.choice(genders) for _ in range(num_people)],
    'Country': [random.choice(countries) for _ in range(num_people)],
    'family_history': [random.choice(family_history) for _ in range(num_people)],
    'treatment': [random.choice(treatment_options) for _ in range(num_people)],
    'work_interfere': [random.choice(work_interfere) for _ in range(num_people)],
    'num_employees': [random.choice(['1-5', '6-25', '26-100', '100-500', '500+']) for _ in range(num_people)],
    'remote_work': [random.choice(['Yes', 'No']) for _ in range(num_people)],
    'tech_company': [random.choice(['Yes', 'No']) for _ in range(num_people)],
    'benefits': [random.choice(['Yes', 'No', "Don't know"]) for _ in range(num_people)],
    'care_options': [random.choice(['Yes', 'No', "Not sure"]) for _ in range(num_people)],
    'wellness_program': [random.choice(['Yes', 'No', "Don't know"]) for _ in range(num_people)],
    'seek_help': [random.choice(['Yes', 'No', "Maybe"]) for _ in range(num_people)],
}

# 3. Turn it into a Pandas DataFrame
df = pd.DataFrame(data)

# 4. INTENTIONALLY ADD SOME "DIRTY" DATA (for us to clean later!)
# Add 20 random missing values in the 'Age' column
age_nan_indices = random.sample(range(num_people), 20)
df.loc[age_nan_indices, 'Age'] = np.nan

# Add 15 missing values in 'Country'
country_nan_indices = random.sample(range(num_people), 15)
df.loc[country_nan_indices, 'Country'] = np.nan

# Add 25 missing values in 'work_interfere'
work_nan_indices = random.sample(range(num_people), 25)
df.loc[work_nan_indices, 'work_interfere'] = np.nan

# Add some typos! Change a few "Yes" to "Y" and "No" to "N" in the treatment column
df.loc[random.sample(range(num_people), 15), 'treatment'] = 'Y'
df.loc[random.sample(range(num_people), 10), 'treatment'] = 'N'

# 5. Save it to a CSV file right in your project folder!
df.to_csv('mental_health_survey.csv', index=False)

print("="*50)
print("✅ SUCCESS! Dataset created successfully!")
print(f"   -> Created {len(df)} rows of survey data.")
print("   -> Saved as 'mental_health_survey.csv' in your project folder.")
print("   -> This file has missing values and typos (perfect for our next lesson!).")
print("="*50)
print("\nNOW CLOSE THIS TAB, and open your 'analysis.py' file.")
print("Click the green 'Play' arrow on 'analysis.py' to see your chart!")