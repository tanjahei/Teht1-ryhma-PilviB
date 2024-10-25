from flask import Flask, send_file, jsonify
import os
import random
import string
import hashlib

app = Flask(__name__)

# Polku, johon tiedosto tallennetaan
data_path = "/serverdata/random_file.txt"

@app.route('/generate', methods=['GET'])
def generate_file():
    # Luodaan satunnainen teksti
    random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=1024))
    with open(data_path, 'w') as f:
        f.write(random_text)
    
    # Lasketaan checksum
    checksum = hashlib.md5(random_text.encode()).hexdigest()

    return jsonify({"checksum": checksum, "message": "File generated."})

@app.route('/file', methods=['GET'])
def send_random_file():
    if os.path.exists(data_path):
        print(f"Sending file: {data_path}")
        return send_file(data_path, as_attachment=True)
    else:
        print(f"File not found: {data_path}")
        return jsonify({"error": "File not found."}), 404

@app.route('/checksum', methods=['GET'])
def get_checksum():
    if os.path.exists(data_path):
        with open(data_path, 'r') as f:
            content = f.read()
        checksum = hashlib.md5(content.encode()).hexdigest()
        print(f"Calculated checksum: {checksum}")
        return jsonify({"checksum": checksum})
    else:
        print(f"File not found: {data_path}")
        return jsonify({"error: File not found."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
