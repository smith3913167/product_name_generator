# gpt_module.py

# OpenAI GPT request module with test coverage, safe for environments without micropip

try:
    import openai
    import os
except ModuleNotFoundError as e:
    raise ImportError("필수 모듈이 누락되었습니다. 'openai'와 'os' 모듈이 필요합니다.") from e

# 환경 변수에서 API 키 로드
openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")

def _build_prompt(product_info):
    return f"""
다음 키워드를 활용하여 쇼핑몰용 상품명 스타일로 자연스럽고 매력적인 한 문장을 만들어줘. 40자 이내로, 클릭을 유도할 수 있도록 구성해줘.

키워드: {product_info}
"""

def generate_shop_title(product_info, model_version="gpt-4"):
    prompt = _build_prompt(product_info)

    try:
        response = openai.ChatCompletion.create(
            model=model_version,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"[ERROR: {str(e)}]"

# Test cases
if __name__ == "__main__":
    test_inputs = [
        "코베아 캠핑의자 경량 접이식 릴렉스체어 여름용",
        "샤오미 무선청소기 강력흡입 저소음 가정용",
        "정관장 홍삼정 6년근 면역력증진 건강식품"
    ]

    for input_text in test_inputs:
        print("====================")
        print(f"[GPT-4] 입력: {input_text}")
        print(generate_shop_title(input_text, model_version="gpt-4"))
        print(f"[GPT-3.5] 입력: {input_text}")
        print(generate_shop_title(input_text, model_version="gpt-3.5-turbo"))