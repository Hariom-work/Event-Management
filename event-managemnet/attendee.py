from fastapi import APIRouter, Depends
from sqlmodel import Session
from crud import register_attendee, check_in_attendee, list_attendees
from schema import AttendeeCreate
from db import get_session
from auth import get_current_user

app = APIRouter()

@app.post("/events/{event_id}/attendees")
def register_attendee_api(event_id: int, attendee: AttendeeCreate, session: Session = Depends(get_session), user: dict = Depends(get_current_user)):
    return register_attendee(session, attendee)

@app.put("/attendees/{attendee_id}/check-in")
def check_in_attendee_api(attendee_id: int, session: Session = Depends(get_session), user: dict = Depends(get_current_user)):
    return check_in_attendee(session, attendee_id)

@app.get("/events/{event_id}/attendees")
def list_attendees_api(event_id: int, session: Session = Depends(get_session), user: dict = Depends(get_current_user)):
    return list_attendees(session, event_id)