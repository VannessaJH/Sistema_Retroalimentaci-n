from fastapi import FastAPI
from routes.parcial_routes import router as parciales_router
import uvicorn

print("INICIANDO SCRIPT MAIN.PY")

app = FastAPI(title="Sistema de Retroalimentación")
app.include_router(parciales_router)

@app.get("/")
def root():
    return {"message": " Servidor funcionando"}

print(" ANTES de uvicorn.run")

if __name__ == "__main__":
    print(" EJECUTANDO uvicorn.run()")
    uvicorn.run(
        "main:app", 
        host="127.0.0.1", 
        port=8000, 
        reload=True,
        log_level="info"
    )
    print(" Esta línea no debería verse")