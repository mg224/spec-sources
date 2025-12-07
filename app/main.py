from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal
from crud import get_all_sources, add_source, delete_source
from schemas import SpecSourceBase, SpecSourceObj
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conf = ConnectionConfig(
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD"),
    MAIL_FROM=os.environ.get("MAIL_FROM"),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()

def welcome_email_template(name: str) -> str:
    return f"""
    <html>
        <body style="font-family: Arial, sans-serif;">
            <h3>Welcome, {name}!</h3>
            <p>We're so happy to have you! Stay tuned for updates from Spec Sources!</p>
        </body>
    </html>
    """

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the FastAPI app!"
    }

@app.get("/health/db/users")
def health_db_users(db: Session = Depends(get_db)):
   count = db.execute(text("SELECT COUNT(*) FROM SpectatorSources")).scalar_one()
   return {
       "count": int(count)
    }

@app.get("/sources")
def get_db_sources(db: Session = Depends(get_db)):
    sources = get_all_sources(db)
    return sources

@app.post("/sources")
async def add_db_source(source: SpecSourceBase, db: Session = Depends(get_db)):
    db_source = add_source(db, source)
    message = MessageSchema(
        subject="Welcome to Spec Sources!",
        recipients=[source.email],
        body=welcome_email_template(source.name),
        subtype=MessageType.html,
    )

    fm = FastMail(conf)
    try:
        await fm.send_message(message)
    except:
        print("Failed to send email.")

    return db_source

# @app.put("/sources/{source_id}")
# def delete_db_source(source_id: int, db: Session = Depends(get_db)):
#     deleted = delete_source(db, source_id)
#     if not deleted:
#         raise HTTPException(status_code=404, detail=f"No source with source id {source_id}")
    
#     return f"Successfully deleted source with id {source_id}"

@app.delete("/sources/{source_id}")
def delete_db_source(source_id: int, db: Session = Depends(get_db)):
    deleted = delete_source(db, source_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"No source with source id {source_id}")
    
    return f"Successfully deleted source with id {source_id}"
