
from fastapi import APIRouter, UploadFile, File, Depends
from services.ocr_service import procesar_imagen_ocr
from config.database import get_db
from sqlalchemy.orm import Session
from controllers.academic.parcial_controller import ParcialController
from controllers.evaluation.pregunta_controller import PreguntaController
router = APIRouter(prefix="/api/parciales", tags=["Parciales"])

@router.post("/procesar-ocr")
async def procesar_examen_ocr(imagen: UploadFile = File(...)):
    resultado = await procesar_imagen_ocr(imagen)
    
    return {
        "mensaje": f"Procesamiento OCR finalizado para {imagen.filename}",
        "data": resultado 
    }

@router.post("/")
async def crear_parcial(
    datos_parcial: dict,  
    db: Session = Depends(get_db)  
):
    try:
        resultado = ParcialController.crear_parcial(db, datos_parcial)
        return resultado
    except Exception as e:
        return {"error": f"Error en el servidor: {str(e)}"}

@router.post("/{id_parcial}/preguntas")
async def agregar_preguntas(
    id_parcial: int,
    datos_pregunta: dict,
    db: Session = Depends(get_db)
                            
    ):
    
    datos_pregunta["id_parcial"] = id_parcial
    resultado = PreguntaController.agregar_pregunta(db, datos_pregunta)
    
    return resultado
        
@router.get("/{id_parcial}")
async def obtener_parcial(id_parcial: int):
    return {
        "mensaje": f"Endpoint para obtener parcial {id_parcial} - EN CONSTRUCCIÓN", 
        "id_parcial": id_parcial
    }