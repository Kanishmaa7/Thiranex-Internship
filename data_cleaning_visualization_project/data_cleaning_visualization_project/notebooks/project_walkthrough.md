# Data Cleaning & Visualization Walkthrough

This file is a notebook-style guide for the project.

## 1. Import libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
```

## 2. Load the raw dataset

```python
df = pd.read_csv("data/raw/retail_sales_raw.csv")
df.head()
```

## 3. Understand the data

```python
df.shape
df.info()
df.describe(include="all")
df.isna().sum()
df.duplicated().sum()
```

## 4. Clean the data

The project:
- standardizes column names
- converts dates and numeric fields
- removes exact duplicate rows
- fills missing categorical values with `Unknown`
- fills numeric missing values using the median
- detects extreme values with the IQR method
- caps extreme quantity and price values
- recalculates revenue and profit

## 5. Create visualizations

The project generates:
1. Monthly revenue trend
2. Revenue by region
3. Profit by category
4. Revenue by product
5. Quantity vs revenue scatter plot

## 6. Storytelling

Use the charts to answer:
- How does revenue change over time?
- Which region contributes the most revenue?
- Which category generates the most profit?
- Which products contribute most to revenue?
- Does higher quantity generally relate to higher revenue?

## 7. Key learning

The important workflow is:

**Raw Data → Data Understanding → Cleaning → Outlier Treatment → Feature Calculation → Visualization → Insights**
