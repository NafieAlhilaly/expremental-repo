import sqlalchemy as sql
import sqlalchemy.orm as orm
import database

class Schedule(database.Base):
    __tablename__ = "da"
    id = sql.Column(sql.Integer, primary_key=True)
    date = sql.Column(sql.String)