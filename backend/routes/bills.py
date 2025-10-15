from flask import Blueprint, jsonify
from services.db import get_db_connection

add_bill_bp = Blueprint("bills_bp", __name__)

@add_bill_bp.route("/bills", methods=["GET"])
def bills():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM all_bills")
    bills = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(bills)