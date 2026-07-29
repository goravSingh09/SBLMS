from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired

from wtforms import (
    StringField,
    TextAreaField,
    SelectField,
    DateField,
    DecimalField,
    SubmitField
)

from wtforms.validators import (
    DataRequired,
    Length,
    Regexp,
    NumberRange
)


class AdmissionForm(FlaskForm):

    full_name = StringField(
        "Full Name",
        validators=[
            DataRequired(),
            Length(min=3, max=100)
        ]
    )

    father_name = StringField(
        "Father Name",
        validators=[
            DataRequired(),
            Length(min=3, max=100)
        ]
    )

    mother_name = StringField(
        "Mother Name",
        validators=[
            DataRequired(),
            Length(min=3, max=100)
        ]
    )

    mobile = StringField(
    "Mobile Number",
    validators=[
        DataRequired(),
        Length(min=10, max=10)
    ]
)
    whatsapp = StringField(
    "WhatsApp Number",
    validators=[
        DataRequired(),
        Length(min=10, max=10)
    ]
)

    emergency_contact = StringField(
    "Emergency Contact",
    validators=[
        DataRequired(),
        Length(min=10, max=10)
    ]
)

    aadhaar_number = StringField(
        "Aadhaar Number",
        validators=[
            DataRequired(),
            Regexp(r"^[0-9]{12}$", message="Enter valid Aadhaar number")
        ]
    )

    dob = DateField(
        "Date of Birth",
        validators=[DataRequired()],
        format="%Y-%m-%d"
    )

    gender = SelectField(
        "Gender",
        choices=[
            ("Male", "Male"),
            ("Female", "Female"),
            ("Other", "Other")
        ]
    )

    address = TextAreaField(
        "Address",
        validators=[DataRequired()]
    )

    preparing_for = SelectField(
        "Preparing For",
        choices=[
            ("UPSC", "UPSC"),
            ("RAS", "RAS"),
            ("SSC", "SSC"),
            ("Banking", "Banking"),
            ("Railway", "Railway"),
            ("NEET", "NEET"),
            ("JEE", "JEE"),
            ("College", "College"),
            ("School", "School"),
            ("Other", "Other")
        ]
    )

    seat_mode = SelectField(
        "Seat Mode",
        choices=[
            ("Auto", "Auto"),
            ("Manual", "Manual")
        ]
    )

    monthly_fee = DecimalField(
        "Monthly Fee",
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ]
    )

    photo = FileField(
        "Student Photo",
        validators=[
            FileRequired(),
            FileAllowed(["jpg", "jpeg", "png"])
        ]
    )

    aadhaar_photo = FileField(
        "Aadhaar Photo",
        validators=[
            FileRequired(),
            FileAllowed(["jpg", "jpeg", "png", "pdf"])
        ]
    )

    submit = SubmitField("Submit Admission")