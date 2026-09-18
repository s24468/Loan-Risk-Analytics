import logging

from src.extract import download_dataset
from src.export import export_summary
from src.load import load_raw_loans
from src.transform import transform_data

# Konfiguracja logowania (wygląda bardzo profesjonalnie w terminalu)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

def main():
    logging.info("=== STARTING LOAN RISK PIPELINE (POSTGRESQL) ===")
    try:
        download_dataset()
        load_raw_loans()
        transform_data()
        export_summary()
        logging.info("=== LOAN RISK PIPELINE COMPLETED SUCCESSFULLY ===")
    except Exception as e:
        logging.exception("Loan risk pipeline failed: %s", e)
        raise

if __name__ == "__main__":
    main()