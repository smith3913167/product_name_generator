from flask import Flask, request, jsonify
from flask_cors import CORS
from gpt_generator import generate_product_name

app = Flask(__name__)
CORS(app)

@app.route("/api/generate-name", methods=["POST"])
def generate_name():
    data = request.get_json()
    keyword = data.get("keyword", "")
    if not keyword:
        return jsonify({"result": "❗ 키워드를 입력해 주세요."})

    result = generate_product_name(keyword)
    return jsonify({"result": result})  # ✅ 이 부분 중요