import os
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import load_dotenv

load_dotenv()
    
conf = ConnectionConfig(
    MAIL_USERNAME = os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD'),
    MAIL_FROM = os.getenv('MAIL_FROM'),
    MAIL_PORT = int(os.getenv('MAIL_PORT')),
    MAIL_SERVER = os.getenv('MAIL_SERVER'),
    MAIL_FROM_NAME = os.getenv('MAIN_FROM_NAME'),
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER='templates'
)

async def send_email(subject: str, email_to: str, body: dict):
    html = """
    <p>Thanks for using Fastapi-mail</p> 
    """

    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=html,
        subtype='html',
    )

    fm = FastMail(conf)
    print("sending...")
    #await fm.send_message(message, template_name='email.html')