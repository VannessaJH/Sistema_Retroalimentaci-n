from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from src.config.database import Base 
class Profesor:
    
    __tablename__ = 'profesores'
    
    id_profesor = Column(Integer(),primary_key = True)
    nombre = Column(String(50))
    correo_electronico = Column(String(70))
    created_at = Column(DateTime(), default = datetime.now)