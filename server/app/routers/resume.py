from fastapi import APIRouter, UploadFile, File, HTTPException

from app.schemas.resume_schema import ResumeResponse
from app.services.resume_service import save_resume

router = APIRouter(
    prefix="/api/resume",
    tags=["Resume"]
)


@router.post(
    "/upload",
    response_model=ResumeResponse
)
def upload_resume(
    file: UploadFile = File(...)
):
    # Validate PDF
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    filename = save_resume(file)

    return ResumeResponse(
        filename=filename,
        message="Resume uploaded successfully"
    )