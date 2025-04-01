
# Event Management API

## Overview
This is a FastAPI-based Event Management API that allows users to create, manage, and track events and attendees. It includes features such as event scheduling, registration, attendee check-ins, and authentication using JWT tokens.

## Features
- **User Authentication** (Signup/Login with JWT tokens)
- **Create Event** (Initialize event with `scheduled` status)
- **Update Event** (Modify event details and status)
- **Register Attendee** (Check max_attendees before allowing registration)
- **Attendee Check-in** (Mark attendee as checked in)
- **List Events** (Filter events by status, location, date)
- **List Attendees** (Retrieve attendees for a specific event with optional filters)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/event-management-api.git
   cd event-management-api
   ```

2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the API
1. Start the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```

2. Open the API documentation in your browser:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Authentication
- Obtain a JWT token by logging in:
  ```sh
  curl -X 'POST' 'http://127.0.0.1:8000/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=your_username&password=your_password'
  ```

- Use the token to authorize API requests in Swagger UI or pass it as `Authorization: Bearer <token>` in headers.

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/signup` | Create a new user |
| POST | `/token` | Authenticate and get JWT token |
| POST | `/events/` | Create a new event |
| PUT | `/events/{event_id}` | Update an event |
| GET | `/events/` | List all events (with filters) |
| POST | `/attendees/` | Register an attendee |
| PUT | `/attendees/{attendee_id}/check-in` | Check-in an attendee |
| GET | `/attendees/{event_id}` | List attendees for an event |

## License
This project is open-source and available under the [MIT License](LICENSE).