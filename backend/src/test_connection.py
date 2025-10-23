from config.database import engine, Base
from models.academic.parcial import Parcial
import mysql.connector

def test_mysql_connection():
    """Prueba conexión directa a MySQL"""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='sistema_retroalimentacion'
        )
        print("Conexión directa a MySQL: EXITOSA")
        conn.close()
    except Exception as e:
        print(f"Error conexión MySQL: {e}")
        return False
    return True

def test_sqlalchemy_tables():
    """Prueba que SQLAlchemy puede ver las tablas"""
    try:
        # Intenta crear las tablas (solo si no existen)
        Base.metadata.create_all(bind=engine)
        print("SQLAlchemy conectado correctamente")
        
        # Ver tablas existentes
        with engine.connect() as conn:
            result = conn.execute("SHOW TABLES")
            tables = [row[0] for row in result]
            print(f"Tablas en BD: {tables}")
            
    except Exception as e:
        print(f"Error SQLAlchemy: {e}")
        return False
    return True

if __name__ == "__main__":
    print("Iniciando pruebas de conexión...")
    
    if test_mysql_connection() and test_sqlalchemy_tables():
        print("¡Todas las pruebas pasaron!")
    else:
        print("Algunas pruebas fallaron")