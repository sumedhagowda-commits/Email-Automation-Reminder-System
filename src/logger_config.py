import logging
import os

# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

def setup_logger():

    logging.basicConfig(
        filename="logs/automation.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("Logger initialized")