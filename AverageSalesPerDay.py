import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Make sure to import seaborn

# Read the data
train_data = pd.read_csv('Data/train.csv')

# Convert the 'date' column to datetime format
train_data['date'] = pd.to_datetime(train_data['date'])

# Extract day of the month
train_data['day_of_month'] = train_data['date'].dt.day

# Aggregate sales by day of the month
avg_sales_by_day = train_data.groupby('day_of_month')['sales'].mean().reset_index()

# Get the minimum sales value
min_sales = avg_sales_by_day['sales'].min()

# Plotting average sales by day of the month
plt.figure(figsize=(10, 6))
sns.barplot(data=avg_sales_by_day, x='day_of_month', y='sales', color='skyblue')

# Highlight the 15th and last day
plt.axvline(x=14, color='red', linestyle='--', label='15th of the Month')
plt.axvline(x=avg_sales_by_day['day_of_month'].max() - 0.5, color='orange', linestyle='--', label='Last Day of the Month')

# Set y-axis limit to start just below the minimum average sales
plt.ylim(min_sales - 50, avg_sales_by_day['sales'].max() * 1.1)  # Adjust range as needed

# Set titles and labels
plt.title('Average Sales by Day of the Month')
plt.xlabel('Day of the Month')
plt.ylabel('Average Sales')
plt.legend()
plt.grid(True)
plt.show()

