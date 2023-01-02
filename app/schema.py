from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class Skills(BaseModel):
    name: str
    category: str


class RecordSchema(BaseModel):
    """
    RecordSchema
        A class to design the structure of schema .
    """

    id: int
    originalId: str
    talentId: Optional[str]
    talentName: Optional[str]
    talentGrade: Optional[str]
    bookingGrade: Optional[str]
    operatingUnit: str
    officeCity: Optional[str]
    officePostalCode: str
    jobManagerName: Optional[str]
    jobManagerId: Optional[str]
    totalHours: float
    startDate: datetime = None
    endDate: datetime = None
    clientName: Optional[str]
    clientId: str
    industry: Optional[str]
    isUnassigned: bool
    requiredSkills: List[Skills]
    optionalSkills: List[Skills]

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.strftime("%m/%d/%Y %I:%M %p"),
        }
