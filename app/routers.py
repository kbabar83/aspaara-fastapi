from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional
from fastapi import UploadFile, Depends
from fastapi import APIRouter
from fastapi_pagination import Page, paginate

from config.database import get_db

from app.import_planning_record import process_record
from app.models import Record
from app.schema import RecordSchema


router = APIRouter(tags=["Record"])


@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    """
    An async method to upload file.
    TODO : Enhance file type and extention.
    """
    if file.content_type == "application/json":
        if file:
            try:
                process_record(file)
                return {"message": f"file {file.filename} processed"}
            except Exception as exc:
                return {"message": "file processing failed"}
    else:
        return {"message": "Invalid Format of File", "status_code": 422}


@router.get("/get_list_record/", response_model=Page[RecordSchema])
async def get_list_record(
    sort_by: Optional[str] = None,
    keyword: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """
        An asyn function to get list of Paginated records as per the sorting and filter applied.\
        Filters available for fields given :
            talentId, talentName, jobManagerId, jobManagerName, clientId, clientName.

    """
    model_query = db.query(Record)
    if keyword:
        model_query = model_query.filter(
            or_(
                Record.talentId.like(keyword),
                Record.talentName.like(keyword),
                Record.jobManagerId.like(keyword),
                Record.jobManagerName.like(keyword),
                Record.clientId.like(keyword),
                Record.clientName.like(keyword),
            )
        )
    if sort_by:
            model_query = model_query.order_by(sort_by)

    return paginate(model_query.all())
