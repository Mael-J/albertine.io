#this_file = "venv/bin/activate_this.py"
#exec(open(this_file).read(), {'__file__': this_file})

from flask import Flask
from flask.helpers import send_from_directory

from api.funds import funds

from flask_cors import CORS, cross_origin
application = Flask(__name__, static_folder='../client/build', static_url_path='')
CORS(application)

#funds Router
application.register_blueprint(funds)

@application.route('/', methods = ["GET"])
def serve():
    return send_from_directory(application.static_folder, 'index.html')



if __name__ == '__main__':
    # from waitress import serve
    # print('app running...')
    # serve(app, host = '0.0.0.0', port = 4000)
    application.run(debug=True, port = 4000)
    