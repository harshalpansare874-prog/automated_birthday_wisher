# 🎂 Automated Birthday Wisher

A Python automation project that automatically sends personalized birthday wishes via email based on a birthday database.

## ✨ Features

- 📅 Checks birthdays automatically
- 📧 Sends personalized birthday emails
- 📝 Randomly selects from multiple letter templates
- 🐼 Uses Pandas to process birthday data
- 🔐 Keeps email credentials outside the source code using environment variables
- ⚙️ Uses SMTP for email delivery

## 🛠️ Technologies Used

- Python
- Pandas
- SMTP
- python-dotenv
- CSV
- Datetime
- Random
- OS

## 🚀 How to Run

1. Clone the repository.

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```
3. Create a .env file in the project directory:
MY_EMAIL=your_email@gmail.com
MY_PASSWORD=your_app_password
Add your birthday data to birthdays.csv.
Run:
python main.py

4. 📚 What I Learned
Automating tasks with Python
Working with Pandas and CSV data
Reading and managing environment variables
Sending emails using SMTP
Working with files and folders
Using random templates
Handling dates with Python

5. 🔒 Security Note
Email credentials are stored using environment variables and are not included in this repository.
The .env file and personal birthday data are excluded using .gitignore.
For Gmail, use an App Password rather than your regular account password.