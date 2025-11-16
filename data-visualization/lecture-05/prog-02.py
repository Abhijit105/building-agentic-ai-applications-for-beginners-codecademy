# Exploration of data
# Exploratory data analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./Customer-Churn (1).csv")
print(df.head(5))
print(df.tail(10))
print(df.info())

# data cleaning
df.dropna(subset=['TotalCharges'])
print(df.info())

print(df.tenure_bins.value_count())
