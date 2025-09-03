# Feature Selection using a simple Correlation Matrix

import pandas as pd
my_df = pd.read_csv("feature_selection_sample_data.csv")

correlation_matrix = my_df.corr()
"""
          output    input1    input2    input3    input4
output  1.000000  0.789747  0.795518 -0.128295  0.086331
input1  0.789747  1.000000  0.610206 -0.140955  0.074541
input2  0.795518  0.610206  1.000000 -0.128990  0.121853
input3 -0.128295 -0.140955 -0.128990  1.000000 -0.020888
input4  0.086331  0.074541  0.121853 -0.020888  1.000000
"""

