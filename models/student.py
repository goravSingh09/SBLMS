from models.db import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    # Auto Generated
    student_id = db.Column(db.String(20), unique=True, nullable=False)

    # Personal Details
    full_name = db.Column(db.String(100), nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    mother_name = db.Column(db.String(100), nullable=False)

    mobile = db.Column(db.String(15), unique=True, nullable=False)
    whatsapp = db.Column(db.String(15), nullable=False)
    emergency_contact = db.Column(db.String(15), nullable=False)

    aadhaar_number = db.Column(db.String(12), unique=True, nullable=False)

    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(20), nullable=False)

    address = db.Column(db.Text, nullable=False)

    preparing_for = db.Column(db.String(100), nullable=False)

    # Documents
    photo = db.Column(db.String(255), nullable=False)
    aadhaar_photo = db.Column(db.String(255), nullable=False)

    # Admin will update later
    seat_number = db.Column(db.String(20), nullable=True)
    monthly_fee = db.Column(db.Float, nullable=True)

    fee_status = db.Column(
        db.String(20),
        nullable=False,
        default="Pending"
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="Pending Approval"
    )

    joining_date = db.Column(db.Date, nullable=True)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )