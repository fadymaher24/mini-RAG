from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
import os
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
from fastapi.responses import JSONResponse

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)


@data_router.get("/upload/{project_id}")
async def upload_data(
    project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings)
):

    # validate file properties
    is_valid = DataController().validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": is_valid[1]},
        )
