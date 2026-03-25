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
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
TARGET_PHONE_NUMBER = os.getenv("TARGET_PHONE_NUMBER")

if not all([STOCKS_API_KEY, NEWS_API_KEY, TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, TWILIO_PHONE_NUMBER, TARGET_PHONE_NUMBER]):
    raise Exception("Missing one or more environment variables")


stock_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCKS_API_KEY
}

response = requests.get(url=ENDPOINT_STOCKS, params=stock_api_params, timeout=10)
response.raise_for_status()
stock_data = response.json()
if "Time Series (Daily)" not in stock_data:
    raise Exception(f"Stock API error or rate limit reached: {stock_data}")
daily_data = stock_data["Time Series (Daily)"]
data_list = list(daily_data.values())

if len(data_list) < 2:
    raise Exception("Not enough stock data returned from API")

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = yesterday_closing_price - day_before_yesterday_closing_price
difference_percent = round((difference / day_before_yesterday_closing_price) * 100, 2)

updown = "🔺" if difference > 0 else "🔻"

if abs(difference_percent) > 1:
    news_api_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(url=ENDPOINT_NEWS, params=news_api_params, timeout=10)
    news_response.raise_for_status()
    news_data = news_response.json()

    if "articles" not in news_data:
        raise Exception(f"News API error: {news_data}")

    articles = news_data["articles"][:3]

    formatted_articles = [f"{STOCK}: {updown}{abs(difference_percent)}%\nHeadline: {article.get('title', 'No title')}\nBrief: {article.get('description', 'No description')}" for article in articles]
    if formatted_articles:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
                body="\n\n".join(formatted_articles),
                from_=TWILIO_PHONE_NUMBER,
                to=TARGET_PHONE_NUMBER
            )
        print("Message sent successfully")
    else:
        print("No relevant news articles found")
else:
    print(f"No alert sent. Stock moved only {abs(difference_percent)}%")

