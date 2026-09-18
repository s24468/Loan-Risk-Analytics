import os

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, URL


def get_database_url() -> str | URL:
    """Return the configured PostgreSQL URL, with local development defaults."""
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        return database_url

    return URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "secret"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=int(os.getenv("POSTGRES_PORT", "5433")),
        database=os.getenv("POSTGRES_DB", "loan_risk_db"),
    )


def get_engine() -> Engine:
    """Create a PostgreSQL engine with a lightweight health check."""
    return create_engine(get_database_url(), pool_pre_ping=True)