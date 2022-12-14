from flask import Flask, render_template, jsonify
from flask_cors import CORS
import os

# configuration
DEBUG = True

# instantiate the app
template_dir = os.path.abspath('../../frontend/')
print(template_dir)
template_dir = os.path.join(template_dir, 'client')
template_dir = os.path.join(template_dir, 'public')

app = Flask(__name__, template_folder=template_dir)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()