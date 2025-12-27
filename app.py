from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile/<username>')
def profile(username):
    age = 22
    hobbies = ['プログラミング', '音楽', '映画鑑賞']
    return render_template('profile.html', username=username, age=age, hobbies=hobbies)

@app.route('/mypage')
def mypage():
    return render_template('mypage.html')