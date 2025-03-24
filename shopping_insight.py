url = "https://openapi.naver.com/v1/datalab/shopping/categories"

body = {
  "startDate": str(start),
  "endDate": str(end),
  "timeUnit": "week",
  "category": "50000002",  # 디지털/가전
  "device": "pc",
  "gender": "f",
  "ages": ["20", "30"]
}

response = requests.post(url, headers=headers, data=json.dumps(body))
result = response.json()

print("🛍️ 쇼핑인사이트 결과:")
for item in result['results'][0]['data']:
    print(f"{item['period']}: 클릭수 {item['ratio']}")