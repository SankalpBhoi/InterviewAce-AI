import os
import shutil
import uuid

UPLOAD_FOLDER = "app/storage/resumes"


def save_resume(file):
    # Create unique filename
    unique_filename = f"{uuid.uuid4()}_{file.filename}"

    # Complete path
    file_path = os.path.join(
        UPLOAD_FOLDER,
        unique_filename
    )

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return unique_filename