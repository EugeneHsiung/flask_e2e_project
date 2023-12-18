from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, url_for, redirect, session
import pandas as pd
import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, text
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
import csv
from flask import Flask, url_for
from flask import Flask
from db_functions import update_or_create_user



#import sentry_sdk
#from db_functions import update_or_create_user


#sentry_sdk.init(
    #dsn=,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    #traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    #profiles_sample_rate=1.0,
#)


app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


load_dotenv()  # Load environment variables from .env file

# Connection string
connect_args={'ssl':{'fake_flag_to_enable_tls': True}}

conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}")

engine = create_engine(
        connection_string,
        connect_args=connect_args,

)

## Connection settings for the Goolge OAuth
GOOGLE_CLIENT_ID = '736457988361-bqsfd7kko0kfcn4qvbjqajmgr1ccbj0u.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'

app = Flask(__name__)
app.secret_key = os.urandom(12)
oauth = OAuth(app)

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


# Google OAuth
@app.route('/google/')
def google():
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    ###note, if running locally on a non-google shell, do not need to override redirect_uri
    ### and can just use url_for as below
    redirect_uri = url_for('google_auth', _external=True)
    print('REDIRECT URL: ', redirect_uri)
    session['nonce'] = generate_token()
    ##, note: if running in google shell, need to override redirect_uri 
    ## to the external web address of the shell, e.g.,
    redirect_uri = 'https://5000-cs-340668953872-default.cs-us-east1-pkhd.cloudshell.dev/google/auth/'
    return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])

@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = user
    update_or_create_user(user)
    print(" Google User ", user)
    return redirect('/dashboard')

@app.route('/dashboard/')
def dashboard():
    user = session.get('user')
    if user:
        return render_template('dashboard.html', user=user)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)





