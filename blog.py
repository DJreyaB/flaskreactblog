#import libraries
from flask import Flask


app = Flask(__name__)

# index route / landing page
@app.route('/')
def home():
    pass




if __name__ == '__main__':
    app.run(debug = True)
