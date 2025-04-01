from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from models import EventStatus

class EventCreate(BaseModel):
    name: str
    description: str
    start_time: datetime
    end_time: datetime
    location: str
    max_attendees: int
    status: Optional[EventStatus] = EventStatus.scheduled

class AttendeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    event_id: int

class EventListResponse(BaseModel):
    events: List[EventCreate]


class CheckInUpdate(BaseModel):
    check_in_status: bool