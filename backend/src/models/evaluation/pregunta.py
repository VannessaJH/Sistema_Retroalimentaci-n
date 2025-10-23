from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Float, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from src.config.database import Base 

class Pregunta(Base):
    
    __tablename__ = 'preguntas'
    
    id_pregunta = Column(Integer(), primary_key = True)
    id_tema = Column(Integer(), ForeignKey('temas.id_tema'), nullable = False)
    id_rac = Column(Integer(), ForeignKey('racs.id_rac'), nullable = False)
    id_parcial = Column(Integer(), ForeignKey('parciales.id_parcial'), nullable = False)
    enunciado = Column(Text)
    valor_base = Column(Float)
    opciones = Column(JSON)
    respuesta_correcta = Column(String(1))
    created_at = Column(DateTime(), default = datetime.now)
    
    tema = relationship("Tema", back_populates="preguntas")
    rac = relationship("Rac", back_populates = "preguntas")
    parcial = relationship("Parcial", back_populates= "preguntas")
    