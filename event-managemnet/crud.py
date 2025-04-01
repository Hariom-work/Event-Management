from sqlmodel import Session, select
from models import Event, Attendee
from schema import EventCreate, AttendeeCreate,EventListResponse
from fastapi import HTTPException

def create_event(session: Session, event: EventCreate):
    db_event = Event(**event.dict())
    session.add(db_event)
    session.commit()
    session.refresh(db_event)
    return db_event


def update_event(session: Session, event_id: int, event_update: EventCreate):
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    for key, value in event_update.dict(exclude_unset=True).items():
        setattr(event, key, value)
    session.commit()
    session.refresh(event)
    return event


def list_events(session: Session):
    events = session.exec(select(Event)).all()
    return EventListResponse(events=events)

def register_attendee(session: Session, attendee: AttendeeCreate):
    event = session.get(Event, attendee.event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    attendee_count = session.exec(select(Attendee).where(Attendee.event_id == attendee.event_id)).count()
    if attendee_count >= event.max_attendees:
        raise HTTPException(status_code=400, detail="Event registration full")
    db_attendee = Attendee(**attendee.dict())
    session.add(db_attendee)
    session.commit()
    session.refresh(db_attendee)
    return db_attendee

def list_attendees(session: Session, event_id: int):
    return session.exec(select(Attendee).where(Attendee.event_id == event_id)).all()

def check_in_attendee(session: Session, event_id: int):
    return session.exec(select(Attendee).where(Attendee.event_id == event_id,Attendee.check_in_status==True)).all()
