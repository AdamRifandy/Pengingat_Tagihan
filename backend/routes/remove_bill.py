from flask import Blueprint, jsonify

remove_bill_bp = Blueprint("remove_bill", __name__)

@remove_bill_bp.route("/remove_bill/<int:id>", methods=["DELETE"])
def remove_bill(id):
    
    return jsonify({"message": f"Tagihan dengan id {id} berhasil dihapus."})