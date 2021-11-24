import fastapi
import sqlalchemy.orm as orm
import services
import models
import time
import datetime
import database
from fastapi_utils.tasks import repeat_every

app = fastapi.FastAPI()

def check_date():
    """
    check database everyday and run task if today date == task date
    """
    db = database.SessionLocal()
    now = datetime.datetime.now().strftime("%m/%d/%Y")
    data = db.query(models.Schedule.date).all()
    for schedule_time in data:
        # from string to datetime obj
        date = datetime.datetime.strptime(date, "%m/%d/%Y")

        if time.mktime(now.timetuple()) == time.mktime(date.timetuple()):
            """
            run task if task date is today
            """
        

@app.on_event("startup")
@repeat_every(seconds= 86400)  # 86400 = 1 day
def check_date_task() -> None:
    check_date()

@app.post("/add_schedule")
async def add_schedule(
    message: str = fastapi.Form(...),
    date: str = fastapi.Form(...),
    db: orm.Session = fastapi.Depends(services.get_db)):

    await services.add_schedule(date,message, db=db)
    return {"message":"added"}