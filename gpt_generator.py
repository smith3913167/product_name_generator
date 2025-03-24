# gpt_generator.py

import openai
import os

# OpenAI API 키 설정 (환경변수 또는 직접 입력 가능)
openai.api_key = os.getenv("OPENAI_API_KEY", "your-api-key")

def generate_product_name(keyword, trend_score=None, click_score=None):
    prompt = f"""
다음 키워드를 활용해서 네이버 쇼핑에 어울리는 상품명을 만들어줘.
30자 이내의 짧고 간결한 스타일로, 검색 클릭을 유도할 수 있는 문구면 좋겠어.

키워드: {keyword}
"""
    if trend_score:
        prompt += f"\n참고: 최근 검색 비율 {trend_score}"
    if click_score:
        prompt += f" / 클릭 비율 {click_score}"

    models = ["gpt-4", "gpt-3.5-turbo"]

    for model in models:
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            return f"[{model}] {response.choices[0].message['content'].strip()}"
        except Exception as e:
            print(f"⚠️ {model} 실패: {e}")
            continue

    return "❌ GPT 생성 실패"