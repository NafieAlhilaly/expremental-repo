from typing import Optional
import fastapi
import sqlalchemy.orm as orm
import services
import models
import time
import datetime
import database
from fastapi_utils.tasks import repeat_every
from send_email import send_email

app = fastapi.FastAPI()

def check_date():
    """
    check database periodically and run task if today date == task date
    """
    db = database.SessionLocal()
    today_date = datetime.datetime.now().strftime("%m/%d/%Y")
    data = db.query(
        models.Schedule.id,
        models.Schedule.date,
        models.Schedule.message,
        models.Schedule.reciever_email,
        models.Schedule.sent_from 
        ).filter(models.Schedule.date == today_date).all()
    print(today_date)
    if data:
        for schedule_time in data:
            """
            send scheduled messages
            """
            

@app.on_event("startup")
@repeat_every(seconds=10)  # 86400 seconds = 1 day
def check_date_task() -> None:
    check_date()

@app.post("/add_schedule")
async def add_schedule(
    msg: str = fastapi.Form(...),
    date: str = fastapi.Form(...),
    reciever_email: str = fastapi.Form(...),
    sent_from: str = fastapi.Form("anonymose"),
    db: orm.Session = fastapi.Depends(services.get_db)):

    await services.add_schedule(
        msg=msg,
        date=date, 
        reciever_email=reciever_email, 
        sent_from=sent_from, 
        db=db)
    return {"message":"added"}