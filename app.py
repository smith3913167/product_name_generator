from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from gpt_generator import generate_product_name

# .env 파일 로드 (OPENAI_API_KEY를 환경변수로 불러오기 위함)
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/api/generate-name", methods=["POST"])
def generate_name():
    data = request.get_json()
    keyword = data.get("keyword", "").strip()

    if not keyword:
        return jsonify({"result": "❗ 키워드를 입력해 주세요."})

    try:
        result = generate_product_name(keyword)
        return jsonify({"result": result})
    except Exception as e:
        print("GPT 오류:", e)
        return jsonify({"result": "❌ GPT 상품명 생성 실패"})

# ✅ Render가 인식할 수 있도록 포트 바인딩 필수
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)