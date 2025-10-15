from flask import Blueprint, jsonify
from services.db import get_db_connection

remove_bill = Blueprint("remove_bill", __name__)

@remove_bill.route("/remove_bill/<int:id>", methods=["DELETE"])
def remove_bill(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM all_bills WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": f"Tagihan dengan id {id} berhasil dihapus."})