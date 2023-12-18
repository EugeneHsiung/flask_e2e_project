import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, inspect
import pandas as pd
  
# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

load_dotenv()

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}")

# Create a database engine
db_engine = create_engine(conn_string, echo=False)

csv = '/home/eugenehsiung/flask_e2e_project/data/Clean-Pregnancy-Associated_Mortality.csv'
df = pd.read_csv(csv)

engine = create_engine(conn_string) # Create SQLAlchemy Engine
df.to_sql('pregnancy', con=engine, if_exists='replace', index=False) # Insert data into Azure SQL Database

# create database Eugene;
# use Eugene;
# create table pregnancy (current_year int, related varchar(200), Underlying_cause varchar(200), race_ethnicity varchar(200), Borough varchar(200), Deaths int);
# select * from pregnancy

# If success print "SQL Database success"
print("SQL Database success")
