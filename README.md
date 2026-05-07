# 🔍 Exploratory Data Analysis: Restaurant Performance
### Uncovering Patterns, Trends, and Influencing Factors

This project focuses on **Exploratory Data Analysis (EDA)** to understand the underlying mechanics of restaurant revenue. Instead of jumping straight to a model, this project dives deep into the data to identify correlations, detect outliers, and visualize the "story" behind the numbers.

---

## 🎯 Project Objectives
The goal of this analysis was to move beyond raw data and develop a structured understanding of how different variables influence financial outcomes.
* **Statistical Profiling:** Understanding the distribution and spread of key metrics.
* **Correlation Discovery:** Identifying which features (e.g., Marketing, Capacity) have the strongest impact on Revenue.
* **Outlier Detection:** Identifying "dirty" data points or unique business cases that deviate from the norm.
* **Visual Storytelling:** Presenting complex data relationships through intuitive charts.

---

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Visualization:** `seaborn`, `matplotlib`
* **Data Manipulation:** `pandas`, `numpy`

---

## 📊 Key Features & Visualizations

### 1. Statistical Summary
Generated comprehensive summaries (Mean, Median, Std Dev) to understand the scale of operations across the dataset.

### 2. Correlation Heatmap
Used a heatmap to quantify the relationship between features. 
> **Finding:** Identified that `Seating Capacity` and `Average Meal Price` have the highest positive correlation with `Revenue`.

### 3. Distribution Analysis
Used Histograms and KDE plots to check the "skewness" of Revenue. This helped determine if the market is dominated by small cafes or high-end restaurants.

### 4. Bivariate Regression Plots
Created regression lines to visualize the direct impact of the **Marketing Budget** on total turnover, helping to identify the "Return on Investment" trend.

---

## 💡 Key Insights & Findings
* **The "Sweet Spot":** Analysis showed that restaurants with a seating capacity between 40-60 often have the most stable revenue-to-cost ratio.
* **Marketing Impact:** There is a linear relationship between social media followers and revenue, but only up to a certain "saturation point."
* **Location Variance:** Urban locations show higher volatility in revenue compared to Suburban areas, despite having higher average sales.

---

## 🚀 How to Run the Analysis
1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/DhanaJayan1918/Restaurant-EDA-Task.git](https://github.com/DhanaJayan1918/Restaurant-EDA-Task.git)
