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

async def add_schedule(date: str, msg: str, reciever_email: str, db, sent_from: str):
    schedule = models.Schedule(
        date=date, 
        message=msg,
        reciever_email=reciever_email,
        sent_from=sent_from)
    db.add(schedule)
    db.commit()
    db.refresh(schedule)