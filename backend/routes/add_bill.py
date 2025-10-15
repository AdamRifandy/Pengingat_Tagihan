from flask import Blueprint, request, jsonify
from services.db import get_db_connection

add_bill_bp = Blueprint("add_bill", __name__)

@add_bill_bp.route("/add_bill", methods=["POST"])
def add_bill():
    data = request.get_json()
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO all_bills VALUES (%s)", ())
    return jsonify({"message": "Data berhasil ditambahkan."}), 201
    