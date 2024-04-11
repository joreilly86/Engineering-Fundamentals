import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('flows.csv', parse_dates=['time'])

# Print the first few rows
print(df.head())

# Get basic information about the DataFrame
print(df.info())

# Describe the data (summary statistics)
print(df.describe())

# Filter data based on a condition
print(df[df['flow'] > 35])

# Group data by day and calculate mean flow
daily_mean = df.groupby(pd.Grouper(key='time', freq='D')).mean()
print(daily_mean)

# Plot the data
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(df['time'], df['flow'])
plt.xlabel('Time')
plt.ylabel('Flow (m³/s)')
plt.title('River Flow over Time')
plt.show()

# Resample data to a different frequency (e.g., hourly to daily)
daily_flows = df.resample('D', on='time').mean()
print(daily_flows)

# Handle missing data
print(df.isnull().sum())  # Check for missing values
df = df.dropna()  # Drop rows with missing values

# Write the DataFrame back to a CSV file
df.to_csv('cleaned_flows.csv', index=False)