import pandas as pd
import logging
import os

from datetime import datetime

from src.email_sender import send_email


def process_reminders(contacts_df, reminders_df, template):

    print("\nProcessing reminders...\n")

    report_data = []

    for _, reminder in reminders_df.iterrows():

        try:

            # Match contact
            contact = contacts_df[
                contacts_df["id"] == reminder["contact_id"]
            ]

            if contact.empty:

                logging.warning(
                    f"No contact found for ID {reminder['contact_id']}"
                )

                continue

            contact = contact.iloc[0]

            # Personalize email
            personalized_message = template.format(
                name=contact["name"],
                reminder_title=reminder["reminder_title"],
                due_date=reminder["due_date"]
            )

            # Send email
            status = send_email(
                contact["email"],
                reminder["subject"],
                personalized_message
            )

            # Save report entry
            report_data.append({
                "name": contact["name"],
                "email": contact["email"],
                "subject": reminder["subject"],
                "status": status,
                "timestamp": datetime.now()
            })

        except Exception as e:

            logging.error(f"Reminder processing error: {e}")

    # Create outputs folder
    os.makedirs("outputs", exist_ok=True)

    # Save report
    report_df = pd.DataFrame(report_data)

    report_df.to_csv(
        "outputs/email_report.csv",
        index=False
    )

    print("Report generated successfully.")

    logging.info("Report generated successfully.")