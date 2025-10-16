from flask import Blueprint, jsonify, session
from services.db import SessionLocal
from services.models import Bill

get_bill_bp = Blueprint("get_bill_bp", __name__)

@get_bill_bp.route("/get_bill", methods=["GET"])
def bills():
    db = SessionLocal()
    user_id = session.get("user_id")
    all_bill = db.query(Bill).filter_by(user_id=user_id).all()
    results = [
        {"bill_name": all_data.bill_name, "amount": all_data.amount, "due_date": all_data.due_date, "status": all_data.status}
        for all_data in all_bill
    ]
    
    db.close()
    return jsonify(results)