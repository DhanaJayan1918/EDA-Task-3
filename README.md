# 📈 Financial Time-Series Prediction: Apple Inc. (AAPL)
### Real-World Data Project - Finance Domain

This project applies machine learning to financial markets, specifically predicting the closing price of Apple Inc. (AAPL). Unlike static datasets, this project handles **Time-Series data**, focusing on historical trends, moving averages, and market volatility.

---

## 🏛️ Domain Context: Finance
In the financial world, data is sequential. This project explores the "Random Walk" theory and attempts to identify signals in the noise of daily stock fluctuations using historical price data.

### 🔑 Key Features
* **Live Data Acquisition:** Integrated `yfinance` API to fetch real-time and historical market data.
* **Technical Indicators:** Engineered features like Simple Moving Averages (SMA-20, SMA-50) and Daily Returns.
* **Time-Series Split:** Utilized chronological splitting (instead of random) to respect the timeline of financial events.
* **Volatility Analysis:** Visualized price "Bollinger Bands" to understand market risk.

---

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **APIs:** `yfinance` (Yahoo Finance)
* **Libraries:** `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `plotly`

---

## 🧪 The Modeling Workflow
1. **Data Collection:** Pulling 5 years of daily OHLC (Open, High, Low, Close) data.
2. **Preprocessing:** Handling market holidays (missing values) and scaling prices for the algorithm.
3. **Feature Engineering:** * *Lag Features:* Using yesterday's price to predict today's.
    * *Rolling Windows:* Calculating the trend over the last 14 days.
4. **Prediction:** Using a **Random Forest Regressor** to predict the next day's 'Close' price.

---

## 📈 Evaluation & Visuals
Financial models are evaluated on their ability to follow the trend rather than just a single $R^2$ score.

| Metric | Result |
| :--- | :--- |
| **MAE (Mean Absolute Error)** | *[Insert Your Value, e.g., $2.40]* |
| **MAPE (Mean Absolute % Error)** | *[Insert Your Value, e.g., 1.2%]* |

### **Project Insights**


* **Trend Following:** The model successfully identified long-term bullish/bearish trends.
* **Lag Analysis:** Identified that 'Volume' has a secondary influence on price spikes.

---

## 🚀 Installation & Usage
1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/DhanaJayan1918/Financial-Prediction-Task.git](https://github.com/DhanaJayan1918/Financial-Prediction-Task.git)
