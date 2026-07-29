import os
import uuid

from werkzeug.utils import secure_filename

from flask import current_app


def save_file(file, folder_name):
    """
    Save uploaded file and return relative path.
    """

    if not file:
        return None

    filename = secure_filename(file.filename)

    extension = os.path.splitext(filename)[1]

    unique_filename = f"{uuid.uuid4().hex}{extension}"

    folder_path = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        folder_name
    )

    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, unique_filename)

    file.save(file_path)

    return f"uploads/{folder_name}/{unique_filename}"