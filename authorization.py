from requests_oauthlib import OAuth2Session
from dotenv import dotenv_values
import os
from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
import logging

config = dotenv_values("secrets.env") 

GOOGLE_CLIENT_ID = config['OAUTH_GOOGLE_CLIENT_ID']
GOOGLE_CLIENT_SECRET = config['OAUTH_GOOGLE_CLIENT_SECRET']
app.secret_key = config['secret_key']


