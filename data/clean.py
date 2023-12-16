import pandas as pd

# import the dataset
df= pd.read_csv('/home/eugenehsiung/flask_e2e_project/data/Pregnancy-Associated_Mortality.csv')
df

df.shape # count dimensions: rows by columns 

df.isnull().sum() # missing values count

df_clean = df.dropna() # remove missing values
df_clean


df_clean.to_csv('/home/eugenehsiung/flask_e2e_project/data/Clean-Pregnancy-Associated_Mortality.csv', index=False) # creates and exports df into new csv file
