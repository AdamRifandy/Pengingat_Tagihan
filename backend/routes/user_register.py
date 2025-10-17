from flask import Blueprint, request, jsonify
from services.db import SessionLocal
from services.models import User

user_register_bp = Blueprint("user_register", __name__)

@user_register_bp.route("/register", methods=["POST"])
def register():
    db = SessionLocal()
    data = request.get_json()
    
    new_user = User(username=data["username"], email=data["email"], password=data["password"])
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    
    return jsonify({"message": f"User berhasil register."})