from sqlmodel import SQLModel, create_engine, Session

database_url = "sqlite:///./event_management.db"
engine = create_engine(database_url, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

SQLModel.metadata.create_all(engine)