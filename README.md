# 📧 Email Automation & Reminder System

A Python-based automation project that automatically sends reminder emails using SMTP, CSV datasets, scheduling, logging, and a Streamlit dashboard.

This project simulates a real-world business productivity and communication automation system used by HR teams, trainers, operations teams, admins, and customer support teams.

---

# 🚀 Project Overview

Manual reminder emails consume time and can lead to:
- missed follow-ups,
- delayed communication,
- repetitive work,
- operational inefficiency.

This project automates the entire workflow using Python.

The system:
- reads contacts from CSV files,
- loads reminder schedules,
- personalizes email templates,
- automates email sending,
- tracks success/failure logs,
- generates CSV reports,
- provides a Streamlit dashboard for monitoring.

---

# 🎯 Problem Statement

Organizations frequently send repetitive emails such as:
- meeting reminders,
- webinar notifications,
- interview schedules,
- payment reminders,
- follow-up emails,
- task notifications.

Sending these manually is inefficient and error-prone.

This project solves the problem through Python automation.

---

# 💡 Industry Relevance

This project is relevant for:

- HR Automation
- Business Productivity Systems
- Workflow Automation
- Operations Management
- Admin Tools
- Customer Communication
- Educational Platforms
- Email Scheduling Systems

---

# ✨ Features

## Core Features
- 📩 Automated Email Sending
- 👤 Personalized Email Templates
- ⏰ Reminder Scheduling
- 📄 CSV-based Contact Management
- 📝 Logging System
- 📊 CSV Report Generation
- 🔒 Environment Variable Security
- 🧪 Dry Run Mode for Safe Testing

---

## Streamlit Dashboard Features
- 📋 Contact Preview
- ⏰ Reminder Schedule Preview
- 📈 Dashboard Statistics
- 🚀 Automation Execution Button
- 📁 Report Download
- 📝 Logs Viewer

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | CSV processing |
| SMTP | Email sending |
| Schedule | Task scheduling |
| Logging | System tracking |
| dotenv | Secure credentials |
| Streamlit | Dashboard UI |

---

# 📂 Folder Structure

```text
Email-Automation-Reminder-System/
│
├── data/
│   ├── contacts.csv
│   └── reminders.csv
│
├── templates/
│   └── reminder_template.txt
│
├── src/
│   ├── email_sender.py
│   ├── scheduler_service.py
│   ├── logger_config.py
│   └── utils.py
│
├── outputs/
│   └── email_report.csv
│
├── logs/
│   └── automation.log
│
├── dashboard/
│   └── app.py
│
├── images/
├── docs/
│
├── .env
├── .env.example
├── requirements.txt
├── README.md
└── main.py
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Email-Automation-Reminder-System.git
```

---

## 2️⃣ Navigate Into Project

```bash
cd Email-Automation-Reminder-System
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Required Libraries

```text
pandas
schedule
python-dotenv
streamlit
```

---

# 🔐 Environment Variables Setup

Create a `.env` file:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
DRY_RUN=True
```

---

# 🔒 Gmail SMTP Setup

1. Enable 2-Step Verification in Gmail
2. Generate App Password
3. Use App Password inside `.env`

---

# ▶️ How To Run

# Run Main Automation System

```bash
python main.py
```

---

# Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 🧪 Dry Run Mode

Dry Run Mode allows testing without sending real emails.

Inside `.env`

```env
DRY_RUN=True
```

This will:
- simulate email sending,
- generate logs,
- generate reports,
- avoid real email delivery.

---

# 📊 Sample Workflow

```text
Contacts CSV
      ↓
Reminder CSV
      ↓
Email Template
      ↓
Python Processing
      ↓
Message Personalization
      ↓
SMTP Email Sending
      ↓
Logging & Reports
      ↓
Dashboard Monitoring
```

---

# 📄 Sample CSV Files

## contacts.csv

```csv
id,name,email
1,John Doe,john@example.com
2,Sarah Smith,sarah@example.com
```

---

## reminders.csv

```csv
contact_id,subject,reminder_title,due_date
1,Meeting Reminder,Project Meeting,2026-05-15
2,Payment Reminder,Course Fee Payment,2026-05-17
```

---

# 📧 Sample Email Template

```text
Hello {name},

This is a reminder regarding:

Reminder: {reminder_title}

Due Date: {due_date}

Regards,
Automation Team
```

---

# 📁 Generated Outputs

## Logs

```text
logs/automation.log
```

---

## CSV Reports

```text
outputs/email_report.csv
```

---

# 🖥️ Streamlit Dashboard

Dashboard includes:
- Contacts Preview
- Reminder Preview
- Dashboard Metrics
- Logs Viewer
- CSV Report Download
- Automation Controls

---

# 📸 Recommended Screenshots

Save these screenshots in `/images`

- Project Folder Structure
- contacts.csv
- reminders.csv
- Email Template
- Terminal Dry Run Output
- Dashboard UI
- Logs Viewer
- CSV Reports
- GitHub Repository Preview

---

# 🔒 Security Best Practices

## Never Upload
- `.env`
- real passwords
- real employee/customer emails

---

## Upload Instead
- `.env.example`
- dummy datasets
- dry-run outputs

---

# 🧠 Learning Outcomes

Through this project, you will learn:
- Python automation
- SMTP email handling
- Scheduling systems
- CSV processing
- Logging systems
- Streamlit dashboard creation
- Environment variable security
- GitHub project management

---

# 🚀 Future Improvements

Possible upgrades:
- SQLite/MySQL database
- Email analytics dashboard
- WhatsApp/SMS integration
- Retry mechanism
- Admin authentication
- Cloud deployment
- Docker support
- Excel file uploads
- Attachment support

---

