from sqlalchemy import Boolean, Column, Integer, String, JSON, Float, DateTime

from config.database import Base


class Record(Base):
    """
    Record
        A class to create table in database to store planning information .
    """

    __tablename__ = "records"

    id = Column(Integer, index=True, unique=True, primary_key=True)
    originalId = Column(String, index=True, unique=True)
    talentId = Column(String, index=True)
    talentName = Column(String, index=True)
    talentGrade = Column(String, index=True)
    bookingGrade = Column(String, index=True)
    operatingUnit = Column(String, index=True)
    officeCity = Column(String, index=True)
    officePostalCode = Column(String, index=True)
    jobManagerName = Column(String, index=True)
    jobManagerId = Column(String, index=True)
    totalHours = Column(Float, index=True)
    startDate = Column(DateTime(timezone=True))
    endDate = Column(DateTime(timezone=True))
    clientName = Column(String, index=True)
    clientId = Column(String, index=True)
    industry = Column(String, index=True)
    isUnassigned = Column(Boolean, default=False)
    requiredSkills = Column(JSON)
    optionalSkills = Column(JSON)
