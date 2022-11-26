https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from util.DB_Interface import DB

app = Flask(__name__)
app.config['ERROR_404_HELP'] = False
CORS(app)
api = Api(app)
db = DB()
