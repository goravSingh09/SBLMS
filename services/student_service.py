from database.database import get_connection


def save_student(student):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO students(

        student_id,

        full_name,

        father_name,

        mother_name,

        mobile,

        whatsapp,

        dob,

        gender,

        address,

        preparing_for,

        seat_number,

        seat_mode,

        monthly_fee,

        fee_status,

        status,

        photo,

        aadhaar_photo,

        joining_date

    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

    """,

    (

        student.student_id,

        student.full_name,

        student.father_name,

        student.mother_name,

        student.mobile,

        student.whatsapp,

        student.dob,

        student.gender,

        student.address,

        student.preparing_for,

        student.seat_number,

        student.seat_mode,

        student.monthly_fee,

        student.fee_status,

        student.status,

        student.photo,

        student.aadhaar_photo,

        student.joining_date

    )

    )

    conn.commit()

    conn.close()