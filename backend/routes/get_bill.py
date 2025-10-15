from flask import Blueprint, jsonify
from services.db import get_db_connection

get_bill_bp = Blueprint("get_bill_bp", __name__)

@get_bill_bp.route("/get_bill", methods=["GET"])
def bills():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM all_bills")
    bills = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(bills)