![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-1.6.2-lightgrey?logo=pandas&logoColor=black)
![API](https://img.shields.io/badge/API-REST-brightgreen)
![JSON](https://img.shields.io/badge/JSON-lightblue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)
![GitHub](https://img.shields.io/badge/GitHub-version1.0-181717?logo=github&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

# 📈 Stock Alert & News Notifier (Python)
### Real-time stock movement alerts with breaking news straight to your phone. Built to show clean Python logic, API integration, and secure environment handling.


## 🚀 What this project does

This Python script tracks a stock (currently **TSLA**) and:

- 📊 Fetches daily stock prices using **Alpha Vantage**

- 📉 Calculates the percentage change between the last two trading days

- 📰 Pulls the **latest news headlines** if the price moves significantly

- 📩 Sends a **clean SMS alert** using Twilio

- 🔐 Keeps **all secrets safe** using environment variables (.env)

If the stock moves more than ±1%, you get notified instantly.

🧠 Why I built this

I wanted a **real-world project** that proves I can:

- Work with **external APIs**

- Handle **JSON data**

- Write **clean, readable Python**

- Manage **secrets securely** (no hardcoded keys)

- Build something actually useful, not just tutorial fluff

This is the kind of script you could expand into a real monitoring or trading tool.

## 🛠️ Tech Stack

- **Python 3**

- **Requests** – API calls

- **Twilio** – SMS notifications

- **dotenv** – environment variable management

- **Alpha Vantage API** – stock data

- **NewsAPI** – financial news

## 📂 Project Structure
 
    ├── main.py
    ├── .gitignore
    ├── .env        # not committed (API keys & secrets)
    └── README.md

## 🔐 Environment Variables

All sensitive data is stored in a .env file (never pushed to GitHub):

    STOCKS_API_KEY=your_alpha_vantage_key
    NEWS_API_KEY=your_newsapi_key
    TWILIO_ACCOUNT_SID=your_twilio_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token

## ▶️ How to run it

1. Clone the repo

2. Install dependencies


    pip install requests python-dotenv twilio

3. Create a .env file with your API keys

4. Run:


    python main.py

## 📌 Notes for recruiters

- Secrets are not exposed

- Project follows best practices

- Code is modular and easy to extend

- Ready for features like:

- Multiple stocks

- Email alerts

- Scheduled execution (cron)

- Dashboard / UI

## 👤 Author

Built by **Fernando Ramirez**