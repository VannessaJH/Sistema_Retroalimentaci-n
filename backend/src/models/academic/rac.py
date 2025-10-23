from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from src.config.database import Base 

class Rac:
    
    __tablename__ = 'racs'
    id_rac = Column(Integer(), primary_key = True)
    id_asignatura = Column (Integer(), ForeignKey ('asignaturas.ID_Asignatura'),  nullable = False)
    descripcion = Column (Text)
    created_at = Column(DateTime(), default = datetime.now)
    
    asignatura = relationship("Asignatura", back_populates="racs")