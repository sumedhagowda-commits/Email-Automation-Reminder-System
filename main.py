import schedule
import time

from src.logger_config import setup_logger
from src.utils import (
    load_contacts,
    load_reminders,
    load_template
)

from src.scheduler_service import process_reminders


# Initialize logger
setup_logger()

# Load data
contacts_df = load_contacts("data/contacts.csv")

reminders_df = load_reminders("data/reminders.csv")

template = load_template(
    "templates/reminder_template.txt"
)

print("\nEmail Automation System Started...\n")

# Schedule automation
schedule.every(1).minutes.do(
    process_reminders,
    contacts_df=contacts_df,
    reminders_df=reminders_df,
    template=template
)

# Run immediately once
process_reminders(
    contacts_df,
    reminders_df,
    template
)

# Keep scheduler running
while True:

    schedule.run_pending()

    time.sleep(1)