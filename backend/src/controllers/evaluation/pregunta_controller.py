from sqlalchemy.orm import Session
from models.evaluation.pregunta import Pregunta
from models.academic.tema import Tema
from models.academic.rac import Rac
from models.academic.parcial import Parcial
import json

class PreguntaController:
    
    @staticmethod
    def agregar_pregunta(db: Session, datos_pregunta: dict):
        
        try: 
            tema = db.query(Tema).filter(Tema.id_tema == datos_pregunta["id_tema"]).first()
            rac = db.query(Rac).filter(Rac.id_rac == datos_pregunta["id_rac"]).first()  
            parcial = db.query(Parcial).filter(Parcial.id_parcial == datos_pregunta["id_parcial"]).first()

            if not tema:
                    return {"error": "El tema no existe"}
            if not rac:
                    return {"error": "El RAC no existe"}
            if not parcial:
                    return {"error": "El parcial no existe"}
            
            nueva_pregunta = Pregunta(
                    id_tema=datos_pregunta["id_tema"],
                    id_rac=datos_pregunta["id_rac"],
                    id_parcial=datos_pregunta["id_parcial"],
                    enunciado=datos_pregunta["enunciado"],
                    opciones=datos_pregunta["opciones"],  # ← Esto es el JSON
                    respuesta_correcta=datos_pregunta["respuesta_correcta"],
                    valor_base=datos_pregunta["valor_base"]
                )
            
            db.add(nueva_pregunta)
            db.commit()
            db.refresh(nueva_pregunta)
            return {
                "mensaje": "Pregunta agregada exitosamente",
                "id_pregunta": nueva_pregunta.id_pregunta
            }
        
            
        except Exception as e:
            db.rollback()
            return {"error": f"Error al crear pregunta: {str(e)}"}
            