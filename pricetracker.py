import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.ca/Logitech-Driving-Feedback-Steering-941-000121/dp/B00Z0UWV98/ref=sr_1_3?crid=2AKGX2PDK6MTX&keywords=logitech+steering+wheel&qid=1574312788&sprefix=logitech+stee%2Caps%2C191&sr=8-3'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

def price_checker():
    page = requests.get(URL, headers=headers)

    chickenSoup = BeautifulSoup(page.content, 'html.parser')

    productName = chickenSoup.find(id="productTitle").get_text()
    productPrice = chickenSoup.find(id="priceblock_ourprice").get_text()
    getPrice = float(productPrice[0.5])

    if(getPrice < 200):
        notify()
    print(productName.strip())

    if (getPrice > 200):
        notify()

def notify():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Email and password combo changed due to privacy 
    server.login('xyz@gmail.com', 'abc123;')

    subject = 'Price Drop!'
    message_body = "Check this amazon link https://www.amazon.ca/Logitech-Driving-Feedback-Steering-941-000121/dp/B00Z0UWV98/ref=sr_1_3?crid=2AKGX2PDK6MTX&keywords=logitech+steering+wheel&qid=1574312788&sprefix=logitech+stee%2Caps%2C191&sr=8-3"
    
    message = f"Subject: {subject}\n\n{message_body}"

    server.sendmail(
        'huzi.blizzard96@gmail.com',
        'huzaifa_khalid9@hotmail.com',
        message
    )
    print('EMAIL SENT')
    server.quit()

while(True):
    price_checker()
    time.sleep(60 * 60)
