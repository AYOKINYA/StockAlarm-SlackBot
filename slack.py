
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from dotenv import load_dotenv
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import time


def get_price(codes):
    if not isinstance(codes, list) and not isinstance(codes, tuple):
        print("Codes must be iterable")
        return None
    USER_AGENT = os.getenv('USER_AGENT')
    headers = {
        'User-agent': USER_AGENT}
    message = datetime.now().strftime('[%m/%d %H:%M:%S] ')
    for code in codes:
        url = 'http://finance.naver.com/item/sise.nhn?code={}'.format(code)
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "lxml")
        stock_name = soup.find('title').text.split(':')[0].strip()
        if len(stock_name) == 0:
            print("Invalid Stock Code : ", code)
            continue

        cur_price = soup.find('strong', id='_nowVal').text
        cur_rate = soup.find('strong', id='_rate').text.strip()

        message += '\n' + stock_name + " : " + cur_price + "(전일대비 " + cur_rate + ")"

    return message

def send_slack(strbuf):
    if strbuf == None:
        return None

    SLACK_TOKEN = os.getenv('SLACK_TOKEN')
    client = WebClient(token=SLACK_TOKEN)

    text = "Current Stock Price\n" + 'http://finance.naver.com/sise/sise_index.nhn?code=KOSPI\n' + strbuf

    try:
        response = client.chat_postMessage(channel="#test", text=text)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")

if __name__ == '__main__':
    
    load_dotenv(verbose=True)
    codes = ["000660", 251270]
    while True:
        strbuf = get_price(codes)
        print(strbuf)
        send_slack(strbuf)
        time.sleep(3600)