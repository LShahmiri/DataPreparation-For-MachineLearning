
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

X = pd.DataFrame({"input1": [1,2,3,4,5],
                  "input2": ["A","C","B","B","C"],
                  "input3": ["X","Y","X","Y","Y"],})


categorical_val = ["input2", "input3"]

one_hot_encoder = OneHotEncoder(sparse_output= False)

encoder_vars_arrays = one_hot_encoder.fit_transform(X[categorical_val])


encoder_features_name = one_hot_encoder.get_feature_names_out(categorical_val)


encoder_vars_df = pd.DataFrame(encoder_vars_arrays, columns=encoder_features_name)


X_new = pd.concat([X.reset_index(drop=True),encoder_vars_df.reset_index(drop=True)], axis=1)


one_hot_encoder = OneHotEncoder(sparse_output= False, drop="first")
