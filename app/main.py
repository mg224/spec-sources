from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal

app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],                 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

@app.get("/health/db/users")
def health_db_users(db: Session = Depends(get_db)):
   count = db.execute(text("SELECT COUNT(*) FROM specsources")).scalar_one()
   return {"count": int(count)}
