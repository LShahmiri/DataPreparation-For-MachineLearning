import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

data_df= pd.DataFrame({"A":[5,5,2,2,5],
                      "B":[2,2,3,3,4],
                      "C":[5,1,5,np.nan,21]})


knn_imputer = KNNImputer()
knn_imputer = KNNImputer(n_neighbors = 1) 
knn_imputer = KNNImputer(n_neighbors = 2) 
knn_imputer.fit_transform(data_df)


knn_imputer = KNNImputer(n_neighbors = 3, weights= "distance") 
knn_imputer.fit_transform(data_df)

data_df1 = pd.DataFrame(knn_imputer.fit_transform(data_df), columns = data_df.columns)