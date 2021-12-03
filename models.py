import sqlalchemy as sql
import database

class Schedule(database.Base):
    __tablename__ = "scheduled_data"
    id = sql.Column(sql.Integer, primary_key=True)
    date = sql.Column(sql.String)
    message = sql.Column(sql.String)
    reciever_email = sql.Column(sql.String, nullable=False)
    sent_from = sql.Column(sql.String,nullable=True, default="from anonymouse") 