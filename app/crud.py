from sqlalchemy.orm import Session
from models import SpecSource
from schemas import SpecSourceBase, SpecSourceObj

def get_all_sources(db: Session):
    return db.query(SpecSource).all()

def get_source_by_id(db: Session, source_id: int):
    return db.query(SpecSource).filter(SpecSource.id == source_id).first()

def add_source(db: Session, source: SpecSourceBase):
    db_source = SpecSource(name=source.name, email=source.email)
    db.add(db_source)
    db.commit()
    db.refresh(db_source)
    return db_source
    
def delete_source(db: Session, source_id: int):
    db_source = get_source_by_id(db, source_id)
    if db_source:
        db.delete(db_source)
        db.commit()
        return True
    
    return False