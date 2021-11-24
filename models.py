import sqlalchemy as sql
import sqlalchemy.orm as orm
import database

class Schedule(database.Base):
    __tablename__ = "scheduled_data"
    id = sql.Column(sql.Integer, primary_key=True)
    date = sql.Column(sql.String)
    message = sql.Column(sql.String)