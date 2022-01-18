import logging
import fastapi
from fastapi import File, UploadFile
from services import file_service


router = fastapi.APIRouter()


@router.post("/api/files", name="add_file", status_code=201)
async def files_post(file: UploadFile = File(...)):
    logging.info("In files_post")
    new_blob_name = file.filename

    content = await file.read()
    await file_service.add_file(new_blob_name, content)

    return {"file": file}
