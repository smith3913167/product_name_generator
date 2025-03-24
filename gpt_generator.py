import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_product_name(keyword):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 상품명 작명 전문가입니다."},
                {"role": "user", "content": f"{keyword}를 포함해서 매력적인 쇼핑몰용 상품명을 지어줘. 한 문장만 출력해줘."}
            ],
            max_tokens=100,
            temperature=0.7,
        )
        result = response.choices[0].message.content.strip()
        return result
    except Exception as e:
        print(f"❌ GPT 생성 중 오류 발생: {e}")
        return "GPT 생성 실패"  # ✅ 문자열 리턴