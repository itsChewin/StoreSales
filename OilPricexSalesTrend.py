import pandas as pd
import matplotlib.pyplot as plt

# Read the data
train_data = pd.read_csv('Data/train.csv')
oil_data = pd.read_csv('Data/oil.csv')

# Convert 'date' to datetime format
train_data['date'] = pd.to_datetime(train_data['date'])
oil_data['date'] = pd.to_datetime(oil_data['date'])

# Merge train data with oil prices on 'date'
train_data = pd.merge(train_data, oil_data, on='date', how='left')

# Aggregating the sales data by date and summing the sales
sales_oil_data = train_data.groupby('date').agg({'sales': 'sum', 'dcoilwtico': 'mean'}).reset_index()

# Fill NaN values for sales and oil prices
sales_oil_data['sales'].fillna(0, inplace=True)
sales_oil_data['dcoilwtico'].fillna(method='ffill', inplace=True)  # Forward fill for oil price

# Smoothing the sales data using a rolling window
sales_oil_data['sales_smooth'] = sales_oil_data['sales'].rolling(window=50).mean()

# Smoothing the oil price data using a rolling window
sales_oil_data['dcoilwtico_smooth'] = sales_oil_data['dcoilwtico'].rolling(window=10).mean()

# Create a plot with two y-axes
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot smoothed Sales on the left y-axis
ax1.set_xlabel('Date (Monthly)')
ax1.set_ylabel('Sales', color='blue')
ax1.plot(sales_oil_data['date'], sales_oil_data['sales_smooth'], color='blue', label='Sales (Smoothed)', linewidth=2)
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis to plot smoothed Oil Price
ax2 = ax1.twinx()
ax2.set_ylabel('Oil Price', color='red')
ax2.plot(sales_oil_data['date'], sales_oil_data['dcoilwtico_smooth'], color='red', label='Oil Price (Smoothed)', linewidth=2)
ax2.tick_params(axis='y', labelcolor='red')

# Add title and grid
plt.title('Monthly Oil Price and Sales Trend')
plt.grid(True)

# Improve layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
