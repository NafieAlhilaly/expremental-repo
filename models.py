import sqlalchemy as sql
import sqlalchemy.orm as orm
import database

class Schedule(database.Base):
    __tablename__ = "da"
    id = sql.Column(sql.Integer, primary_key=True),
    message = sql.Column(sql.String)
    date = sql.Column(sql.String)