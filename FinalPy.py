import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('final.csv')
grouped = df.groupby(['zip_code', 'item_description'])[['bottles_sold', 'sale_dollars']].sum().reset_index()
most_popular = grouped.loc[grouped.groupby('zip_code')['bottles_sold'].idxmax()]
most_popular['percent_sales'] = most_popular.groupby('zip_code')['bottles_sold'].apply(lambda x: 100 * x / x.sum())

colors = plt.cm.get_cmap('tab20').colors
for i, (zip_code, group) in enumerate(most_popular.groupby('zip_code')):
    plt.scatter(group['zip_code'], group['bottles_sold'], c=colors[i % len(colors)])

plt.ylabel('Bottles Sold')
plt.xlabel('Zip Code')
plt.legend()
plt.show()

most_popular.to_csv('result.csv', index=False)
