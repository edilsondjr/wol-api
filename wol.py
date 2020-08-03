import flask
import os

app = flask.Flask(__name__)

from views import *

if __name__ == '__main__':
    if os.environ.get('PORT'):
        port = os.environ.get('PORT')
        app.run(debug=True, host='0.0.0.0', port=port)
    else:
        app.run(debug=True, host='0.0.0.0', port=5000)