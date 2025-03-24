import requests
import json
import datetime

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

# 날짜 계산
end = datetime.date.today()
start = end - datetime.timedelta(days=30)

url = "https://openapi.naver.com/v1/datalab/search"

headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret,
    "Content-Type": "application/json"
}

body = {
    "startDate": str(start),
    "endDate": str(end),
    "timeUnit": "date",
    "keywordGroups": [
        {"groupName": "무선청소기", "keywords": ["무선청소기"]},
        {"groupName": "캠핑의자", "keywords": ["캠핑의자"]}
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(body))
result = response.json()

for group in result["results"]:
    print(f"\n📈 {group['title']} 검색 추이")
    for day in group["data"]:
        print(f"{day['period']}: {day['ratio']}")