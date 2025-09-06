from flask import Flask, request, jsonify


app = Flask(__name__)


# In-memory data store for demo purposes only
data_store = {}




@app.route("/api/data", methods=["POST"]) 
def create_data():
	if not request.is_json:
		return jsonify({"error": "Request must be JSON"}), 400
	payload = request.get_json() or {}
	# Replace the store with provided payload
	data_store.clear()
	if isinstance(payload, dict):
		data_store.update(payload)
	else:
		data_store["value"] = payload
	return jsonify({"message": "Created", "data": data_store}), 201


@app.route("/api/data", methods=["PUT"]) 
def replace_data():
	if not request.is_json:
		return jsonify({"error": "Request must be JSON"}), 400
	payload = request.get_json() or {}
	# PUT = full replacement
	data_store.clear()
	if isinstance(payload, dict):
		data_store.update(payload)
	else:
		data_store["value"] = payload
	return jsonify({"message": "Replaced", "data": data_store}), 200


@app.route("/api/data", methods=["PATCH"]) 
def patch_data():
	if not request.is_json:
		return jsonify({"error": "Request must be JSON"}), 400
	payload = request.get_json() or {}
	# PATCH = partial update (dict merge)
	if isinstance(payload, dict):
		data_store.update(payload)
	else:
		data_store["value"] = payload
	return jsonify({"message": "Patched", "data": data_store}), 200



@app.route("/api/data", methods=["GET"])
def get_data():
	return jsonify({"data": data_store}), 200
	
@app.route("/api/data", methods=["DELETE"]) 
def delete_data():
	data_store.clear()
	return jsonify({"message": "Deleted"}), 200

if __name__ == "__main__":
	# Runs on http://localhost:5000
	app.run(host="127.0.0.1", port=5000, debug=True)


