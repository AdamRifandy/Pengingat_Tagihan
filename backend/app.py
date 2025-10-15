from flask import Flask
from flask_cors import CORS
from routes import bills_bp, add_bill_bp, edit_bill_bp, remove_bill_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(bills_bp)
app.register_blueprint(add_bill_bp)
app.register_blueprint(edit_bill_bp)
app.register_blueprint(remove_bill_bp)

app.run(debug=True)