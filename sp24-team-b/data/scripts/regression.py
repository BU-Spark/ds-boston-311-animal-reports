import pandas as pd
import numpy as np
import statsmodels.api as sm

# Defining the data
data = {
    'Year': np.arange(2013, 2024),  # Years from 2013 to 2023
    'Reports': [
        5530, 7802, 8887, 11052, 11343,
        11013, 11855, 13511, 14997, 16741, 17070
    ]
}

df = pd.DataFrame(data)

# Prepare the independent variable (Year) by adding a constant for the intercept
X = sm.add_constant(df['Year'])

# Dependent variable (Reports)
Y = df['Reports']

# Fit the model
model = sm.OLS(Y, X).fit()

print(model.summary())
