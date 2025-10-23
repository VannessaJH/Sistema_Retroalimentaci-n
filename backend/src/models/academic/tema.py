from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from src.config.database import Base 

class Tema(Base):
    
    __tablename__ = 'temas'
    
    id_tema = Column(Integer(), primary_key = True)
    id_asignatura = Column (Integer(), ForeignKey ('asignaturas.ID_Asignatura'),  nullable = False)
    nombre = (String(100))
    descripción = (Text)
    created_at = Column(DateTime(), default = datetime.now)
    
    asignatura = relationship("Asignatura", back_populates="temas")