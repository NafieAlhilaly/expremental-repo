import fastapi
import sqlalchemy.orm as orm
import services

app = fastapi.FastAPI()

@app.post("/add_schedule")
async def add_schedule(
    message: str = fastapi.Form(...),
    date: str = fastapi.Form(...),
    db: orm.Session = fastapi.Depends(services.get_db)):

    await services.add_schedule(date, db)
    return {"message":"added"}