import logging
from pathlib import Path

from sqlalchemy import text

from src.database import get_engine


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SQL_SCRIPT_PATH = PROJECT_ROOT / "sql" / "create_views.sql"

def transform_data():
    logging.info("Rozpoczynam transformację danych w bazie...")
    
    if not SQL_SCRIPT_PATH.is_file():
        raise FileNotFoundError(f"Nie znaleziono pliku {SQL_SCRIPT_PATH}!")
        
    with SQL_SCRIPT_PATH.open("r", encoding="utf-8") as f:
        sql_code = f.read()
        
    engine = get_engine()
    try:
        with engine.begin() as connection:
            connection.execute(text(sql_code))
    finally:
        engine.dispose()
    
    logging.info("Transformacja zakończona sukcesem. Widoki SQL zostały zaktualizowane.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    transform_data()