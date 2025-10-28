# backend/src/services/ocr_service.py

import pytesseract
from PIL import Image
from io import BytesIO
from fastapi import UploadFile


async def procesar_imagen_ocr(imagen: UploadFile) -> dict:
    """Función de servicio que realiza la extracción de texto (OCR) de una imagen."""
    
    try:
        contents = await imagen.read()
    except Exception as e:
        return {"estado": "error", "mensaje": f"Error al leer el archivo: {e}"}

    try:
        img = Image.open(BytesIO(contents))
    except Exception:
        return {"estado": "error", "mensaje": "Formato de imagen no soportado o corrupto."}
        
    try:
        texto_detectado = pytesseract.image_to_string(img, lang='spa')
    except pytesseract.TesseractError as e:
        return {"estado": "error", "mensaje": f"Fallo en la ejecución de Tesseract: {e}"}

    return {
        "estado": "completado",
        "archivo_nombre": imagen.filename,
        "texto_extraido": texto_detectado.strip()
    }