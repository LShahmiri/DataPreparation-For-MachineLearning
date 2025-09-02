import pandas as pd
import numpy as np

data_df = pd.DataFrame({"A":[6,6,4,np.nan,5,np.nan,1],
                      "B":[1,np.nan,5,np.nan,8,np.nan,3]})
data_df.isna()
data_df.isna().sum()

# Dropping Missing Values 
data_df.dropna() 
data_df.dropna(how="any")
data_df.dropna(how="all")
data_df.dropna(how="any", subset = ["A"])
data_df.dropna(how="any", inplace = True)


data_df = pd.DataFrame({"A":[6,7,1,np.nan,5,np.nan,7],
                      "B":[3,np.nan,6,np.nan,2,np.nan,3]})

data_df.fillna(value=100)

mean_value = data_df["A"].mean()
data_df["A"].fillna(value = mean_value)
"""Get mean of each column and apply on correspondent column"""
data_df.fillna(value = data_df.mean(), inplace=True)