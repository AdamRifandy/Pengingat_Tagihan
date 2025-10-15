from flask import Blueprint, request, jsonify
from services.db import get_db_connection

edit_bill = Blueprint("edit_bill", __name__)

@edit_bill.route("/edit_bill/<int:id>", methods=["PUT"])
def edit_bill(id):
    data = request.get_json
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("UPDATE all_bills SET ", ())
    connection.commit()
    
    cursor.close()
    connection.close()
    
    return jsonify({"message": f"Tagihan dengan id {id} berhasil di edit."})