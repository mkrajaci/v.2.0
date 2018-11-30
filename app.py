from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Mario',
        'title': 'Prvi blog',
        'content': 'Prvi sadrzaj',
        'date_posted': '28.11.2018.'
    },
    {
        'author': 'Marija',
        'title': 'Drugi blog',
        'content': 'Drugi sadrzaj',
        'date_posted': '29.11.2018.'
    }
]

@app.route('/')
@app.route('/home')
def home():                             # posts koristim za referencu u htmlu
    return render_template('home.html', posts=posts) # mjesto gdje odredjujem koji html rederira

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
