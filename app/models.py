from sqlalchemy import Column, Integer, String
from database import Base

"""
CREATE TABLE SpectatorSources (
   id INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(100) NOT NULL,
   email VARCHAR(100) NOT NULL UNIQUE
);
"""

class SpecSource(Base):
    __tablename__ = "SpectatorSources"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)    
    email = Column(String(100), unique=True, nullable=False)
