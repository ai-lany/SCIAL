from flask import Flask, jsonify, request,render_template, redirect, url_for
import requests
from flask_dance.contrib.google import make_google_blueprint, google
from rich import print, pretty
import endpoints
from requests_oauthlib import OAuth2Session
from dotenv import dotenv_values
import os
import json

from google.oauth2 import id_token, credentials
from google.auth.transport import requests as g_requests
import google_auth_oauthlib.flow

app = Flask(__name__)
pretty.install()

config = dotenv_values("secrets.env") 

GOOGLE_CLIENT_ID = config['OAUTH_GOOGLE_CLIENT_ID']
GOOGLE_CLIENT_SECRET = config['OAUTH_GOOGLE_CLIENT_SECRET']
app.secret_key = config['secret_key']

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

blueprint = make_google_blueprint(
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    reprompt_consent=True,
    scope=["profile","email"]
)

app.register_blueprint(blueprint,url_prefix="/login")


@app.route('/')
def index():
    google_data = None
    user_info_endpoint = '/oauth2/v2/userinfo'
    if google.authorized:
        google_data = google.get(user_info_endpoint).json()
        print(google_data)
    if google_data == None:
        return "none"
    res = requests.get(url = google.base_url + user_info_endpoint, params = google_data)
    print(os.environ['OAUTHLIB_INSECURE_TRANSPORT'])
    return res.json()


@app.route('/login')
def login():
    return redirect(url_for('google.login'))



@app.route('/ig_posts')
def getIGPosts():
    data = request.get_json()
    result = getIGPosts(data['userID'])
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)