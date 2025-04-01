from fastapi import APIRouter, Depends
from sqlmodel import Session
from crud import create_event, update_event, list_events
from schema import EventCreate
from db import get_session
from auth import get_current_user

app = APIRouter()

@app.post("/events")
def create_event_api(event: EventCreate, session: Session = Depends(get_session), user: dict = Depends(get_current_user)):
    return create_event(session, event)

@app.put("/events/{event_id}")
def update_event_api(event_id: int, event: EventCreate, session: Session = Depends(get_session), user: dict = Depends(get_current_user)):
    return update_event(session, event_id, event)

@app.get("/events")
def list_events_api(session: Session = Depends(get_session), user: dict = Depends(get_current_user)):
    return list_events(session)