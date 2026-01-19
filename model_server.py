import os
import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)
MODEL_DIR = "./models/v1/"

# VULNERABILITY 1: Global Debug Mode enabled in production code
app.config['DEBUG'] = True 

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Client sends a model name (e.g., "fraud_detection_v1")
        model_name = request.json.get('model_name')
        data = np.array(request.json.get('features'))

        # VULNERABILITY 2: Path Traversal
        # Attacker sends model_name = "../../../etc/passwd" (if it were a file read)
        # or forces loading a malicious pickle file from /tmp
        model_path = os.path.join(MODEL_DIR, model_name + ".pkl")

        # VULNERABILITY 3: Insecure Deserialization (Pickle)
        # If an attacker can upload a file to the server (even to /tmp),
        # they can point this loader to it and achieve RCE.
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
            
        prediction = model.predict(data)
        
        return jsonify({"status": "success", "prediction": prediction.tolist()})

    except Exception as e:
        # VULNERABILITY 4: Information Leakage
        # Returning the raw exception trace to the user
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
