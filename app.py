from flask import Flask, jsonify, request
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)

@app.route('/api/vxlans', methods=['POST'])
def create_vxlan():
    data = request.json
    return jsonify({"message": "VXLAN created", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
