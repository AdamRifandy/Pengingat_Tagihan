from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, Date, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from .db import Base

class BillStatus(enum.Enum):
    BELUM_BAYAR = 'Belum dibayar'
    LUNAS = 'Lunas'

class ReminderStatus(enum.Enum):
    TERKIRIM = 'Terkirim'
    GAGAL = 'Gagal'

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    
    bills = relationship("Bill", back_populates="author", cascade="all, delete")

class Bill(Base):
    __tablename__ = "bills"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    bill_name = Column(String(100), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    due_date = Column(Date, nullable=False)
    status = Column(Enum(BillStatus), default=BillStatus.BELUM_BAYAR) # ENUM
    created_at = Column(DateTime, default=datetime.utcnow) # Timestamp
    # foreign key
    author = relationship("User", back_populates="bills")
    
    reminders = relationship("Reminder", back_populates="to_bill", cascade="all, delete")

class Reminder(Base):
    __tablename__ = "reminders"
    
    id = Column(Integer, primary_key=True)
    bill_id = Column(Integer, ForeignKey("bills.id", ondelete="CASCADE"), nullable=False)
    reminder_date = Column(Date, nullable=False) # date
    status = Column(Enum(ReminderStatus), default=ReminderStatus.TERKIRIM) # enum
    # foreign bill_id column with reference table bills column id
    to_bill = relationship("Bill", back_populates="reminders")
