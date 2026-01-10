from flask import Flask,request, render_template,redirect,url_for
from werkzeug.utils import secure_filename
import os

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

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return 'ファイルが選択されていません'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
        else:
            return '許可されていないファイル形式です'
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return f'アップロード完了: <br><img src="/static/uploads/{filename}" width="300">'

@app.route('/gallery')
def gallery():
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('gallery.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)

