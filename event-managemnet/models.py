from sqlmodel import SQLModel, Field
from datetime import datetime
from enum import Enum
from typing import Optional

class EventStatus(str, Enum):
    scheduled = "scheduled"
    ongoing = "ongoing"
    completed = "completed"
    canceled = "canceled"

class Event(SQLModel, table=True):
    event_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    start_time: datetime
    end_time: datetime
    location: str
    max_attendees: int
    status: EventStatus = Field(default=EventStatus.scheduled)

class Attendee(SQLModel, table=True):
    attendee_id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str = Field(unique=True)
    phone_number: str
    event_id: int = Field(foreign_key="event.event_id")
    check_in_status: bool = Field(default=False)


class UserIn(SQLModel):
    username: str = Field(unique=True)
    password: str

class User(UserIn, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    