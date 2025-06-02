from flask import Flask, request, jsonify
from memory_store import save_receipts, get_points
from receipt_utils import calculate_points

app = Flask(__name__)

@app.route("/receipts/{id}/points", methods = ["GET"])
def get_points_by_id(id):
    points = get_points(id)
    if points is None:
        return jsonify({"error": "Receipt not found"}), 400
    return jsonify({"points": points})


@app.route("/receipts/points", methods = ["POST"])
def process_receipts():
    receipt = request.get_json()
    if not receipt:
        return jsonify({"error": "Invalid receipt format"}), 400

    points = calculate_points(receipt)
    receipt_id = save_receipts(points)
    return jsonify({"id": receipt_id})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)