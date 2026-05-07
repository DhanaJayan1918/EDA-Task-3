import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load your existing dataset
df = pd.read_csv('restaurant_data.csv')

# 2. Set the aesthetic style
sns.set_theme(style="whitegrid")

# 3. Create a Multi-Plot Report
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Plot 1: Revenue Distribution
sns.histplot(df['Revenue'], kde=True, ax=axes[0, 0], color='teal')
axes[0, 0].set_title('Distribution of Annual Revenue')

# Plot 2: Correlation Heatmap
numeric_df = df.select_dtypes(include=['float64', 'int64'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='YlGnBu', ax=axes[0, 1])
axes[0, 1].set_title('Feature Correlation Heatmap')

# Plot 3: Seating Capacity vs Revenue
sns.regplot(x='Seating Capacity', y='Revenue', data=df, ax=axes[1, 0], scatter_kws={'alpha':0.5})
axes[1, 0].set_title('Seating Capacity impact on Revenue')

# Plot 4: Marketing Budget vs Revenue
sns.scatterplot(x='Marketing Budget', y='Revenue', hue='Location', data=df, ax=axes[1, 1])
axes[1, 1].set_title('Marketing Budget by Location')

plt.tight_layout()
plt.show()