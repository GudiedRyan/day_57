import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')

df.head()

df.columns

df.shape

df.isna()

df.tail()

clean_df = df.dropna()

# Highest mid career salary:

mid_max = clean_df['Mid-Career Median Salary'].idxmax()
print(clean_df['Undergraduate Major'].loc[mid_max], clean_df['Mid-Career Median Salary'].max())
# Chemical Engineering

# Lowest starting career salary:

min_start = clean_df['Starting Median Salary'].idxmin()
print(clean_df['Undergraduate Major'].loc[min_start], clean_df['Starting Median Salary'].min())

# lowest mid career salary:

mid_min = clean_df['Mid-Career Median Salary'].idxmin()
print(clean_df['Undergraduate Major'].loc[mid_min], clean_df['Mid-Career Median Salary'].loc[mid_min])

# Adding new column

spread_col = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
clean_df.insert(1, 'Spread', spread_col)

# Making a new table to view top 
high_risk = clean_df.sort_values('Spread', ascending=False)
high_risk[['Undergraduate Major', 'Spread']].head()