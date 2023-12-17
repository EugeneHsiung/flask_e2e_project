from flask import Flask, render_template, request, redirect
import pandas as pd
import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, text
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
import csv



app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

load_dotenv()  # Load environment variables from .env file

# Connection string
connect_args={'ssl':{'fake_flag_to_enable_tls': True}}

connection_string = (f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
                    f"?charset={DB_CHARSET}")

engine = create_engine(
        connection_string,
        connect_args=connect_args,

)

## Connection settings for the Goolge OAuth
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('home.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')


df = pd.read_csv('/home/eugenehsiung/flask_e2e_project/data/Clean-Pregnancy-Associated_Mortality.csv')
@app.route('/data')
def data():
    # sample of 50
    df = pd.read_csv('/home/eugenehsiung/flask_e2e_project/data/Clean-Pregnancy-Associated_Mortality.csv').sample(50)
    return render_template('data.html', data=df)




if __name__ == '__main__':
    app.run(debug=True)





