import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load Dataset
train_data = pd.read_csv('Data/train.csv')
oil_data = pd.read_csv('Data/oil.csv')
store_data = pd.read_csv('Data/stores.csv')
holiday_data = pd.read_csv('Data/holidays_events.csv')
transaction_data = pd.read_csv('Data/transactions.csv')

# Convert 'date' to datetime format
train_data['date'] = pd.to_datetime(train_data['date'])
oil_data['date'] = pd.to_datetime(oil_data['date'])
holiday_data['date'] = pd.to_datetime(holiday_data['date'])
transaction_data['date'] = pd.to_datetime(transaction_data['date'])

# Filling missing oil prices
full_date_range = pd.date_range(start=oil_data['date'].min(), end=oil_data['date'].max())
full_date_df = pd.DataFrame({'date': full_date_range})
oil_data = pd.merge(full_date_df, oil_data, on='date', how='left')
oil_data['dcoilwtico'] = oil_data['dcoilwtico'].interpolate(method='linear')


pd.set_option('display.max_rows', None)
print(train_data.head())
print(oil_data.head())
print(store_data.head())
print(holiday_data.head())
print(transaction_data.head())