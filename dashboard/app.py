import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Email Automation Dashboard",
    page_icon="📧",
    layout="wide"
)

# Title
st.title("📧 Email Automation & Reminder System")

st.markdown("""
This dashboard simulates an industry-style email automation system.
""")

# Sidebar
st.sidebar.header("System Controls")

dry_run = st.sidebar.checkbox(
    "Enable Dry Run Mode",
    value=True
)

# Load CSV files
contacts_path = "data/contacts.csv"
reminders_path = "data/reminders.csv"
report_path = "outputs/email_report.csv"

# Contacts Section
st.header("👥 Contact List")

if os.path.exists(contacts_path):

    contacts_df = pd.read_csv(contacts_path)

    st.dataframe(
        contacts_df,
        use_container_width=True
    )

    st.success(f"{len(contacts_df)} contacts loaded.")

else:
    st.error("contacts.csv not found.")

# Reminders Section
st.header("⏰ Reminder Schedule")

if os.path.exists(reminders_path):

    reminders_df = pd.read_csv(reminders_path)

    st.dataframe(
        reminders_df,
        use_container_width=True
    )

    st.info(f"{len(reminders_df)} reminders scheduled.")

else:
    st.error("reminders.csv not found.")

# Statistics Section
st.header("📊 Dashboard Statistics")

col1, col2, col3 = st.columns(3)

if os.path.exists(contacts_path):
    total_contacts = len(pd.read_csv(contacts_path))
else:
    total_contacts = 0

if os.path.exists(reminders_path):
    total_reminders = len(pd.read_csv(reminders_path))
else:
    total_reminders = 0

if os.path.exists(report_path):
    report_df = pd.read_csv(report_path)
    total_processed = len(report_df)
else:
    total_processed = 0

col1.metric("Total Contacts", total_contacts)
col2.metric("Scheduled Reminders", total_reminders)
col3.metric("Processed Emails", total_processed)

# Simulate Automation
st.header("🚀 Automation Execution")

if st.button("Run Email Automation"):

    st.warning("Processing reminders...")

    progress_bar = st.progress(0)

    for percent in range(100):

        progress_bar.progress(percent + 1)

    st.success("Automation Completed Successfully!")

    st.write("Execution Time:", datetime.now())

    if dry_run:
        st.info("Dry Run Mode Enabled — No real emails sent.")
    else:
        st.error("Real Email Mode Enabled.")

# Reports Section
st.header("📁 Generated Reports")

if os.path.exists(report_path):

    report_df = pd.read_csv(report_path)

    st.dataframe(
        report_df,
        use_container_width=True
    )

    csv = report_df.to_csv(index=False)

    st.download_button(
        label="Download Report CSV",
        data=csv,
        file_name="email_report.csv",
        mime="text/csv"
    )

else:
    st.warning("No report generated yet.")

# Logs Section
st.header("📝 System Logs")

log_path = "logs/automation.log"

if os.path.exists(log_path):

    with open(log_path, "r") as file:

        logs = file.read()

    st.text_area(
        "Automation Logs",
        logs,
        height=300
    )

else:
    st.warning("No logs found.")

# Footer
st.markdown("---")

st.caption(
    "Built using Python, Streamlit, Pandas, SMTP, and Scheduling"
)