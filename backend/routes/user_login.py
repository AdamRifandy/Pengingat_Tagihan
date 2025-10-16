from flask import Blueprint, request, jsonify, session
from services.db import SessionLocal
from services.models import User

user_login_bp = Blueprint("user_login", __name__)

@user_login_bp.route("/login", methods=["POST"])
def login():
    db = SessionLocal()
    data = request.get_json()
    
    user = db.query(User).filter_by(username=data["username"], email=data["email"], password=data["password"]).first()
    db.close()
    
    if not user:
        return jsonify({"error": f"Login gagal, username, email atau password salah!"}), 401
    
    session["user_id"] = user.id
    session["username"] = user.username
    
    return jsonify({"message": f"Login berhasil, selamat datang {user.username}!"})