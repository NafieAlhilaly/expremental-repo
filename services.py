import database as db
import models

def get_db():
    database = db.SessionLocal()
    try:
        yield database
    finally:
        database.close()

def create_database():
    db.Base.metadata.create_all(bind=db.engine)

async def add_schedule(date: str, db):
    schedule = models.Schedule(date=date)
    db.add(schedule)
    db.commit()
    db.refresh(schedule)