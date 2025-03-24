import os
from dotenv import load_dotenv
from openai import OpenAI
import logging

# .env에서 환경 변수 로드
load_dotenv()

# OpenAI API 키 불러오기
openai_api_key = os.getenv("OPENAI_API_KEY")

# OpenAI 클라이언트 설정
client = OpenAI(api_key=openai_api_key)

# GPT를 활용한 상품명 생성 함수
def generate_product_name(keyword, category, monthly_search, competition_score, related_keywords):
    try:
        prompt = (
            f"당신은 스마트한 마케팅 전문가입니다. "
            f"다음 정보를 바탕으로 매력적이고 클릭을 유도할 수 있는 상품명을 하나 추천해주세요:\n\n"
            f"- 키워드: {keyword}\n"
            f"- 카테고리: {category}\n"
            f"- 최근 검색량: {monthly_search}\n"
            f"- 경쟁 강도: {competition_score}\n"
            f"- 관련 키워드: {', '.join(related_keywords)}\n\n"
            f"✨ 추천 상품명:"
        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=50,
        )

        product_name = response.choices[0].message.content.strip()
        return {"generated_name": product_name}

    except Exception as e:
        logging.error(f"GPT 상품명 생성 실패: {e}")
        return {"generated_name": "GPT 생성 실패"}