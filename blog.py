#import libraries
from flask import Flask, render_template, url_for

app = Flask(__name__)

# index route / landing page
@app.route('/')
def home():
    return render_template('home.html')

# about page
@app.route('/about')
def about():
    return render_template('about.html')




if __name__ == '__main__':
    app.run(debug = True)
