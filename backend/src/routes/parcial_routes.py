from fastapi import APIRouter, UploadFile, File
from services.ocr_service import procesar_imagen_ocr
router = APIRouter(prefix="/api/parciales", tags=["Parciales"])

@router.post("/procesar-ocr")
async def procesar_examen_ocr(imagen: UploadFile = File(...)):
    resultado = await procesar_imagen_ocr(imagen)
    
    return {
        "mensaje": f"Procesamiento OCR finalizado para {imagen.filename}",
        "data": resultado # El diccionario devuelto por el servicio (con el texto extraído)
    }

@router.post("/")
async def crear_parcial():
    return {"mensaje": "Endpoint para crear parcial en BD - EN CONSTRUCCIÓN"}

@router.post("/{id_parcial}/preguntas")
async def agregar_preguntas(id_parcial: int):
    return {
        "mensaje": f"Endpoint para agregar preguntas al parcial {id_parcial} - EN CONSTRUCCIÓN",
        "id_parcial": id_parcial
    }

@router.get("/{id_parcial}")
async def obtener_parcial(id_parcial: int):
    return {
        "mensaje": f"Endpoint para obtener parcial {id_parcial} - EN CONSTRUCCIÓN", 
        "id_parcial": id_parcial
    }