import pandas as pd
from sqlalchemy import create_engine, text

def load_raw_loans():
    # Twój connection string do PostgreSQL (port 5433)
    engine = create_engine('postgresql+psycopg2://postgres:secret@localhost:5433/loan_risk_db')
    
    df = pd.read_csv('data/Loan_default.csv')
    print(f"Wczytano {len(df)} wierszy z pliku CSV.")
    
    # KROK NAPRAWCZY DLA POSTGRESQL: Usuwamy widok zależny przed podmianą tabeli
    with engine.begin() as conn:
        conn.execute(text("DROP VIEW IF EXISTS vw_loan_summary CASCADE;"))
    
    # Teraz Pandas może bezpiecznie podmienić tabelę raw_loans
    df.to_sql('raw_loans', engine, if_exists='replace', index=False)
    print("Tabela 'raw_loans' została pomyślnie zaktualizowana w PostgreSQL.")

if __name__ == "__main__":
    load_raw_loans()