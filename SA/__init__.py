from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '8f22a1e5dedd9923b250ebdff40c3732'

from SA import routes