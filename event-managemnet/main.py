from fastapi import FastAPI
from routes import event, attendee, user

app = FastAPI()
app.include_router(user.app)
app.include_router(event.app)
app.include_router(attendee.app)