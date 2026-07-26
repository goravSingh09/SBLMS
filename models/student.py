from models.db import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.String(20), unique=True, nullable=False)

    full_name = db.Column(db.String(100), nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    mother_name = db.Column(db.String(100), nullable=False)

    mobile = db.Column(db.String(15), nullable=False)
    whatsapp = db.Column(db.String(15), nullable=False)
    emergency_contact = db.Column(db.String(15), nullable=False)

    aadhaar_number = db.Column(db.String(20), unique=True, nullable=False)

    dob = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(20), nullable=False)

    address = db.Column(db.Text, nullable=False)

    preparing_for = db.Column(db.String(100), nullable=False)

    seat_mode = db.Column(db.String(20), default="Auto")
    seat_number = db.Column(db.String(20))

    monthly_fee = db.Column(db.Float)

    fee_status = db.Column(db.String(20), default="Pending")

    status = db.Column(db.String(20), default="Pending Approval")

    photo = db.Column(db.String(255), nullable=False)
    aadhaar_photo = db.Column(db.String(255), nullable=False)

    joining_date = db.Column(db.String(20))

    created_at = db.Column(db.DateTime, server_default=db.func.now())

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )