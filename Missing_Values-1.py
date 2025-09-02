import pandas as pd
import numpy as np

data_df = pd.DataFrame({"A":[1,2,9,np.nan,8,np.nan,7,6],
                      "B":[4,np.nan,7,np.nan,1,np.nan,2,9]})

# Missing Values Finding with Pandas
data_df.isna()
data_df.isna().sum()
data_df.dropna(how=any)
data_df.dropna(how=all)
data_df.fillna(value=100)



