import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data to mock API behavior
mock_data = {
    "roblox": {"status": "success", "message": "Account found!", "results": []},
    "microsoft": {"status": "success", "message": "Account found!", "results": []},
    "steam": {"status": "error", "message": "No account found."}
}

@app.route('/recoverfile', methods=['POST'])
def recover_file():
    data = request.get_json()
    emails = data.get("emails", [])
    
    results = {}
    for email in emails:
        if "roblox" in email:
            results[email] = {"status": "SUCCESS", "message": "Account found!"}
        else:
            results[email] = {"status": "FAILED", "message": "Account not found."}

    return jsonify({"status": "success", "results": results})

@app.route('/bulk_solve', methods=['POST'])
def bulk_solve():
    data = request.get_json()
    combos = data.get("combos", [])
    
    results = {}
    for combo in combos:
        results[combo] = {"status": "SUCCESS", "message": "Account found!"}

    return jsonify({"status": "success", "results": results})

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    combo = data.get("combo", "")
    search_params = data.get("search_params", {})
    
    # Mock check behavior
    if combo.startswith("roblox"):
        return jsonify(mock_data["roblox"])
    elif combo.startswith("microsoft"):
        return jsonify(mock_data["microsoft"])
    elif combo.startswith("steam"):
        return jsonify(mock_data["steam"])

    return jsonify({"status": "error", "message": "Unsupported account type"})

if __name__ == "__main__":
    app.run(debug=True)
