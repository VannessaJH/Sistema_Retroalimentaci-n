from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from src.config.database import Base 


class Parcial(Base):
    
    __tablename__ = 'parciales'
    
    id_parcial = Column (Integer(), primary_key = True )
    id_asignatura = Column (Integer(), ForeignKey ('asignaturas.ID_Asignatura'), nullable = False)
    corte = Column(Integer(), nullable = False)
    fecha = Column(DateTime(), default = datetime.now())
    created_at = Column(DateTime(), default = datetime.now)
    
    asignatura = relationship("Asignatura", back_populates="parciales")
    preguntas = relationship("Pregunta", back_populates="parcial")
    
    
  
        