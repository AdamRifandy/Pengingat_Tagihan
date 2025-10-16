from flask import Blueprint, request, jsonify, session
from services.db import SessionLocal
from services.models import Bill

add_bill_bp = Blueprint("add_bill", __name__)

@add_bill_bp.route("/add_bill", methods=["POST"])
def add_bill():
    data = request.get_json
    
    db = SessionLocal()
    user_identifier = session.get("user_id")
    
    new_bill = Bill(user_id=user_identifier, bill_name=data["bill_name"], amount=data["amount"], due_date=data["due_date"])
    db.add(new_bill)
    db.commit()
    db.refresh(new_bill)
    db.close()
    
    return jsonify({"message": "Data berhasil ditambahkan."}), 201
    