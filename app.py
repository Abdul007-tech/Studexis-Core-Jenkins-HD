from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "Ok"}), 200

@app.route("/tasks", methods=["GET", "POST"])
def task_handler():
    if request.method == "POST":
        data = request.get_json()
        task = {"id": len(tasks)+1, "title": data.get("title", "")}
        tasks.append(task)
        return jsonify(task), 201
    return jsonify(tasks), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
