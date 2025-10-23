import sys
import os
from sqlalchemy import text

# Importar desde src
from src.config.database import engine, Base

print(" Script iniciado...")

def test_mysql_connection():
    """Prueba conexión directa a MySQL"""
    try:
        # Usar el engine de SQLAlchemy para probar conexión
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("Conexión a MySQL: EXITOSA")
        return True
    except Exception as e:
        print(f" Error conexión MySQL: {e}")
        return False

def test_tables_exist():
    """Prueba que las tablas existen en MySQL"""
    try:
        with engine.connect() as conn:
            # Ver tablas existentes
            result = conn.execute(text("SHOW TABLES"))
            tables = [row[0] for row in result]
            print(f"Tablas en BD: {tables}")
            
            # Verificar que existe la tabla 'parciales'
            if 'parciales' in tables:
                print(" Tabla 'parciales' encontrada")
                
                # Mostrar estructura de la tabla
                result = conn.execute(text("DESCRIBE parciales"))
                print(" Estructura de 'parciales':")
                for row in result:
                    print(f"   - {row[0]} ({row[1]})")
            else:
                print(" Tabla 'parciales' NO encontrada")
                
    except Exception as e:
        print(f" Error leyendo tablas: {e}")
        return False
    return True

if __name__ == "__main__":
    print("Iniciando pruebas de conexión...")
    
    if test_mysql_connection() and test_tables_exist():
        print(" ¡Todas las pruebas pasaron!")
    else:
        print(" Algunas pruebas fallaron")