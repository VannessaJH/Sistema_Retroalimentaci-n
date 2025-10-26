from sqlalchemy.orm import Session
from models.academic.parcial import Parcial
from models.academic.asignatura import Asignatura

class ParcialController:
    
    @staticmethod
    def crear_parcial(db: Session, datos_parcial: dict):
        try:
        
            asignatura = db.query(Asignatura).filter(
                Asignatura.id_asignatura == datos_parcial["id_asignatura"]
            ).first()
            
            if not asignatura:
                raise ValueError("La asignatura no existe")
            
          
            nuevo_parcial = Parcial(
                id_asignatura=datos_parcial["id_asignatura"],
                corte=datos_parcial["corte"],
                fecha=datos_parcial["fecha"]
            )
            
          
            db.add(nuevo_parcial)
            db.commit()
            db.refresh(nuevo_parcial)
            
            
            return {
                "id_parcial": nuevo_parcial.id_parcial,
                "mensaje": "Parcial creado exitosamente",
                "asignatura": asignatura.nombre
            }
            
        except Exception as e:
            db.rollback()  
            raise e