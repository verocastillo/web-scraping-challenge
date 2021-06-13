# Import modules
from flask import Flask, render_template, redirect
import pymongo
from scrape_mars import scrape

# Create instance
app = Flask(__name__)

# Setup Mongo connection
mongo = pymongo(app, uri="mongodb://localhost:27017/app")

# Main app route
@app.route("/")
def index():
    scrape = mongo.db.scrapes.find_one()
    return render_template("index.html", scrape=scrape)

# Scraping route
@app.route("/scrape")
def scraper():
    scrapes = mongo.db.scrapes
    scrape_data = scrape()
    scrapes.update({}, scrape_data, upsert=True)
    return redirect("/", code=302)

# Added so when file is ran, the function runs
if __name__ == "__main__":
    app.run(debug=True)