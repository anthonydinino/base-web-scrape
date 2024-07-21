from flask import Flask, request
from scraper import scrape

app = Flask(__name__)

@app.route("/")
def start():
  url = request.args.get('url')
  if not url:
    return "USAGE: localhost:8000?url=[url]"
  else:
    return scrape(url)



