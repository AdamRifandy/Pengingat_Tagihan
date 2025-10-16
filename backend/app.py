from flask import Flask
from flask_cors import CORS
from routes import get_bill_bp, add_bill_bp, edit_bill_bp, remove_bill_bp, user_login_bp
from services.db import init_db
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

app.secret_key = os.getenv("SECRET_KEY")
init_db()

app.register_blueprint(user_login_bp)
app.register_blueprint(get_bill_bp)
app.register_blueprint(add_bill_bp)
app.register_blueprint(edit_bill_bp)
app.register_blueprint(remove_bill_bp)

app.run(debug=True)