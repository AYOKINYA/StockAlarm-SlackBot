requirements :

Python version: 3.6+

- requests : send requests to websites
- slack_sdk : python slack SDK
- python-dotenv : read .env file
- beautifulsoup4 : crawl data from NAVER 금융

Get your own .env file

```jsx
SLACK_TOKEN=xoxb-...  #Bot User OAuth Access Token from Slack API
USER_AGENT=Mozilla/5.0... #Get your user-agent @ http://httpbin.org/user-agent
```

```python
set stock codes @slack.py line 54
ex) codes = ["000660", 251270]

python slack.py #your slackbot sends current stock price every hour
```
