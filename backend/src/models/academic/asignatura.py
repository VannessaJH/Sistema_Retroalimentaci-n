from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from src.config.database import Base 

class Asignatura(Base):
    
    __tablename__ = 'asignaturas'
    
    id_asignatura = Column (Integer(), primary_key = True )
    id_profesor = Column (Integer(), ForeignKey ('profesores.ID_Profesor'), nullable = False)
    semestre = Column(Integer(), nullable = False)
    nombre = Column(String(100))
    created_at = Column(DateTime(), default = datetime.now)
    
    profesor = relationship("Profesor", back_populates="asignaturas")
    