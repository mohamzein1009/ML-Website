from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run_template', methods=['POST'])
def run_template():
    data = request.json  # User preferences from frontend
    script_name = data.get("script")  # Example: "data_cleaning.py"
    
    try:
        result = subprocess.run(["python", f"../{script_name}"], capture_output=True, text=True)
        return jsonify({"output": result.stdout})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)