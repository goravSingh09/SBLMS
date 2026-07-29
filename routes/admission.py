from datetime import date

from flask import Blueprint, render_template, redirect, url_for, flash

from forms.admission_form import AdmissionForm
from models.db import db
from models.student import Student

from services.student_id_service import generate_student_id
from services.upload_service import save_file

admission_bp = Blueprint("admission", __name__)


@admission_bp.route("/admission", methods=["GET", "POST"])
def admission():

    form = AdmissionForm()

    # ==========================
    # DEBUGGING START
    # ==========================

    if form.validate_on_submit():

        print("✅ VALID FORM")

        photo_path = save_file(form.photo.data, "photos")

        aadhaar_path = save_file(form.aadhaar_photo.data, "aadhaar")

        student = Student(

            student_id=generate_student_id(),

            full_name=form.full_name.data,

            father_name=form.father_name.data,

            mother_name=form.mother_name.data,

            mobile=form.mobile.data,

            whatsapp=form.whatsapp.data,

            emergency_contact=form.emergency_contact.data,

            aadhaar_number=form.aadhaar_number.data,

            dob=form.dob.data,

            gender=form.gender.data,

            address=form.address.data,

            preparing_for=form.preparing_for.data,

            photo=photo_path,

            aadhaar_photo=aadhaar_path,

            status="Pending Approval",

            fee_status="Pending",

            joining_date=date.today()

        )

        db.session.add(student)

        db.session.commit()

        flash(
            "Admission submitted successfully!",
            "success"
        )

        return redirect(url_for("admission.admission"))

    else:

     if form.is_submitted():

        print("❌ FORM ERRORS")
        print(form.errors)

        print("Mobile Value :", repr(form.mobile.data))
        print("WhatsApp Value :", repr(form.whatsapp.data))
        print("Emergency Value :", repr(form.emergency_contact.data))

    # ==========================
    # DEBUGGING END
    # ==========================

    return render_template(
        "admission.html",
        form=form
    )