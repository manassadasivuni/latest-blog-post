import feedparser
from flask import Flask, redirect


feed = feedparser.parse('https://manassadasivuni.com/feed') # parses xml feed
latestLink = feed['entries'][0]['link'] # gets latest entry from the feed

app = Flask(__name__)
@app.route('/')
def home():
    return redirect(latestLink) # redirects to the latest entry

app.run()