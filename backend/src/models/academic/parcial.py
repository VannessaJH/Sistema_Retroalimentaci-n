from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


Base = declarative_base()


class Parcial (Base):
    __tablename__ = 'parciales'
    id_parcial = Column(Integer(), primary_key = True)
    id_asignatura = Column(Integer(), ForeignKey('asignaturas.ID_Asignatura'))
    corte = Column(Integer())
    fecha = Column(DateTime)
    created_at = Column(DateTime(), default = datetime.now())
    
asignatura = relationship("Asignatura", back_populates="parciales")
preguntas = relationship("Pregunta", back_populates="parcial")
    
    