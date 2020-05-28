from flask import render_template, request

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def form_response():
    username = request.form['username']
    password = request.form['password']
    hashtags = request.form['hashtags']
    print(username)
    run_scraper(username, password, hashtags)
    return render_template("index.html")

def run_scraper(username, password, hashtags):
    from app import scraper
    if len(hashtags) > 1:
        hashtags = hashtags.split(',')
    me = scraper.InstagramBot(username, password)
    me.login()
    print("Logged in as " + username)
    for hashtag in hashtags:
        print("in loop in views.py")
        me.like_posts_in(hashtag)
        print("Back to loop in views.py")


@app.route('/about')
def about():
    return render_template("about.html")