import pandas as pd
import numpy as np
import statsmodels.api as sm

# Defining the data
data = {
    'Year': np.arange(2013, 2024),  # Years from 2013 to 2023
    'Reports': [
        3095, 5268, 6221, 7494, 7760,
        7872, 8928, 9606, 10941, 11959, 12689
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