# %%
import pandas as pd

df = pd.read_csv('rides.csv')
df
# %%
nullmask = df.isnull().any(axis=1)
df[nullmask]
# Find out all the rows that have bad values
plate_mask = ~df['plate'].str.match(r'^[0-9A-Z]{3,}', na=False)
df[plate_mask]
# - Missing values are not allowed
# - A plate must be a combination of at least 3 upper case letters or digits
# - Distance much be bigger than 0
# %%
