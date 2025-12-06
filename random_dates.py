#calculator for random dates in csv file - calculating dates difference

import numpy as np
import pandas as pd

# Load random dates from CSV file
random_dates = pd.read_csv('random_dates.csv')
print(random_dates.head(1))

# Convert to datetime64[D] format
random_dates = random_dates.iloc[:,0].values.astype('datetime64[D]')

# Get today's date
date_today = np.datetime64('today', 'D')    
print("Today's date:")
print(date_today)

date_difference = date_today - random_dates

# Create a DataFrame to store results
result =pd.DataFrame(
    {
    'random_date' : random_dates,
    'difference_in_days' : date_difference
})

print(result)
result.to_csv('date_differences.csv', index=False)



