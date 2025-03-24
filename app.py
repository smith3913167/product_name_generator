from dotenv import load_dotenv
load_dotenv()
# app.py – GPT 상품명 생성 API 서버 (Flask)

from flask import Flask, request, jsonify
from flask_cors import CORS
from gpt_generator import generate_product_name
import os

app = Flask(__name__)
CORS(app)  # GitHub Pages 연결 허용

@app.route("/api/generate-name", methods=["POST"])
def generate_name():
    try:
        data = request.json
        keyword = data.get("keyword", "")
        trend = data.get("trendScore")
        click = data.get("clickScore")

        if not keyword:
            return jsonify({"error": "키워드를 입력하세요."}), 400

        result = generate_product_name(keyword, trend_score=trend, click_score=click)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))  # ← 5000 → 5050 변경
    app.run(host="0.0.0.0", port=port, debug=True)
