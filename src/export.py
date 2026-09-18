from pathlib import Path

import pandas as pd

from src.database import get_engine


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_CSV_PATH = PROJECT_ROOT / "data" / "loan_summary_ready.csv"


def export_summary() -> None:
	"""Export the analytical view to the Power BI-ready CSV."""
	engine = get_engine()
	try:
		df = pd.read_sql_query("SELECT * FROM vw_loan_summary", engine)
	finally:
		engine.dispose()

	OUTPUT_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
	df.to_csv(OUTPUT_CSV_PATH, index=False)
	print(f"Exported {len(df)} rows to {OUTPUT_CSV_PATH}.")


if __name__ == "__main__":
	export_summary()