from flask import Blueprint, request, jsonify

edit_bill_bp = Blueprint("edit_bill", __name__)

@edit_bill_bp.route("/edit_bill/<int:id>", methods=["PUT"])
def edit_bill(id):
    data = request.get_json
    
    return jsonify({"message": f"Tagihan dengan id {id} berhasil di edit."})