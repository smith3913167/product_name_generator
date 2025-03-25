from flask import Flask, request, jsonify
from flask_cors import CORS
from gpt_generator import generate_product_name
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/api/generate-name", methods=["POST"])
def generate_name():
    try:
        data = request.get_json()

        required_keys = ["keyword", "category", "monthly_search", "competition_score", "related_keywords"]
        if not all(key in data for key in required_keys):
            return jsonify({"error": "입력값 부족"}), 400

        keyword = data["keyword"]
        category = data["category"]
        monthly_search = data["monthly_search"]
        competition_score = data["competition_score"]
        related_keywords = data["related_keywords"]

        result = generate_product_name(
            keyword=keyword,
            category=category,
            monthly_search=monthly_search,
            competition_score=competition_score,
            related_keywords=related_keywords
        )

        # 🔥 result는 딕셔너리 {"generated_name": "추천상품명"} 형태
        return jsonify({"name": result["generated_name"]})

    except Exception as e:
        return jsonify({"error": f"서버 오류: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)