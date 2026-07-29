from models.student import Student


def generate_student_id():
    """
    Generate Student ID
    Example:
    SBL0001
    SBL0002
    SBL0003
    """

    last_student = (
        Student.query
        .order_by(Student.id.desc())
        .first()
    )

    if last_student is None:
        return "SBL0001"

    last_number = int(last_student.student_id.replace("SBL", ""))

    new_number = last_number + 1

    return f"SBL{new_number:04d}"