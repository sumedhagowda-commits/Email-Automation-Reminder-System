import pandas as pd

def load_contacts(file_path):

    try:
        contacts = pd.read_csv(file_path)
        return contacts

    except Exception as e:
        print(f"Error loading contacts: {e}")
        return pd.DataFrame()


def load_reminders(file_path):

    try:
        reminders = pd.read_csv(file_path)
        return reminders

    except Exception as e:
        print(f"Error loading reminders: {e}")
        return pd.DataFrame()


def load_template(file_path):

    try:
        with open(file_path, "r") as file:
            return file.read()

    except Exception as e:
        print(f"Error loading template: {e}")
        return ""