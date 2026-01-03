from flask import Flask,request, render_template

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

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['input_name']
    age = request.form['input_age']
    blood_type = request.form['input_blood_type']
    birthday = request.form['input_birthday']
    error = None

    if not name or not age or not blood_type or not birthday:
        error = '全ての項目を入力してください'
    
    return render_template('result.html', front_name=name, front_age=age, front_blood_type=blood_type,front_birthday=birthday,error=error)

@app.route('/search')
def search():
    query = request.args.get('q')
    return f'検索ワード: {query}'
