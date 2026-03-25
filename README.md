![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![API](https://img.shields.io/badge/API-External-brightgreen)
![Data Format](https://img.shields.io/badge/Data-JSON-lightblue)
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

## 🧠 Why I built this

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
    ├── requirements.txt
    ├── .env.example
    ├── .gitignore
    └── README.md
   
    

## 🔐 Environment Variables

All sensitive data is stored in a .env file (never pushed to GitHub):

    STOCKS_API_KEY=your_alpha_vantage_key
    NEWS_API_KEY=your_newsapi_key
    TWILIO_ACCOUNT_SID=your_twilio_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    TWILIO_PHONE_NUMBER=your_twilio_number
    TARGET_PHONE_NUMBER=your_number
  
  
## ▶️ How to run it

1. Clone the repo

        git clone https://github.com/fernandogrh/stock-alert-news-notifier.git
        cd stock-alert-news-notifier
    
2. Install dependencies

        pip install -r requirements.txt

3. Copy '.env.example' and rename it to '.env', then fill in your keys:

        STOCKS_API_KEY=your_alpha_vantage_key
        NEWS_API_KEY=your_newsapi_key
        TWILIO_ACCOUNT_SID=your_twilio_sid
        TWILIO_AUTH_TOKEN=your_twilio_auth_token
        TWILIO_PHONE_NUMBER=your_twilio_number
        TARGET_PHONE_NUMBER=your_number

4. Run:

        python main.py

## 📌 Notes for recruiters

- Secrets are not exposed

- Project follows clean code and best practices

- Code is modular and easy to extend

- Ready for features like:

- Multiple stocks

- Email alerts

- Scheduled execution (cron)

- Dashboard / UI

## 👤 Author

Built by **Fernando Ramirez**