from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal
from crud import get_all_sources, add_source, delete_source
from schemas import SpecSourceBase, SpecSourceObj

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
    return {
        "message": "Welcome to the FastAPI app!"
    }

@app.get("/health/db/users")
def health_db_users(db: Session = Depends(get_db)):
   count = db.execute(text("SELECT COUNT(*) FROM specsources")).scalar_one()
   return {
       "count": int(count)
    }

@app.get("/sources")
def get_db_sources(db: Session = Depends(get_db)):
    sources = get_all_sources(db)
    return sources

@app.post("/sources")
def add_db_source(source: SpecSourceBase, db: Session = Depends(get_db)):
    db_source = add_source(db, source)
    return db_source

@app.delete("/sources/{source_id}")
def delete_db_source(source_id: int, db: Session = Depends(get_db)):
    deleted = delete_source(db, source_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"No source with source id {source_id}")
    
    return f"Successfully deleted source with id {source_id}"
