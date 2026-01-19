import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ENDPOINT_STOCKS = "https://www.alphavantage.co/query"
ENDPOINT_NEWS = "https://newsapi.org/v2/everything"
STOCKS_API_KEY = os.getenv("STOCKS_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

stock_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCKS_API_KEY
}

response = requests.get(url=ENDPOINT_STOCKS, params=stock_api_params)
data = response.json()["Time Series (Daily)"]
if "Time Series (Daily)" not in data:
    raise Exception("Stock API error or rate limit reached")
data = data["Time Series (Daily)"]

data_list = list(data.values())

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(day_before_yesterday_closing_price) - float(yesterday_closing_price)
difference_percent = round((difference / float(yesterday_closing_price)) * 100, 2)

updown = "🔺" if difference > 0 else "🔻"

if abs(difference_percent) > 1:

    news_api_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(url=ENDPOINT_NEWS, params=news_api_params)
    articles = news_response.json()["articles"]

    first_three_articles = articles[:3]

    formatted_articles = [f"{STOCK}: {updown}{difference_percent}%\nHeadline: {article['title']}, \nBrief: {article['description']}" for article in first_three_articles]
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
            body="\n\n".join(formatted_articles),
            from_="TWILIO TRIAL NUMBER HERE",
            to= "YOUR NUMBER HERE"
        )

