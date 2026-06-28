import logging
from concurrent.futures import ThreadPoolExecutor
from src.config import START_ID, END_ID, MAX_WORKERS
from src.scraper import check_id

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main() -> None:
    logging.info(f"Starting OSINT scraper for IDs {START_ID}-{END_ID}...")

    # Запускаем многопоточность
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(check_id, range(START_ID, END_ID + 1))

    logging.info("Scraping completed.")

if __name__ == "__main__":
    main()