import logging
import os
from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIRECTORY = PROJECT_ROOT / "data"
DATASET_SLUG = "yasserh/loan-default-dataset"
CSV_PATH = DATA_DIRECTORY / "Loan_default.csv"

logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s [%(levelname)s] %(message)s",
)
LOGGER = logging.getLogger(__name__)


def _credentials_are_configured() -> bool:
	"""Return whether Kaggle credentials are available without exposing them."""
	username = os.getenv("KAGGLE_USERNAME")
	key = os.getenv("KAGGLE_KEY")
	if bool(username) != bool(key):
		raise RuntimeError(
			"Both KAGGLE_USERNAME and KAGGLE_KEY must be set when using environment credentials."
		)

	if username and key:
		return True

	config_directory = Path(
		os.getenv("KAGGLE_CONFIG_DIR", Path.home() / ".kaggle")
	)
	return (config_directory / "kaggle.json").is_file()


def download_dataset() -> Path:
	"""Download and extract the Kaggle dataset when the CSV is not present."""
	DATA_DIRECTORY.mkdir(parents=True, exist_ok=True)

	if CSV_PATH.is_file():
		LOGGER.info("Dataset already exists: %s", CSV_PATH)
		return CSV_PATH

	if not _credentials_are_configured():
		raise RuntimeError(
			"Kaggle credentials were not found. Set KAGGLE_USERNAME and KAGGLE_KEY "
			"or place kaggle.json in the standard .kaggle directory."
		)

	LOGGER.info("Downloading Kaggle dataset %s to %s", DATASET_SLUG, DATA_DIRECTORY)
	api = KaggleApi()
	try:
		api.authenticate()
		api.dataset_download_files(
			DATASET_SLUG,
			path=str(DATA_DIRECTORY),
			unzip=True,
		)
	except Exception as error:
		raise RuntimeError(
			f"Kaggle dataset download failed for {DATASET_SLUG}: {error}"
		) from error

	if not CSV_PATH.is_file():
		raise FileNotFoundError(
			f"Kaggle download completed, but {CSV_PATH.name} was not found in {DATA_DIRECTORY}."
		)

	LOGGER.info("Dataset downloaded successfully: %s", CSV_PATH)
	return CSV_PATH


if __name__ == "__main__":
	download_dataset()