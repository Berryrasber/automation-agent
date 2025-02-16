from flask import Flask, request, jsonify
from task_executor import execute_task  # Import task execution logic

app = Flask(__name__)

@app.route('/')
def home():
    return 'Flask API is running!'

@app.route('/run', methods=['POST'])
def run_task():
    """Executes a task based on the given plain-English description."""
    task_description = request.args.get('task')

    if not task_description:
        return jsonify({"error": "Task description is required"}), 400

    result = execute_task(task_description)

    if result["status"] == "success":
        return jsonify(result), 200
    elif result["error"] == "Bad Request":
        return jsonify(result), 400
    else:
        return jsonify(result), 500
    
import os
from flask import Response

@app.route('/read', methods=['GET'])
def read_file():
    """Reads the content of a file."""
    path = request.args.get('path')

    # Debugging: Print the requested path
    print(f"DEBUG: Requested file path -> {path}")

    # Ensure the path is inside /data for security
    if not path or not path.startswith("/data/") or ".." in path:
        return "", 404

    full_path = os.path.join(os.getcwd(), path.lstrip("/"))

    # Debugging: Print the actual full path
    print(f"DEBUG: Full file path -> {full_path}")

    if not os.path.exists(full_path):
        return "", 404

    try:
        with open(full_path, 'r') as f:
            content = f.read()
        return Response(content, mimetype='text/plain'), 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
